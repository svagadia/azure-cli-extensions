# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class WorkflowProvisioningState(str, Enum):
    """The workflow provisioning state.
    """

    not_specified = "NotSpecified"
    accepted = "Accepted"
    running = "Running"
    ready = "Ready"
    creating = "Creating"
    created = "Created"
    deleting = "Deleting"
    deleted = "Deleted"
    canceled = "Canceled"
    failed = "Failed"
    succeeded = "Succeeded"
    moving = "Moving"
    updating = "Updating"
    registering = "Registering"
    registered = "Registered"
    unregistering = "Unregistering"
    unregistered = "Unregistered"
    completed = "Completed"

class WorkflowState(str, Enum):
    """The workflow state.
    """

    not_specified = "NotSpecified"
    completed = "Completed"
    enabled = "Enabled"
    disabled = "Disabled"
    deleted = "Deleted"
    suspended = "Suspended"

class SkuName(str, Enum):
    """The sku name.
    """

    not_specified = "NotSpecified"
    free = "Free"
    shared = "Shared"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"

class ParameterType(str, Enum):
    """The parameter type.
    """

    not_specified = "NotSpecified"
    string = "String"
    secure_string = "SecureString"
    int = "Int"
    float = "Float"
    bool = "Bool"
    array = "Array"
    object = "Object"
    secure_object = "SecureObject"

class DaysOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"

class DayOfWeek(str, Enum):
    """The day of the week.
    """

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"

class WorkflowTriggerProvisioningState(str, Enum):
    """The workflow trigger provisioning state.
    """

    not_specified = "NotSpecified"
    accepted = "Accepted"
    running = "Running"
    ready = "Ready"
    creating = "Creating"
    created = "Created"
    deleting = "Deleting"
    deleted = "Deleted"
    canceled = "Canceled"
    failed = "Failed"
    succeeded = "Succeeded"
    moving = "Moving"
    updating = "Updating"
    registering = "Registering"
    registered = "Registered"
    unregistering = "Unregistering"
    unregistered = "Unregistered"
    completed = "Completed"

class WorkflowStatus(str, Enum):
    """The workflow status.
    """

    not_specified = "NotSpecified"
    paused = "Paused"
    running = "Running"
    waiting = "Waiting"
    succeeded = "Succeeded"
    skipped = "Skipped"
    suspended = "Suspended"
    cancelled = "Cancelled"
    failed = "Failed"
    faulted = "Faulted"
    timed_out = "TimedOut"
    aborted = "Aborted"
    ignored = "Ignored"

class RecurrenceFrequency(str, Enum):
    """The recurrence frequency.
    """

    not_specified = "NotSpecified"
    second = "Second"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"

class IntegrationAccountSkuName(str, Enum):
    """The integration account sku name.
    """

    not_specified = "NotSpecified"
    free = "Free"
    basic = "Basic"
    standard = "Standard"

class IntegrationServiceEnvironmentAccessEndpointType(str, Enum):
    """The integration service environment access endpoint type.
    """

    not_specified = "NotSpecified"
    external = "External"
    internal = "Internal"

class IntegrationServiceEnvironmentSkuName(str, Enum):
    """The integration service environment sku name.
    """

    not_specified = "NotSpecified"
    premium = "Premium"
    developer = "Developer"

class EventLevel(str, Enum):
    """The event level.
    """

    log_always = "LogAlways"
    critical = "Critical"
    error = "Error"
    warning = "Warning"
    informational = "Informational"
    verbose = "Verbose"

class TrackingRecordType(str, Enum):
    """The tracking record type.
    """

    not_specified = "NotSpecified"
    custom = "Custom"
    as2_message = "AS2Message"
    as2_mdn = "AS2MDN"
    x12_interchange = "X12Interchange"
    x12_functional_group = "X12FunctionalGroup"
    x12_transaction_set = "X12TransactionSet"
    x12_interchange_acknowledgment = "X12InterchangeAcknowledgment"
    x12_functional_group_acknowledgment = "X12FunctionalGroupAcknowledgment"
    x12_transaction_set_acknowledgment = "X12TransactionSetAcknowledgment"
    edifact_interchange = "EdifactInterchange"
    edifact_functional_group = "EdifactFunctionalGroup"
    edifact_transaction_set = "EdifactTransactionSet"
    edifact_interchange_acknowledgment = "EdifactInterchangeAcknowledgment"
    edifact_functional_group_acknowledgment = "EdifactFunctionalGroupAcknowledgment"
    edifact_transaction_set_acknowledgment = "EdifactTransactionSetAcknowledgment"

class SchemaType(str, Enum):
    """The schema type.
    """

    not_specified = "NotSpecified"
    xml = "Xml"

class MapType(str, Enum):
    """The map type.
    """

    not_specified = "NotSpecified"
    xslt = "Xslt"
    xslt20 = "Xslt20"
    xslt30 = "Xslt30"
    liquid = "Liquid"

class PartnerType(str, Enum):
    """The partner type.
    """

    not_specified = "NotSpecified"
    b2_b = "B2B"

class X12DateFormat(str, Enum):
    """The x12 date format.
    """

    not_specified = "NotSpecified"
    ccyymmdd = "CCYYMMDD"
    yymmdd = "YYMMDD"

class X12TimeFormat(str, Enum):
    """The x12 time format.
    """

    not_specified = "NotSpecified"
    hhmm = "HHMM"
    hhmmss = "HHMMSS"
    hhmms_sdd = "HHMMSSdd"
    hhmms_sd = "HHMMSSd"

class TrailingSeparatorPolicy(str, Enum):
    """The trailing separator policy.
    """

    not_specified = "NotSpecified"
    not_allowed = "NotAllowed"
    optional = "Optional"
    mandatory = "Mandatory"

class SegmentTerminatorSuffix(str, Enum):
    """The segment terminator suffix.
    """

    not_specified = "NotSpecified"
    none = "None"
    cr = "CR"
    lf = "LF"
    crlf = "CRLF"

class EdifactDecimalIndicator(str, Enum):
    """The edifact decimal indicator.
    """

    not_specified = "NotSpecified"
    comma = "Comma"
    decimal = "Decimal"

class AgreementType(str, Enum):
    """The agreement type.
    """

    not_specified = "NotSpecified"
    as2 = "AS2"
    x12 = "X12"
    edifact = "Edifact"

class HashingAlgorithm(str, Enum):
    """The signing or hashing algorithm.
    """

    not_specified = "NotSpecified"
    none = "None"
    md5 = "MD5"
    sha1 = "SHA1"
    sha2256 = "SHA2256"
    sha2384 = "SHA2384"
    sha2512 = "SHA2512"

class EncryptionAlgorithm(str, Enum):
    """The encryption algorithm.
    """

    not_specified = "NotSpecified"
    none = "None"
    des3 = "DES3"
    rc2 = "RC2"
    aes128 = "AES128"
    aes192 = "AES192"
    aes256 = "AES256"

class SigningAlgorithm(str, Enum):
    """The signing or hashing algorithm.
    """

    not_specified = "NotSpecified"
    default = "Default"
    sha1 = "SHA1"
    sha2256 = "SHA2256"
    sha2384 = "SHA2384"
    sha2512 = "SHA2512"

class X12CharacterSet(str, Enum):
    """The X12 character set.
    """

    not_specified = "NotSpecified"
    basic = "Basic"
    extended = "Extended"
    utf8 = "UTF8"

class UsageIndicator(str, Enum):
    """The usage indicator.
    """

    not_specified = "NotSpecified"
    test = "Test"
    information = "Information"
    production = "Production"

class MessageFilterType(str, Enum):
    """The message filter type.
    """

    not_specified = "NotSpecified"
    include = "Include"
    exclude = "Exclude"

class EdifactCharacterSet(str, Enum):
    """The edifact character set.
    """

    not_specified = "NotSpecified"
    unob = "UNOB"
    unoa = "UNOA"
    unoc = "UNOC"
    unod = "UNOD"
    unoe = "UNOE"
    unof = "UNOF"
    unog = "UNOG"
    unoh = "UNOH"
    unoi = "UNOI"
    unoj = "UNOJ"
    unok = "UNOK"
    unox = "UNOX"
    unoy = "UNOY"
    keca = "KECA"

class IntegrationServiceEnvironmentSkuScaleType(str, Enum):
    """The integration service environment sku scale type.
    """

    manual = "Manual"
    automatic = "Automatic"
    none = "None"

class IntegrationServiceEnvironmentNetworkEndPointAccessibilityState(str, Enum):
    """The integration service environment network endpoint accessibility state.
    """

    not_specified = "NotSpecified"
    unknown = "Unknown"
    available = "Available"
    not_available = "NotAvailable"

class IntegrationServiceEnvironmentNetworkDependencyCategoryType(str, Enum):
    """The integration service environment network dependency category type.
    """

    not_specified = "NotSpecified"
    azure_storage = "AzureStorage"
    azure_management = "AzureManagement"
    azure_active_directory = "AzureActiveDirectory"
    ssl_certificate_verification = "SSLCertificateVerification"
    diagnostic_logs_and_metrics = "DiagnosticLogsAndMetrics"
    integration_service_environment_connectors = "IntegrationServiceEnvironmentConnectors"
    redis_cache = "RedisCache"
    access_endpoints = "AccessEndpoints"
    recovery_service = "RecoveryService"
    sql = "SQL"
    regional_service = "RegionalService"

class ErrorResponseCode(str, Enum):
    """The error response code.
    """

    not_specified = "NotSpecified"
    integration_service_environment_not_found = "IntegrationServiceEnvironmentNotFound"
    internal_server_error = "InternalServerError"
    invalid_operation_id = "InvalidOperationId"

class ApiType(str, Enum):

    not_specified = "NotSpecified"
    rest = "Rest"
    soap = "Soap"

class WsdlImportMethod(str, Enum):
    """The WSDL import method.
    """

    not_specified = "NotSpecified"
    soap_to_rest = "SoapToRest"
    soap_pass_through = "SoapPassThrough"

class ApiDeploymentParameterVisibility(str, Enum):
    """The Api deployment parameter visibility.
    """

    not_specified = "NotSpecified"
    default = "Default"
    internal = "Internal"

class ApiTier(str, Enum):
    """The Api tier.
    """

    not_specified = "NotSpecified"
    enterprise = "Enterprise"
    standard = "Standard"
    premium = "Premium"

class SwaggerSchemaType(str, Enum):
    """The swagger schema type.
    """

    string = "String"
    number = "Number"
    integer = "Integer"
    boolean = "Boolean"
    array = "Array"
    file = "File"
    object = "Object"
    null = "Null"

class StatusAnnotation(str, Enum):
    """The status annotation.
    """

    not_specified = "NotSpecified"
    preview = "Preview"
    production = "Production"

class KeyType(str, Enum):
    """The key type.
    """

    not_specified = "NotSpecified"
    primary = "Primary"
    secondary = "Secondary"

class TrackEventsOperationOptions(str, Enum):
    """The track events operation options.
    """

    none = "None"
    disable_source_info_enrich = "DisableSourceInfoEnrich"

class IntegrationServiceEnvironmentNetworkDependencyHealthState(str, Enum):
    """The integration service environment network dependency health state.
    """

    not_specified = "NotSpecified"
    healthy = "Healthy"
    unhealthy = "Unhealthy"
    unknown = "Unknown"

class AzureAsyncOperationState(str, Enum):
    """The Azure async operation state.
    """

    failed = "Failed"
    succeeded = "Succeeded"
    pending = "Pending"
    canceled = "Canceled"
