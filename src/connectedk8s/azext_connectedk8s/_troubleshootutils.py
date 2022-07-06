# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from argparse import Namespace
from pydoc import cli
from kubernetes import client, config, watch, utils
from binascii import a2b_hex
from logging import exception
import os
import json
import datetime
from subprocess import Popen, PIPE, run, STDOUT, call, DEVNULL
from base64 import b64encode, b64decode
from unicodedata import name
from azure.core.exceptions import ClientAuthenticationError
import shutil
from knack.util import CLIError
from knack.log import get_logger
from azure.cli.core import telemetry
from azure.cli.core.azclierror import ManualInterrupt, InvalidArgumentValueError, UnclassifiedUserFault, CLIInternalError, FileOperationError, ClientRequestError, DeploymentError, ValidationError, ArgumentUsageError, MutuallyExclusiveArgumentError, RequiredArgumentMissingError, ResourceNotFoundError
from azext_connectedk8s._client_factory import _graph_client_factory
from azext_connectedk8s._client_factory import cf_resource_groups
from azext_connectedk8s._client_factory import _resource_client_factory
from azext_connectedk8s._client_factory import _resource_providers_client
from azext_connectedk8s._client_factory import get_graph_client_service_principals
import azext_connectedk8s._constants as consts
import azext_connectedk8s.custom as custom
from .vendored_sdks.models import ConnectedCluster, ConnectedClusterIdentity, ListClusterUserCredentialProperties
from threading import Timer, Thread
from azure.cli.core import get_default_cli
logger = get_logger(__name__)
# pylint:disable=unused-argument
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=line-too-long


diagnoser_output = []


def create_folder_diagnosticlogs(time_stamp):

    global diagnoser_output

    try:

        home_dir = os.path.expanduser('~')
        filepath = os.path.join(home_dir, '.azure', 'arc_diagnostic_logs')

        # Creating Diagnostic folder and its subfolder with the given timestamp and cluster name to store all the logs
        try:
            os.mkdir(filepath)
        except FileExistsError:
            pass

        filepath_with_timestamp = os.path.join(filepath, time_stamp)
        try:
            os.mkdir(filepath_with_timestamp)
        except FileExistsError:
            pass

        return filepath_with_timestamp, "folder_created"

    except OSError as e:
        if "[Errno 28]" in str(e):
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            return "", "no_storage_space"
        else:
            logger.warning("An exception has occured while creating the diagnostic logs folder in your local machine. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Storage_Available_Fault_Type, summary="Error while trying to create diagnostic logs folder")
            diagnoser_output.append("An exception has occured while creating the diagnostic logs folder in your local machine. Exception: {}".format(str(e)) + "\n")
            return "", "folder_not_created"

    except Exception as e:
        logger.warning("An exception has occured while creating the diagnostic logs folder in your local machine. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Storage_Available_Fault_Type, summary="Error while trying to create diagnostic logs folder")
        diagnoser_output.append("An exception has occured while creating the diagnostic logs folder in your local machine. Exception: {}".format(str(e)) + "\n")
        return "", "folder_not_created"


def connected_cluster_logger(filepath_with_timestamp, connected_cluster, storage_space_available):

    global diagnoser_output

    try:
        connected_cluster_resource_path = os.path.join(filepath_with_timestamp, "Connected_cluster_resource.txt")
        if storage_space_available:
            with open(connected_cluster_resource_path, 'w+') as cc:
                cc.write(str(connected_cluster))
        return "Passed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while trying to store the connected cluster resource logs from the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Connected_Cluster_Resource_Fault_Type, summary="Eror occure while storing the connected cluster resource logs")
            diagnoser_output.append("An exception has occured while trying to store the connected cluster resource logs from the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while trying to store the connected cluster resource logs from the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Connected_Cluster_Resource_Fault_Type, summary="Eror occure while storing the connected cluster resource logs")
        diagnoser_output.append("An exception has occured while trying to store the connected cluster resource logs from the cluster. Exception: {}".format(str(e)) + "\n")

    return "Failed", storage_space_available


def retrieve_arc_agents_logs(corev1_api_instance, filepath_with_timestamp, storage_space_available):

    global diagnoser_output

    try:

        if storage_space_available:
            # To retrieve all of the arc agents pods that are presesnt in the Cluster
            arc_agents_pod_list = corev1_api_instance.list_namespaced_pod(namespace="azure-arc")

            # Traversing thorugh all agents
            for each_agent_pod in arc_agents_pod_list.items:

                # Fethcing the current Pod name and creating a folder with that name inside the timestamp folder
                agent_name = each_agent_pod.metadata.name
                arc_agent_logs_path = os.path.join(filepath_with_timestamp, "Arc_Agents_logs")
                try:
                    os.mkdir(arc_agent_logs_path)
                except FileExistsError:
                    pass

                agent_name_logs_path = os.path.join(arc_agent_logs_path, agent_name)
                try:
                    os.mkdir(agent_name_logs_path)
                except FileExistsError:
                    pass

                # If the agent is not in Running state we wont be able to get logs of the containers
                if(each_agent_pod.status.phase != "Running"):
                    continue

                # Traversing through all of the containers present inside each pods
                for each_container in each_agent_pod.spec.containers:

                    # Fetching the Container name
                    container_name = each_container.name

                    # Creating a text file with the name of the container and adding that containers logs in it
                    container_log = corev1_api_instance.read_namespaced_pod_log(name=agent_name, container=container_name, namespace="azure-arc")

                    arc_agent_container_logs = os.path.join(agent_name_logs_path, container_name + ".txt")
                    with open(arc_agent_container_logs, 'w+') as container_file:
                        container_file.write(str(container_log))

        return "Passed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while trying to fetch the azure arc agents logs from the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Arc_Agents_Logger_Fault_Type, summary="Error occured in arc agents logger")
            diagnoser_output.append("An exception has occured while trying to fetch the azure arc agents logs from the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while trying to fetch the azure arc agents logs from the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Arc_Agents_Logger_Fault_Type, summary="Error occured in arc agents logger")
        diagnoser_output.append("An exception has occured while trying to fetch the azure arc agents logs from the cluster. Exception: {}".format(str(e)) + "\n")

    return "Failed", storage_space_available


def retrieve_arc_agents_event_logs(filepath_with_timestamp, storage_space_available):

    global diagnoser_output

    try:

        if storage_space_available:

            # CMD command to get helm values in azure arc and converting it to json format
            command = ["kubectl", "get", "events", "-n", "azure-arc", "--output", "json"]

            # Using Popen to execute the helm get values command and fetching the output
            response_kubectl_get_events = Popen(command, stdout=PIPE, stderr=PIPE)
            output_kubectl_get_events, error_kubectl_get_events = response_kubectl_get_events.communicate()

            if response_kubectl_get_events.returncode != 0:
                telemetry.set_exception(exception=error_kubectl_get_events.decode("ascii"), fault_type=consts.Kubectl_Get_Events_Failed, summary='Error while doing kubectl get events')
                logger.warning("Error while doing kubectl get events")

            # Converting output obtained in json format and fetching the clusterconnect-agent feature
            events_json = json.loads(output_kubectl_get_events)

            event_logs_path = os.path.join(filepath_with_timestamp, "Arc_Agents_Events.txt")
            with open(event_logs_path, 'w+') as event_log:

                for events in events_json["items"]:
                        event_log.write(str(events) + "\n")

            return "Passed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while trying to fetch the events occured in azure-arc namespace from the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Arc_Agents_Events_Logger_Fault_Type, summary="Error occured in arc agents events logger")
            diagnoser_output.append("An exception has occured while trying to fetch the events occured in azure-arc namespace from the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while trying to fetch the events occured in azure-arc namespace from the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Arc_Agents_Events_Logger_Fault_Type, summary="Error occured in arc agents events logger")
        diagnoser_output.append("An exception has occured while trying to fetch the events occured in azure-arc namespace from the cluster. Exception: {}".format(str(e)) + "\n")

    return "Failed", storage_space_available


def retrieve_deployments_logs(appv1_api_instance, filepath_with_timestamp, storage_space_available):

    global diagnoser_output

    try:

        if storage_space_available:

            # Creating new Deployment Logs folder in the given timestamp folder
            deployments_path = os.path.join(filepath_with_timestamp, "Deployment_logs")
            try:
                os.mkdir(deployments_path)
            except FileExistsError:
                pass

            # To retrieve all the the deployements that are present in the Cluster
            deployments_list = appv1_api_instance.list_namespaced_deployment("azure-arc")

            # Traversing through all the deployments present
            for deployment in deployments_list.items:

                # Fetching the deployment name
                deployment_name = deployment.metadata.name

                deployment_logs_path = os.path.join(deployments_path, deployment_name + ".txt")
                # Creating a text file with the name of the deployment and adding deployment status in it
                with open(deployment_logs_path, 'w+') as deployment_file:
                    deployment_file.write(str(deployment.status))

        return "Passed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while trying to fetch the azure arc deployment logs from the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Arc_Deployments_Logger_Fault_Type, summary="Error occured in deployments logger")
            diagnoser_output.append("An exception has occured while trying to fetch the azure arc deployment logs from the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while trying to fetch the azure arc deployment logs from the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Arc_Deployments_Logger_Fault_Type, summary="Error occured in deployments logger")
        diagnoser_output.append("An exception has occured while trying to fetch the azure arc deployment logs from the cluster. Exception: {}".format(str(e)) + "\n")

    return "Failed", storage_space_available


def check_agent_state(corev1_api_instance, filepath_with_timestamp, storage_space_available):

    global diagnoser_output
    all_agents_stuck = "Incomplete"
    try:

        # To check if agents are not in Running state
        agent_state_counter = 0

        # To check if all the containers are working for the Running agents
        agent_conatiners_counter = 0

        # If all agents are stuck we will skip the certificates check
        all_agents_stuck = "True"

        agent_state_path = os.path.join(filepath_with_timestamp, "Agent_State.txt")
        with open(agent_state_path, 'w+') as agent_state:
            # To retrieve all of the arc agent pods that are presesnt in the Cluster
            arc_agents_pod_list = corev1_api_instance.list_namespaced_pod(namespace="azure-arc")

            # Check if any arc agent other than kube aadp proxy is not in Running state
            for each_agent_pod in arc_agents_pod_list.items:

                if storage_space_available:

                    # Storing the state of the arc agent in the user machine
                    agent_state.write(each_agent_pod.metadata.name + " : Status = " + each_agent_pod.status.phase + "\n")

                if each_agent_pod.status.phase != 'Running':
                    agent_state_counter = 1
                    storage_space_available = describe_stuck_agent_log(filepath_with_timestamp, corev1_api_instance, each_agent_pod.metadata.name, storage_space_available)
                else:
                    all_agents_stuck = "False"

                    for each_container_status in each_agent_pod.status.container_statuses:

                        if each_container_status.ready is False:
                            agent_conatiners_counter = 1

                        agent_state.write("\t" + each_container_status.name + " :" + " Status = " + str(each_container_status.ready) + ", Restart_Counts = " + str(each_container_status.restart_count) + "\n")
                agent_state.write("\n")

        # Displaying error if the arc agents are in pending state.
        if agent_state_counter:
            print("Error: One or more Azure Arc agents are in pending state. It may be caused due to insufficient resource availability on the cluster.\n ")
            diagnoser_output.append("Error: One or more Azure Arc agents are in pending state. It may be caused due to insufficient resource availability on the cluster.\n ")
            return "Failed", storage_space_available, all_agents_stuck

        elif agent_conatiners_counter:
            print("Error: One or more containers in the Azure Arc agents are not in ready state. It may be caused due to insufficient resources or connectivity issues on the cluster.\n")
            diagnoser_output.append("Error: One or more containers in the Azure Arc agents are not in ready state. It may be caused due to insufficient resource availability on the cluster.\n ")
            return "Failed", storage_space_available, all_agents_stuck

        return "Passed", storage_space_available, all_agents_stuck

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while trying to check the azure arc agents state in the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Agent_State_Check_Fault_Type, summary="Error ocuured while performing the agent state check")
            diagnoser_output.append("An exception has occured while trying to check the azure arc agents state in the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while trying to check the azure arc agents state in the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Agent_State_Check_Fault_Type, summary="Error ocuured while performing the agent state check")
        diagnoser_output.append("An exception has occured while trying to check the azure arc agents state in the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete", storage_space_available, all_agents_stuck


def check_agent_version(connected_cluster, azure_arc_agent_version):

    global diagnoser_output

    try:

        # If the agent version in the connected cluster resource is none skip the check
        if(connected_cluster.agent_version is None):
            return "Incomplete"

        # To get user agent verison and the latest agent version
        user_agent_version = connected_cluster.agent_version
        current_user_version = user_agent_version.split('.')
        latest_agent_version = azure_arc_agent_version.split('.')

        # Comparing if the user version is comaptible or not
        if((int(current_user_version[0]) < int(latest_agent_version[0])) or (int(latest_agent_version[1]) - int(current_user_version[1]) > 2)):
            logger.warning("We found that you are on an older agent version that is not supported.\n Please visit this link to know the agent version support policy 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/agent-upgrade#version-support-policy'.\n")
            diagnoser_output.append("We found that you are on an older agent version that is not supported.\n Please visit this link to know the agent version support policy 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/agent-upgrade#version-support-policy'.\n")
            return "Failed"

        return "Passed"

    except Exception as e:
        logger.warning("An exception has occured while trying to check the azure arc agents version in the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Agent_Version_Check_Fault_Type, summary="Error occured while performing the agent version check")
        diagnoser_output.append("An exception has occured while trying to check the azure arc agents version in the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete"


def check_diagnoser_container(corev1_api_instance, batchv1_api_instance, filepath_with_timestamp, storage_space_available, namespace, absolute_path):
    global diagnoser_output

    try:

        # Setting DNS and Outbound Check as working
        dns_check = "Starting"
        outbound_connectivity_check = "Starting"

        # Executing the Diagnoser job and fetching the logs obtained
        diagnoser_container_log = executing_diagnoser_job(corev1_api_instance, batchv1_api_instance, namespace, absolute_path)

        if(diagnoser_container_log != ""):
            dns_check, storage_space_available = check_cluster_DNS(diagnoser_container_log, filepath_with_timestamp, storage_space_available)
            outbound_connectivity_check, storage_space_available = check_cluster_outbound_connectivity(diagnoser_container_log, filepath_with_timestamp, storage_space_available)
        else:
            return "Incomplete", storage_space_available

        if(dns_check == "Passed" and outbound_connectivity_check == "Passed"):
            return "Passed", storage_space_available
        elif(dns_check == "Incomplete" or outbound_connectivity_check == "Incomplete"):
            return "Incomplete", storage_space_available
        else:
            return "Failed", storage_space_available

    except Exception as e:
        logger.warning("An exception has occured while trying to perform diagnoser container check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Diagnoser_Container_Check_Fault_Type, summary="Error occured while performing the diagnoser container checks")
        diagnoser_output.append("An exception has occured while trying to perform diagnoser container check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete", storage_space_available


def executing_diagnoser_job(corev1_api_instance, batchv1_api_instance, namespace, absolute_path):

    global diagnoser_output

    # Setting the log output as Empty
    diagnoser_container_log = ""
    yaml_file_path = os.path.join(absolute_path, "troubleshoot_diagnoser_job.yaml")
    cmd_delete_job = ["kubectl", "delete", "-f", ""]
    cmd_delete_job[3] = str(yaml_file_path)

    # To handle the user keyboard Interrupt
    try:

        # Executing the diagnoser_job.yaml
        config.load_kube_config()
        k8s_client = client.ApiClient()

        try:
            utils.create_from_yaml(k8s_client, yaml_file_path)
        except Exception as e:
            all_exceptions_list = str(e).split('\n')
            counter = 0
            for ind_exception in all_exceptions_list:
                if("Error from server (Conflict)" in ind_exception or ind_exception == ""):
                    continue
                else:
                    if(counter == 0):
                        diagnoser_output.append("An Error occured while trying to execute diagnoser_job.yaml.")
                        logger.warning("An Error occured while trying to execute diagnoser_job.yaml.")
                        counter = 1
                        logger.warning(ind_exception)
                    else:
                        logger.warning(ind_exception)
            logger.warning("\n")
            if(counter == 1):
                Popen(cmd_delete_job, stdout=PIPE, stderr=PIPE)
                return ""

        # Watching for diagnoser contianer to reach in completed stage
        w = watch.Watch()
        counter = 0

        for event in w.stream(batchv1_api_instance.list_namespaced_job, namespace=namespace, label_selector="", timeout_seconds=90):

            try:

                if event["object"].metadata.name == "azure-arc-diagnoser-job" and event["object"].status.conditions[0].type == "Complete":
                    counter = 1
                    w.stop()

            except Exception as e:
                continue
            else:
                    continue

        # If container not created then clearing all the resource with proper error message
        if (counter == 0):
            logger.warning("Unable to execute the diagnoser job in the cluster. It may be caused due to insufficient resource availability on the cluster.\n")
            Popen(cmd_delete_job, stdout=PIPE, stderr=PIPE)
            diagnoser_output.append("Unable to execute the diagnoser job in the cluster. It may be caused due to insufficient resource availability on the cluster.\n")
            return ""

        else:

            # Fetching the Diagnoser Container logs
            try:

                job_name = "azure-arc-diagnoser-job"

                all_pods = corev1_api_instance.list_namespaced_pod(namespace)
                # Traversing thorugh all agents
                for each_pod in all_pods.items:

                    # Fethcing the current Pod name and creating a folder with that name inside the timestamp folder
                    pod_name = each_pod.metadata.name

                    if(pod_name.startswith(job_name)):

                        # Creating a text file with the name of the container and adding that containers logs in it
                        diagnoser_container_log = corev1_api_instance.read_namespaced_pod_log(name=pod_name, container="azure-arc-diagnoser-container", namespace=namespace)

                # Clearing all the resources after fetching the diagnoser container logs
                Popen(cmd_delete_job, stdout=PIPE, stderr=PIPE)

            except Exception as e:
                Popen(cmd_delete_job, stdout=PIPE, stderr=PIPE)
                return ""

    except Exception as e:
        logger.warning("An exception has occured while trying to execute the diagnoser job in the cluster. Exception: {}".format(str(e)) + "\n")
        Popen(cmd_delete_job, stdout=PIPE, stderr=PIPE)
        telemetry.set_exception(exception=e, fault_type=consts.Executing_Diagnoser_Job_Fault_Type, summary="Error while executing Diagnoser Job")
        diagnoser_output.append("An exception has occured while trying to execute the diagnoser job in the cluster. Exception: {}".format(str(e)) + "\n")

    return diagnoser_container_log


def check_cluster_DNS(diagnoser_container_log, filepath_with_timestamp, storage_space_available):

    global diagnoser_output

    try:
        # To retreive only the DNS lookup result from the diagnoser container logs
        dns_check = diagnoser_container_log[0:len(diagnoser_container_log) - 5:]

        # Validating if DNS is working or not and displaying proper result
        if("NXDOMAIN" in dns_check or "connection timed out" in dns_check):
            print("Error: We found an issue with the DNS resolution on your cluster. For details about debugging DNS issues visit 'https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/'.\n")
            diagnoser_output.append("Error: We found an issue with the DNS resolution on your cluster. For details about debugging DNS issues visit 'https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/'.\n")
            if storage_space_available:
                dns_check_path = os.path.join(filepath_with_timestamp, "DNS_Check.txt")
                with open(dns_check_path, 'w+') as dns:
                    dns.write(dns_check + "\nWe found an issue with the DNS resolution on your cluster.")
            return "Failed", storage_space_available

        else:
            if storage_space_available:
                dns_check_path = os.path.join(filepath_with_timestamp, "DNS_Check.txt")
                with open(dns_check_path, 'w+') as dns:
                    dns.write(dns_check + "\nCluster DNS check passed successfully.")
            return "Passed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while performing the DNS check on the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Cluster_DNS_Check_Fault_Type, summary="Error occured while performing cluster DNS check")
            diagnoser_output.append("An exception has occured while performing the DNS check on the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while performing the DNS check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Cluster_DNS_Check_Fault_Type, summary="Error occured while performing cluster DNS check")
        diagnoser_output.append("An exception has occured while performing the DNS check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete", storage_space_available


def check_cluster_outbound_connectivity(diagnoser_container_log, filepath_with_timestamp, storage_space_available):

    global diagnoser_output

    try:

        # To retreive only the outbound connectivity result from the diagnoser container logs
        outbound_check = diagnoser_container_log[-4:-1:]

        # Validating if outbound connectiivty is working or not and displaying proper result
        if(outbound_check != "000"):
            if storage_space_available:
                outbound_connectivity_check_path = os.path.join(filepath_with_timestamp, "Outbound_Network_Connectivity_Check.txt")
                with open(outbound_connectivity_check_path, 'w+') as outbound:
                    outbound.write("Response code " + outbound_check + "\nOutbound network connectivity check passed successfully.")
            return "Passed", storage_space_available
        else:
            print("Error: We found an issue with outbound network connectivity from the cluster.\nIf your cluster is behind an outbound proxy server, please ensure that you have passed proxy paramaters during the onboarding of your cluster.\nFor more details visit 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#connect-using-an-outbound-proxy-server'.\nPlease ensure to meet the following network requirements 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#meet-network-requirements' \n")
            diagnoser_output.append("Error: We found an issue with outbound network connectivity from the cluster.\nIf your cluster is behind an outbound proxy server, please ensure that you have passed proxy paramaters during the onboarding of your cluster.\nFor more details visit 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#connect-using-an-outbound-proxy-server'.\nPlease ensure to meet the following network requirements 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#meet-network-requirements' \n")
            if storage_space_available:
                outbound_connectivity_check_path = os.path.join(filepath_with_timestamp, "Outbound_Network_Connectivity_Check.txt")
                with open(outbound_connectivity_check_path, 'w+') as outbound:
                    outbound.write("Response code " + outbound_check + "\nWe found an issue with Outbound network connectivity from the cluster.")
            return "Failed", storage_space_available

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while performing the outbound connectivity check on the cluster. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Outbound_Connectivity_Check_Fault_Type, summary="Error occured while performing outbound connectivity check in the cluster")
            diagnoser_output.append("An exception has occured while performing the outbound connectivity check on the cluster. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
        logger.warning("An exception has occured while performing the outbound connectivity check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Outbound_Connectivity_Check_Fault_Type, summary="Error occured while performing outbound connectivity check in the cluster")
        diagnoser_output.append("An exception has occured while performing the outbound connectivity check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete", storage_space_available


def check_msi_certificate(corev1_api_instance):

    global diagnoser_output

    try:

        # Initializing msi certificate as not present
        msi_cert_present = False

        # Going thorugh all the secrets in azure-arc
        all_secrets_azurearc = corev1_api_instance.list_namespaced_secret(namespace="azure-arc")

        for secrets in all_secrets_azurearc.items:

            # If name of secret is azure-identity-certificate then we stop there
            if(secrets.metadata.name == consts.MSI_Certificate_Secret_Name):
                msi_cert_present = True

        # Checking if msi cerificate is present or not
        if not msi_cert_present:
            print("Error: Unable to pull MSI certificate. Please ensure to meet the following network requirements 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#meet-network-requirements'. \n")
            diagnoser_output.append("Error: Unable to pull MSI certificate. Please ensure to meet the following network requirements 'https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?tabs=azure-cli#meet-network-requirements'. \n")
            return "Failed"

        return "Passed"

    except Exception as e:
        logger.warning("An exception has occured while performing the msi certificate check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.MSI_Cert_Check_Fault_Type, summary="Error occured while trying to pull MSI certificate")
        diagnoser_output.append("An exception has occured while performing the msi certificate check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete"


def check_cluster_security_policy(corev1_api_instance, helm_client_location):

    global diagnoser_output

    try:
        # Intializing the kap_pod_present and cluster_connect_feature variable as False
        kap_pod_present = False
        cluster_connect_feature = False

        # CMD command to get helm values in azure arc and converting it to json format
        command = [helm_client_location, "get", "values", "azure-arc", "-o", "json"]

        # Using Popen to execute the helm get values command and fetching the output
        response_helm_values_get = Popen(command, stdout=PIPE, stderr=PIPE)
        output_helm_values_get, error_helm_get_values = response_helm_values_get.communicate()

        if response_helm_values_get.returncode != 0:
            if ('forbidden' in error_helm_get_values.decode("ascii") or 'timed out waiting for the condition' in error_helm_get_values.decode("ascii")):
                telemetry.set_exception(exception=error_helm_get_values.decode("ascii"), fault_type=consts.Get_Helm_Values_Failed,
                                        summary='Error while doing helm get values azure-arc')

        # Converting output obtained in json format and fetching the clusterconnect-agent feature
        helm_values_json = json.loads(output_helm_values_get)
        cluster_connect_feature = helm_values_json["systemDefaultValues"]["clusterconnect-agent"]["enabled"]

        # To retrieve all of the arc agent pods that are presesnt in the Cluster
        arc_agents_pod_list = corev1_api_instance.list_namespaced_pod(namespace="azure-arc")

        # Traversing thorugh all agents and checking if the Kube aad proxy pod is present or not
        for each_agent_pod in arc_agents_pod_list.items:

            if(each_agent_pod.metadata.name.startswith("kube-aad-proxy")):
                kap_pod_present = True
                break

        # Checking if any pod security policy is set
        if(cluster_connect_feature is True and kap_pod_present is False):
            print("Error: Unable to create Kube-aad-proxy deployment there might be a security policy or security context constraint (SCC) present which is preventing the deployment of kube-aad-proxy as it doesn't have admin privileges.\n ")
            diagnoser_output.append("Error: Unable to create Kube-aad-proxy deployment there might be a security policy present which is preventing the deployment of kube-aad-proxy as it doesn't have admin privileges.\n ")
            return "Failed"
        return "Passed"

    except Exception as e:
        logger.warning("An exception has occured while trying to performing KAP cluster security policy check in the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Cluster_Security_Policy_Check_Fault_Type, summary="Error occured while performing cluster security policy check")
        diagnoser_output.append("An exception has occured while trying to performing KAP cluster security policy check in the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete"


def check_kap_cert(corev1_api_instance):

    global diagnoser_output

    try:
        # Initialize the kap_cert_present as False
        kap_cert_present = False
        kap_pod_status = ""

        # To retrieve all of the arc agent pods that are presesnt in the Cluster
        arc_agents_pod_list = corev1_api_instance.list_namespaced_pod(namespace="azure-arc")

        # Traversing thorugh all agents and checking if the Kube aad proxy pod is in containercreating state
        for each_agent_pod in arc_agents_pod_list.items:

            if each_agent_pod.metadata.name.startswith("kube-aad-proxy") and each_agent_pod.status.phase == "ContainerCreating":
                kap_pod_status = "ContainerCreating"
                break

        # Going thorugh all the secrets in azure-arc
        all_secrets_azurearc = corev1_api_instance.list_namespaced_secret(namespace="azure-arc")

        for secrets in all_secrets_azurearc.items:

            # If name of secret is kube-aad-proxy-certificate then we stop there
            if(secrets.metadata.name == consts.KAP_Certificate_Secret_Name):
                kap_cert_present = True

        if not kap_cert_present and kap_pod_status == "ContainerCreating":
            print("Error: Unable to pull Kube aad proxy certificate.\n")
            diagnoser_output.append("Error: Unable to pull Kube aad proxy certificate.\n")
            return "Failed"

        return "Passed"

    except Exception as e:
        logger.warning("An exception has occured while performing kube aad proxy certificate check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.KAP_Cert_Check_Fault_Type, summary="Error occured while trying to pull kap cert certificate")
        diagnoser_output.append("An exception has occured while performing kube aad proxy certificate check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete"


def check_msi_expiry(connected_cluster):

    global diagnoser_output

    try:
        # Fetch the expiry time of the msi certificate
        Expiry_date = str(connected_cluster.managed_identity_certificate_expiration_time)

        # Fetch the current time and format it same as msi certificate
        Current_date_temp = datetime.datetime.now().utcnow().replace(microsecond=0, tzinfo=datetime.timezone.utc).isoformat()
        Current_date = Current_date_temp.replace('T', ' ')

        # Check if expiry date is lesser than current time
        if (Expiry_date < Current_date):
            print("Error: Your MSI certificate has expired. To resolve this issue you can delete the cluster and reconnect it to azure arc.\n")
            diagnoser_output.append("Error: Your MSI certificate has expired. To resolve this issue you can delete the cluster and reconnect it to azure arc.\n")
            return "Failed"

        return "Passed"

    except Exception as e:
        logger.warning("An exception has occured while performing msi expiry check on the cluster. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.MSI_Cert_Expiry_Check_Fault_Type, summary="Error occured while trying to perform the MSI cert expiry check")
        diagnoser_output.append("An exception has occured while performing msi expiry check on the cluster. Exception: {}".format(str(e)) + "\n")

    return "Incomplete"


def describe_stuck_agent_log(filepath_with_timestamp, corev1_api_instance, agent_pod_name, storage_space_available):

    try:
        if storage_space_available:
            describe_stuck_agent_path = os.path.join(filepath_with_timestamp, 'Describe_Stuck_Agents')
            try:
                os.mkdir(describe_stuck_agent_path)
            except FileExistsError:
                pass
            api_response = corev1_api_instance.read_namespaced_pod(name=agent_pod_name, namespace='azure-arc')
            stuck_agent_pod_path = os.path.join(describe_stuck_agent_path, agent_pod_name + '.txt')

            with open(stuck_agent_pod_path, 'w+') as stuck_agent_log:
                stuck_agent_log.write(str(api_response))

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)
        else:
            logger.warning("An exception has occured while storing stuck agent logs in the user local machine. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Describe_Stuck_Agents_Fault_Type, summary="Error occured while storing the stuck agents description")
            diagnoser_output.append("An exception has occured while storing stuck agent logs in the user local machine. Exception: {}".format(str(e)) + "\n")

    except Exception as e:
            logger.warning("An exception has occured while storing stuck agent logs in the user local machine. Exception: {}".format(str(e)) + "\n")
            telemetry.set_exception(exception=e, fault_type=consts.Describe_Stuck_Agents_Fault_Type, summary="Error occured while storing the stuck agents description")
            diagnoser_output.append("An exception has occured while storing stuck agent logs in the user local machine. Exception: {}".format(str(e)) + "\n")

    return storage_space_available


def cli_output_logger(filepath_with_timestamp, storage_space_available, flag):

    global diagnoser_output

    try:

        if storage_space_available:

            cli_output_logger_path = os.path.join(filepath_with_timestamp, "Diagnoser_Results.txt")

            if len(diagnoser_output) > 0:
                with open(cli_output_logger_path, 'w+') as cli_output_writer:
                    for output in diagnoser_output:
                        cli_output_writer.write(output + "\n")
                    if flag == 0:
                        cli_output_writer.write("Process terminated externally.\n")
            elif flag:
                with open(cli_output_logger_path, 'w+') as cli_output_writer:
                    cli_output_writer.write("Diagnoser did not find any issues with the cluster.\n")
            else:
                with open(cli_output_logger_path, 'w+') as cli_output_writer:
                    cli_output_writer.write("Process terminated externally.\n")

        return "Passed"

    except OSError as e:
        if "[Errno 28]" in str(e):
            storage_space_available = False
            telemetry.set_exception(exception=e, fault_type=consts.No_Storage_Space_Available_Fault_Type, summary="No space left on device")
            shutil.rmtree(filepath_with_timestamp, ignore_errors=False, onerror=None)

    except Exception as e:
        logger.warning("An exception has occured while trying to store the diagnoser results. Exception: {}".format(str(e)) + "\n")
        telemetry.set_exception(exception=e, fault_type=consts.Diagnoser_Result_Fault_Type, summary="Error while storing the diagnoser results")

    return "Failed"
