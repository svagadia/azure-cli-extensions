# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg, rg_2, rg_3):
    pass


# EXAMPLE: /IntegrationAccounts/put/Create or update an integration account
@try_manual
def step__integrationaccounts_put_create_or_update_an_integration_account(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account create '
             '--location "westus" '
             '--sku name="Standard" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /Workflows/put/Create or update a workflow
@try_manual
def step__workflows_put_create_or_update_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow create '
             '--resource-group "{rg}" '
             '--location "brazilsouth" '
             '--properties-definition "{{\\"$schema\\":\\"https://schema.management.azure.com/providers/Microsoft.Logic'
             '/schemas/2016-06-01/workflowdefinition.json#\\",\\"actions\\":{{\\"Find_pet_by_ID\\":{{\\"type\\":\\"ApiC'
             'onnection\\",\\"inputs\\":{{\\"path\\":\\"/pet/@{{encodeURIComponent(\'1\')}}\\",\\"method\\":\\"get\\",'
             '\\"host\\":{{\\"connection\\":{{\\"name\\":\\"@parameters(\'$connections\')[\'test-custom-connector\'][\''
             'connectionId\']\\"}}}}}},\\"runAfter\\":{{}}}}}},\\"contentVersion\\":\\"1.0.0.0\\",\\"outputs\\":{{}},\\'
             '"parameters\\":{{\\"$connections\\":{{\\"type\\":\\"Object\\",\\"defaultValue\\":{{}}}}}},\\"triggers\\":'
             '{{\\"manual\\":{{\\"type\\":\\"Request\\",\\"inputs\\":{{\\"schema\\":{{}}}},\\"kind\\":\\"Http\\"}}}}}}"'
             ' '
             '--properties-integration-account id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Micro'
             'soft.Logic/integrationAccounts/{test-integration-account}" '
             '--properties-parameters "{{\\"$connections\\":{{\\"value\\":{{\\"test-custom-connector\\":{{\\"connection'
             'Id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Web/connections/test-cu'
             'stom-connector\\",\\"connectionName\\":\\"test-custom-connector\\",\\"id\\":\\"/subscriptions/{subscripti'
             'on_id}/providers/Microsoft.Web/locations/brazilsouth/managedApis/test-custom-connector\\"}}}}}}}}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccountMaps/put/Create or update a map
@try_manual
def step__integrationaccountmaps_put_create_or_update_a_map(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-map create '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--location "westus" '
             '--properties-content "<?xml version=\\"1.0\\" encoding=\\"UTF-16\\"?>\\r\\n<xsl:stylesheet xmlns:xsl=\\"h'
             'ttp://www.w3.org/1999/XSL/Transform\\" xmlns:msxsl=\\"urn:schemas-microsoft-com:xslt\\" xmlns:var=\\"http'
             '://schemas.microsoft.com/BizTalk/2003/var\\" exclude-result-prefixes=\\"msxsl var s0 userCSharp\\" versio'
             'n=\\"1.0\\" xmlns:ns0=\\"http://BizTalk_Server_Project4.StringFunctoidsDestinationSchema\\" xmlns:s0=\\"h'
             'ttp://BizTalk_Server_Project4.StringFunctoidsSourceSchema\\" xmlns:userCSharp=\\"http://schemas.microsoft'
             '.com/BizTalk/2003/userCSharp\\">\\r\\n  <xsl:import href=\\"http://btsfunctoids.blob.core.windows.net/fun'
             'ctoids/functoids.xslt\\" />\\r\\n  <xsl:output omit-xml-declaration=\\"yes\\" method=\\"xml\\" version=\\'
             '"1.0\\" />\\r\\n  <xsl:template match=\\"/\\">\\r\\n    <xsl:apply-templates select=\\"/s0:Root\\" />\\r'
             '\\n  </xsl:template>\\r\\n  <xsl:template match=\\"/s0:Root\\">\\r\\n    <xsl:variable name=\\"var:v1\\" '
             'select=\\"userCSharp:StringFind(string(StringFindSource/text()) , &quot;SearchString&quot;)\\" />\\r\\n  '
             '  <xsl:variable name=\\"var:v2\\" select=\\"userCSharp:StringLeft(string(StringLeftSource/text()) , &quot'
             ';2&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v3\\" select=\\"userCSharp:StringRight(string(StringRi'
             'ghtSource/text()) , &quot;2&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v4\\" select=\\"userCSharp:St'
             'ringUpperCase(string(UppercaseSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v5\\" select=\\"us'
             'erCSharp:StringLowerCase(string(LowercaseSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v6\\" s'
             'elect=\\"userCSharp:StringSize(string(SizeSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v7\\" '
             'select=\\"userCSharp:StringSubstring(string(StringExtractSource/text()) , &quot;0&quot; , &quot;2&quot;)'
             '\\" />\\r\\n    <xsl:variable name=\\"var:v8\\" select=\\"userCSharp:StringConcat(string(StringConcatSour'
             'ce/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v9\\" select=\\"userCSharp:StringTrimLeft(string(Str'
             'ingLeftTrimSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v10\\" select=\\"userCSharp:StringTri'
             'mRight(string(StringRightTrimSource/text()))\\" />\\r\\n    <ns0:Root>\\r\\n      <StringFindDestination>'
             '\\r\\n        <xsl:value-of select=\\"$var:v1\\" />\\r\\n      </StringFindDestination>\\r\\n      <Strin'
             'gLeftDestination>\\r\\n        <xsl:value-of select=\\"$var:v2\\" />\\r\\n      </StringLeftDestination>'
             '\\r\\n      <StringRightDestination>\\r\\n        <xsl:value-of select=\\"$var:v3\\" />\\r\\n      </Stri'
             'ngRightDestination>\\r\\n      <UppercaseDestination>\\r\\n        <xsl:value-of select=\\"$var:v4\\" />'
             '\\r\\n      </UppercaseDestination>\\r\\n      <LowercaseDestination>\\r\\n        <xsl:value-of select='
             '\\"$var:v5\\" />\\r\\n      </LowercaseDestination>\\r\\n      <SizeDestination>\\r\\n        <xsl:value-'
             'of select=\\"$var:v6\\" />\\r\\n      </SizeDestination>\\r\\n      <StringExtractDestination>\\r\\n     '
             '   <xsl:value-of select=\\"$var:v7\\" />\\r\\n      </StringExtractDestination>\\r\\n      <StringConcatD'
             'estination>\\r\\n        <xsl:value-of select=\\"$var:v8\\" />\\r\\n      </StringConcatDestination>\\r\\'
             'n      <StringLeftTrimDestination>\\r\\n        <xsl:value-of select=\\"$var:v9\\" />\\r\\n      </String'
             'LeftTrimDestination>\\r\\n      <StringRightTrimDestination>\\r\\n        <xsl:value-of select=\\"$var:v1'
             '0\\" />\\r\\n      </StringRightTrimDestination>\\r\\n    </ns0:Root>\\r\\n  </xsl:template>\\r\\n</xsl:s'
             'tylesheet>" '
             '--properties-content-type "application/xml" '
             '--properties-map-type "Xslt" '
             '--properties-metadata "{{}}" '
             '--map-name "testMap" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/put/Create or update an integration service environment
@try_manual
def step__integrationserviceenvironments_put_create_or_update_an_integration_service_environment(test, rg, rg_2,
                                                                                                 rg_3):
    test.cmd('az logic integration-service-environment create '
             '--location "brazilsouth" '
             '--properties "{{\\"networkConfiguration\\":{{\\"accessEndpoint\\":{{\\"type\\":\\"Internal\\"}},\\"subnet'
             's\\":[{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/vi'
             'rtualNetworks/{vn}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg'
             '_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{s'
             'ubscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"'
             '}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtu'
             'alNetworks/{vn}/subnets/default\\"}}]}}}}" '
             '--sku name="Premium" capacity=2 '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountSchemas/put/Create or update schema
@try_manual
def step__integrationaccountschemas_put_create_or_update_schema(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-schema create '
             '--location "westus" '
             '--properties-content "<?xml version=\\"1.0\\" encoding=\\"utf-16\\"?>\\r\\n<xs:schema xmlns:b=\\"http://s'
             'chemas.microsoft.com/BizTalk/2003\\" xmlns=\\"http://Inbound_EDI.OrderFile\\" targetNamespace=\\"http://I'
             'nbound_EDI.OrderFile\\" xmlns:xs=\\"http://www.w3.org/2001/XMLSchema\\">\\r\\n  <xs:annotation>\\r\\n    '
             '<xs:appinfo>\\r\\n      <b:schemaInfo default_pad_char=\\" \\" count_positions_by_byte=\\"false\\" parser'
             '_optimization=\\"speed\\" lookahead_depth=\\"3\\" suppress_empty_nodes=\\"false\\" generate_empty_nodes='
             '\\"true\\" allow_early_termination=\\"false\\" early_terminate_optional_fields=\\"false\\" allow_message_'
             'breakup_of_infix_root=\\"false\\" compile_parse_tables=\\"false\\" standard=\\"Flat File\\" root_referenc'
             'e=\\"OrderFile\\" />\\r\\n      <schemaEditorExtension:schemaInfo namespaceAlias=\\"b\\" extensionClass='
             '\\"Microsoft.BizTalk.FlatFileExtension.FlatFileExtension\\" standardName=\\"Flat File\\" xmlns:schemaEdit'
             'orExtension=\\"http://schemas.microsoft.com/BizTalk/2003/SchemaEditorExtensions\\" />\\r\\n    </xs:appin'
             'fo>\\r\\n  </xs:annotation>\\r\\n  <xs:element name=\\"OrderFile\\">\\r\\n    <xs:annotation>\\r\\n      '
             '<xs:appinfo>\\r\\n        <b:recordInfo structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"tr'
             'ue\\" suppress_trailing_delimiters=\\"false\\" sequence_number=\\"1\\" />\\r\\n      </xs:appinfo>\\r\\n '
             '   </xs:annotation>\\r\\n    <xs:complexType>\\r\\n      <xs:sequence>\\r\\n        <xs:annotation>\\r\\n'
             '          <xs:appinfo>\\r\\n            <b:groupInfo sequence_number=\\"0\\" />\\r\\n          </xs:appin'
             'fo>\\r\\n        </xs:annotation>\\r\\n        <xs:element name=\\"Order\\">\\r\\n          <xs:annotatio'
             'n>\\r\\n            <xs:appinfo>\\r\\n              <b:recordInfo sequence_number=\\"1\\" structure=\\"de'
             'limited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" child_de'
             'limiter_type=\\"hex\\" child_delimiter=\\"0x0D 0x0A\\" child_order=\\"infix\\" />\\r\\n            </xs:a'
             'ppinfo>\\r\\n          </xs:annotation>\\r\\n          <xs:complexType>\\r\\n            <xs:sequence>\\r'
             '\\n              <xs:annotation>\\r\\n                <xs:appinfo>\\r\\n                  <b:groupInfo se'
             'quence_number=\\"0\\" />\\r\\n                </xs:appinfo>\\r\\n              </xs:annotation>\\r\\n    '
             '          <xs:element name=\\"Header\\">\\r\\n                <xs:annotation>\\r\\n                  <xs:'
             'appinfo>\\r\\n                    <b:recordInfo sequence_number=\\"1\\" structure=\\"delimited\\" preserv'
             'e_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" child_delimiter_type=\\"ch'
             'ar\\" child_delimiter=\\"|\\" child_order=\\"infix\\" tag_name=\\"HDR|\\" />\\r\\n                  </xs:'
             'appinfo>\\r\\n                </xs:annotation>\\r\\n                <xs:complexType>\\r\\n               '
             '   <xs:sequence>\\r\\n                    <xs:annotation>\\r\\n                      <xs:appinfo>\\r\\n  '
             '                      <b:groupInfo sequence_number=\\"0\\" />\\r\\n                      </xs:appinfo>\\r'
             '\\n                    </xs:annotation>\\r\\n                    <xs:element name=\\"PODate\\" type=\\"xs'
             ':string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n   '
             '                       <b:fieldInfo sequence_number=\\"1\\" justification=\\"left\\" />\\r\\n            '
             '            </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:eleme'
             'nt>\\r\\n                    <xs:element name=\\"PONumber\\" type=\\"xs:string\\">\\r\\n                 '
             '     <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInf'
             'o justification=\\"left\\" sequence_number=\\"2\\" />\\r\\n                        </xs:appinfo>\\r\\n   '
             '                   </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:e'
             'lement name=\\"CustomerID\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n      '
             '                  <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"3\\" justif'
             'ication=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotati'
             'on>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"CustomerContactNa'
             'me\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:a'
             'ppinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"4\\" justification=\\"left\\" />\\'
             'r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n              '
             '      </xs:element>\\r\\n                    <xs:element name=\\"CustomerContactPhone\\" type=\\"xs:strin'
             'g\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n         '
             '                 <b:fieldInfo sequence_number=\\"5\\" justification=\\"left\\" />\\r\\n                  '
             '      </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r'
             '\\n                  </xs:sequence>\\r\\n                </xs:complexType>\\r\\n              </xs:elemen'
             't>\\r\\n              <xs:element minOccurs=\\"1\\" maxOccurs=\\"unbounded\\" name=\\"LineItems\\">\\r\\n'
             '                <xs:annotation>\\r\\n                  <xs:appinfo>\\r\\n                    <b:recordInf'
             'o sequence_number=\\"2\\" structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress'
             '_trailing_delimiters=\\"false\\" child_delimiter_type=\\"char\\" child_delimiter=\\"|\\" child_order=\\"i'
             'nfix\\" tag_name=\\"DTL|\\" />\\r\\n                  </xs:appinfo>\\r\\n                </xs:annotation>'
             '\\r\\n                <xs:complexType>\\r\\n                  <xs:sequence>\\r\\n                    <xs:'
             'annotation>\\r\\n                      <xs:appinfo>\\r\\n                        <b:groupInfo sequence_nu'
             'mber=\\"0\\" />\\r\\n                      </xs:appinfo>\\r\\n                    </xs:annotation>\\r\\n '
             '                   <xs:element name=\\"PONumber\\" type=\\"xs:string\\">\\r\\n                      <xs:a'
             'nnotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence'
             '_number=\\"1\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n             '
             '         </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element nam'
             'e=\\"ItemOrdered\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n               '
             '         <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"2\\" justification='
             '\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\'
             'n                    </xs:element>\\r\\n                    <xs:element name=\\"Quantity\\" type=\\"xs:st'
             'ring\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n      '
             '                    <b:fieldInfo sequence_number=\\"3\\" justification=\\"left\\" />\\r\\n               '
             '         </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>'
             '\\r\\n                    <xs:element name=\\"UOM\\" type=\\"xs:string\\">\\r\\n                      <xs'
             ':annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequen'
             'ce_number=\\"4\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n           '
             '           </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element n'
             'ame=\\"Price\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                   '
             '     <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"5\\" justification=\\"le'
             'ft\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n    '
             '                </xs:element>\\r\\n                    <xs:element name=\\"ExtendedPrice\\" type=\\"xs:st'
             'ring\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n      '
             '                    <b:fieldInfo sequence_number=\\"6\\" justification=\\"left\\" />\\r\\n               '
             '         </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>'
             '\\r\\n                    <xs:element name=\\"Description\\" type=\\"xs:string\\">\\r\\n                 '
             '     <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInf'
             'o sequence_number=\\"7\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n   '
             '                   </xs:annotation>\\r\\n                    </xs:element>\\r\\n                  </xs:se'
             'quence>\\r\\n                </xs:complexType>\\r\\n              </xs:element>\\r\\n            </xs:seq'
             'uence>\\r\\n          </xs:complexType>\\r\\n        </xs:element>\\r\\n      </xs:sequence>\\r\\n    </x'
             's:complexType>\\r\\n  </xs:element>\\r\\n</xs:schema>" '
             '--properties-content-type "application/xml" '
             '--properties-metadata "{{}}" '
             '--properties-schema-type "Xml" '
             '--tags integrationAccountSchemaName="IntegrationAccountSchema8120" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}" '
             '--schema-name "testSchema"',
             checks=[])


# EXAMPLE: /IntegrationAccountSessions/put/Create or update an integration account session
@try_manual
def step__integrationaccountsessions_put_create_or_update_an_integration_account_session(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-session create '
             '--integration-account-name "{IntegrationAccounts_3}" '
             '--resource-group "{rg_3}" '
             '--properties-content "{{\\"controlNumber\\":\\"1234\\",\\"controlNumberChangedTime\\":\\"2017-02-21T22:30'
             ':11.9923759Z\\"}}" '
             '--session-name "testsession123-ICN"',
             checks=[])


# EXAMPLE: /IntegrationAccountPartners/put/Create or update a partner
@try_manual
def step__integrationaccountpartners_put_create_or_update_a_partner(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-partner create '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--location "westus" '
             '--properties-content "{{\\"b2b\\":{{\\"businessIdentities\\":[{{\\"qualifier\\":\\"AA\\",\\"value\\":\\"Z'
             'Z\\"}}]}}}}" '
             '--properties-metadata "{{}}" '
             '--properties-partner-type "B2B" '
             '--partner-name "testPartner" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAgreements/put/Create or update an agreement
@try_manual
def step__integrationaccountagreements_put_create_or_update_an_agreement(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-agreement create '
             '--location "westus" '
             '--properties-agreement-type "AS2" '
             '--properties-content "{{\\"aS2\\":{{\\"receiveAgreement\\":{{\\"protocolSettings\\":{{\\"acknowledgementC'
             'onnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"sup'
             'portHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"envelopeSettings\\":{{\\"autogenerat'
             'eFileName\\":true,\\"fileNameTemplate\\":\\"Test\\",\\"messageContentType\\":\\"text/plain\\",\\"suspendM'
             'essageOnFileNameGenerationError\\":true,\\"transmitFileNameInMimeHeader\\":true}},\\"errorSettings\\":{{'
             '\\"resendIfMDNNotReceived\\":true,\\"suspendDuplicateMessage\\":true}},\\"mdnSettings\\":{{\\"disposition'
             'NotificationTo\\":\\"http://tempuri.org\\",\\"mdnText\\":\\"Sample\\",\\"micHashingAlgorithm\\":\\"SHA1\\'
             '",\\"needMDN\\":true,\\"receiptDeliveryUrl\\":\\"http://tempuri.org\\",\\"sendInboundMdnToMessageBox\\":t'
             'rue,\\"sendMDNAsynchronously\\":true,\\"signMDN\\":true,\\"signOutboundMdnIfOptional\\":true}},\\"message'
             'ConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"su'
             'pportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"securitySettings\\":{{\\"enableNRRF'
             'orInboundDecodedMessages\\":true,\\"enableNRRForInboundEncodedMessages\\":true,\\"enableNRRForInboundMDN'
             '\\":true,\\"enableNRRForOutboundDecodedMessages\\":true,\\"enableNRRForOutboundEncodedMessages\\":true,\\'
             '"enableNRRForOutboundMDN\\":true,\\"overrideGroupSigningCertificate\\":false}},\\"validationSettings\\":{'
             '{\\"checkCertificateRevocationListOnReceive\\":true,\\"checkCertificateRevocationListOnSend\\":true,\\"ch'
             'eckDuplicateMessage\\":true,\\"compressMessage\\":true,\\"encryptMessage\\":false,\\"encryptionAlgorithm'
             '\\":\\"AES128\\",\\"interchangeDuplicatesValidityDays\\":100,\\"overrideMessageProperties\\":true,\\"sign'
             'Message\\":false}}}},\\"receiverBusinessIdentity\\":{{\\"qualifier\\":\\"ZZ\\",\\"value\\":\\"ZZ\\"}},\\"'
             'senderBusinessIdentity\\":{{\\"qualifier\\":\\"AA\\",\\"value\\":\\"AA\\"}}}},\\"sendAgreement\\":{{\\"pr'
             'otocolSettings\\":{{\\"acknowledgementConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\'
             '"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},'
             '\\"envelopeSettings\\":{{\\"autogenerateFileName\\":true,\\"fileNameTemplate\\":\\"Test\\",\\"messageCont'
             'entType\\":\\"text/plain\\",\\"suspendMessageOnFileNameGenerationError\\":true,\\"transmitFileNameInMimeH'
             'eader\\":true}},\\"errorSettings\\":{{\\"resendIfMDNNotReceived\\":true,\\"suspendDuplicateMessage\\":tru'
             'e}},\\"mdnSettings\\":{{\\"dispositionNotificationTo\\":\\"http://tempuri.org\\",\\"mdnText\\":\\"Sample'
             '\\",\\"micHashingAlgorithm\\":\\"SHA1\\",\\"needMDN\\":true,\\"receiptDeliveryUrl\\":\\"http://tempuri.or'
             'g\\",\\"sendInboundMdnToMessageBox\\":true,\\"sendMDNAsynchronously\\":true,\\"signMDN\\":true,\\"signOut'
             'boundMdnIfOptional\\":true}},\\"messageConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,'
             '\\"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}'
             '},\\"securitySettings\\":{{\\"enableNRRForInboundDecodedMessages\\":true,\\"enableNRRForInboundEncodedMes'
             'sages\\":true,\\"enableNRRForInboundMDN\\":true,\\"enableNRRForOutboundDecodedMessages\\":true,\\"enableN'
             'RRForOutboundEncodedMessages\\":true,\\"enableNRRForOutboundMDN\\":true,\\"overrideGroupSigningCertificat'
             'e\\":false}},\\"validationSettings\\":{{\\"checkCertificateRevocationListOnReceive\\":true,\\"checkCertif'
             'icateRevocationListOnSend\\":true,\\"checkDuplicateMessage\\":true,\\"compressMessage\\":true,\\"encryptM'
             'essage\\":false,\\"encryptionAlgorithm\\":\\"AES128\\",\\"interchangeDuplicatesValidityDays\\":100,\\"ove'
             'rrideMessageProperties\\":true,\\"signMessage\\":false}}}},\\"receiverBusinessIdentity\\":{{\\"qualifier'
             '\\":\\"AA\\",\\"value\\":\\"AA\\"}},\\"senderBusinessIdentity\\":{{\\"qualifier\\":\\"ZZ\\",\\"value\\":'
             '\\"ZZ\\"}}}}}}}}" '
             '--properties-guest-identity qualifier="AA" value="AA" '
             '--properties-guest-partner "GuestPartner" '
             '--properties-host-identity qualifier="ZZ" value="ZZ" '
             '--properties-host-partner "HostPartner" '
             '--properties-metadata "{{}}" '
             '--tags IntegrationAccountAgreement="<IntegrationAccountAgreementName>" '
             '--agreement-name "testAgreement" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountCertificates/put/Create or update a certificate
@try_manual
def step__integrationaccountcertificates_put_create_or_update_a_certificate(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-certificate create '
             '--location "brazilsouth" '
             '--properties-key "{{\\"keyName\\":\\"<keyName>\\",\\"keyVault\\":{{\\"id\\":\\"/subscriptions/{subscripti'
             'on_id}/resourcegroups/{rg_2}/providers/microsoft.keyvault/vaults/<keyVaultName>\\"}},\\"keyVersion\\":\\"'
             '87d9764197604449b9b8eb7bd8710868\\"}}" '
             '--properties-public-certificate "<publicCertificateValue>" '
             '--certificate-name "testCertificate" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAssemblies/put/Create or update an account assembly
@try_manual
def step__integrationaccountassemblies_put_create_or_update_an_account_assembly(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-assembly create '
             '--location "westus" '
             '--properties assembly-name="System.IdentityModel.Tokens.Jwt" content="Base64 encoded Assembly Content" me'
             'tadata={{}} '
             '--assembly-artifact-name "testAssembly" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountBatchConfigurations/put/Create or update a batch configuration
@try_manual
def step__integrationaccountbatchconfigurations_put_create_or_update_a_batch_configuration(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-batch-configuration create '
             '--location "westus" '
             '--properties "{{\\"batchGroupName\\":\\"DEFAULT\\",\\"releaseCriteria\\":{{\\"batchSize\\":234567,\\"mess'
             'ageCount\\":10,\\"recurrence\\":{{\\"frequency\\":\\"Minute\\",\\"interval\\":1,\\"startTime\\":\\"2017-0'
             '3-24T11:43:00\\",\\"timeZone\\":\\"India Standard Time\\"}}}}}}" '
             '--batch-configuration-name "testBatchConfiguration" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRepetitionsRequestHistories/get/Get a repetition request history
@try_manual
def step__workflowrunactionrepetitionsrequesthistories_get_get_a_repetition_request_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-repetition-request-history show '
             '--action-name "HTTP_Webhook" '
             '--repetition-name "000001" '
             '--request-history-name "08586611142732800686" '
             '--resource-group "{rg}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRequestHistories/get/Get a request history
@try_manual
def step__workflowrunactionrequesthistories_get_get_a_request_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-request-history show '
             '--action-name "HTTP_Webhook" '
             '--request-history-name "08586611142732800686" '
             '--resource-group "{rg}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionScopeRepetitions/get/Get a scoped repetition
@try_manual
def step__workflowrunactionscoperepetitions_get_get_a_scoped_repetition(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-scope-repetition show '
             '--action-name "for_each" '
             '--repetition-name "000000" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRepetitions/get/Get a repetition
@try_manual
def step__workflowrunactionrepetitions_get_get_a_repetition(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-repetition show '
             '--action-name "testAction" '
             '--repetition-name "000001" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountBatchConfigurations/get/Get a batch configuration
@try_manual
def step__integrationaccountbatchconfigurations_get_get_a_batch_configuration(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-batch-configuration show '
             '--batch-configuration-name "testBatchConfiguration" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentManagedApis/put/Gets the integration service environment managed Apis
@try_manual
def step__integrationserviceenvironmentmanagedapis_put_gets_the_integration_service_environment_managed_apis(test, rg,
                                                                                                             rg_2,
                                                                                                             rg_3):
    test.cmd('az logic integration-service-environment-managed-api put '
             '--api-name "servicebus" '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountAssemblies/get/Get an integration account assembly
@try_manual
def step__integrationaccountassemblies_get_get_an_integration_account_assembly(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-assembly show '
             '--assembly-artifact-name "testAssembly" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentNetworkHealth/get/Gets the integration service environment network health
@try_manual
def step__integrationserviceenvironmentnetworkhealth_get_gets_the_integration_service_environment_network_health(test,
                                                                                                                 rg,
                                                                                                                 rg_2,
                                                                                                                 rg_3):
    test.cmd('az logic integration-service-environment-network-health show '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountCertificates/get/Get certificate by name
@try_manual
def step__integrationaccountcertificates_get_get_certificate_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-certificate show '
             '--certificate-name "testCertificate" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggerHistories/get/Get a workflow trigger history
@try_manual
def step__workflowtriggerhistories_get_get_a_workflow_trigger_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger-history show '
             '--history-name "08586676746934337772206998657CU22" '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTriggerName" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAgreements/get/Get agreement by name
@try_manual
def step__integrationaccountagreements_get_get_agreement_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-agreement show '
             '--agreement-name "testAgreement" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountPartners/get/Get partner by name
@try_manual
def step__integrationaccountpartners_get_get_partner_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-partner show '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--partner-name "testPartner" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountSessions/get/Get an integration account session
@try_manual
def step__integrationaccountsessions_get_get_an_integration_account_session(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-session show '
             '--integration-account-name "{IntegrationAccounts_3}" '
             '--resource-group "{rg_3}" '
             '--session-name "testsession123-ICN"',
             checks=[])


# EXAMPLE: /IntegrationAccountSchemas/get/Get schema by name
@try_manual
def step__integrationaccountschemas_get_get_schema_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-schema show '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}" '
             '--schema-name "testSchema"',
             checks=[])


# EXAMPLE: /WorkflowRunOperations/get/Get a run operation
@try_manual
def step__workflowrunoperations_get_get_a_run_operation(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-operation show '
             '--operation-id "ebdcbbde-c4db-43ec-987c-fd0f7726f43b" '
             '--resource-group "{rg_2}" '
             '--run-name "08586774142730039209110422528" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/get/Get integration service environment by name
@try_manual
def step__integrationserviceenvironments_get_get_integration_service_environment_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-service-environment show '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/get/Get trigger schema
@try_manual
def step__workflowtriggers_get_get_trigger_schema(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger show '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTrigger" '
             '--workflow-name "{Workflows_4}"',
             checks=[])


# EXAMPLE: /WorkflowRunActions/get/Get a workflow run action
@try_manual
def step__workflowrunactions_get_get_a_workflow_run_action(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action show '
             '--action-name "HTTP" '
             '--resource-group "{rg}" '
             '--run-name "08586676746934337772206998657CU22" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccountMaps/get/Get map by name
@try_manual
def step__integrationaccountmaps_get_get_map_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-map show '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--map-name "testMap" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/get/Get a workflow trigger
@try_manual
def step__workflowtriggers_get_get_a_workflow_trigger(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger show '
             '--resource-group "{rg}" '
             '--trigger-name "manual" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowVersions/get/Get a workflow version
@try_manual
def step__workflowversions_get_get_a_workflow_version(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-version show '
             '--resource-group "{rg}" '
             '--version-id "08586676824806722526" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/get/Get integration account by name
@try_manual
def step__integrationaccounts_get_get_integration_account_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account show '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowRuns/get/Get a run for a workflow
@try_manual
def step__workflowruns_get_get_a_run_for_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run show '
             '--resource-group "{rg}" '
             '--run-name "08586676746934337772206998657CU22" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /Workflows/get/Get a workflow
@try_manual
def step__workflows_get_get_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow show '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRepetitionsRequestHistories/get/List repetition request history
@try_manual
def step__workflowrunactionrepetitionsrequesthistories_get_list_repetition_request_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-repetition-request-history list '
             '--action-name "HTTP_Webhook" '
             '--repetition-name "000001" '
             '--resource-group "{rg}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentManagedApiOperations/get/Gets the integration service environment managed Apis
@try_manual
def step__integrationserviceenvironmentmanagedapioperations_get_gets_the_integration_service_environment_managed_apis(test,
                                                                                                                       rg,
                                                                                                                       rg_2,
                                                                                                                       rg_3):
    test.cmd('az logic integration-service-environment-managed-api-operation list '
             '--api-name "servicebus" '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRequestHistories/get/List a request history
@try_manual
def step__workflowrunactionrequesthistories_get_list_a_request_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-request-history list '
             '--action-name "HTTP_Webhook" '
             '--resource-group "{rg}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRunActionScopeRepetitions/get/List the scoped repetitions
@try_manual
def step__workflowrunactionscoperepetitions_get_list_the_scoped_repetitions(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-scope-repetition list '
             '--action-name "for_each" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentManagedApis/get/Gets the integration service environment managed Apis
@try_manual
def step__integrationserviceenvironmentmanagedapis_get_gets_the_integration_service_environment_managed_apis(test, rg,
                                                                                                             rg_2,
                                                                                                             rg_3):
    test.cmd('az logic integration-service-environment-managed-api list '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /WorkflowRunActionRepetitions/get/List repetitions
@try_manual
def step__workflowrunactionrepetitions_get_list_repetitions(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-repetition list '
             '--action-name "testAction" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentSkus/get/List integration service environment skus
@try_manual
def step__integrationserviceenvironmentskus_get_list_integration_service_environment_skus(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-service-environment-sku list '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountBatchConfigurations/get/List batch configurations
@try_manual
def step__integrationaccountbatchconfigurations_get_list_batch_configurations(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-batch-configuration list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggerHistories/get/List a workflow trigger history
@try_manual
def step__workflowtriggerhistories_get_list_a_workflow_trigger_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger-history list '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTriggerName" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /IntegrationAccountCertificates/get/Get certificates by integration account name
@try_manual
def step__integrationaccountcertificates_get_get_certificates_by_integration_account_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-certificate list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAssemblies/get/List integration account assemblies
@try_manual
def step__integrationaccountassemblies_get_list_integration_account_assemblies(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-assembly list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAgreements/get/Get agreements by integration account name
@try_manual
def step__integrationaccountagreements_get_get_agreements_by_integration_account_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-agreement list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountPartners/get/Get partners by integration account name
@try_manual
def step__integrationaccountpartners_get_get_partners_by_integration_account_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-partner list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountSessions/get/Get a list of integration account sessions
@try_manual
def step__integrationaccountsessions_get_get_a_list_of_integration_account_sessions(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-session list '
             '--integration-account-name "{IntegrationAccounts_3}" '
             '--resource-group "{rg_3}"',
             checks=[])


# EXAMPLE: /IntegrationAccountSchemas/get/Get schemas by integration account name
@try_manual
def step__integrationaccountschemas_get_get_schemas_by_integration_account_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-schema list '
             '--integration-account-name "{IntegrationAccounts_4}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountMaps/get/Get maps by integration account name
@try_manual
def step__integrationaccountmaps_get_get_maps_by_integration_account_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-map list '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowRunActions/get/List a workflow run actions
@try_manual
def step__workflowrunactions_get_list_a_workflow_run_actions(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action list '
             '--resource-group "{rg}" '
             '--run-name "08586676746934337772206998657CU22" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowVersions/get/List a workflows versions
@try_manual
def step__workflowversions_get_list_a_workflows_versions(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-version list '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/get/List workflow triggers
@try_manual
def step__workflowtriggers_get_list_workflow_triggers(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger list '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRuns/get/List workflow runs
@try_manual
def step__workflowruns_get_list_workflow_runs(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run list '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/get/List integration service environments by resource group name
@try_manual
def step__integrationserviceenvironments_get_list_integration_service_environments_by_resource_group_name(test, rg,
                                                                                                          rg_2, rg_3):
    test.cmd('az logic integration-service-environment list '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/get/List integration accounts by resource group name
@try_manual
def step__integrationaccounts_get_list_integration_accounts_by_resource_group_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account list '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /Workflows/get/List all workflows in a resource group
@try_manual
def step__workflows_get_list_all_workflows_in_a_resource_group(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/get/List integration service environments by subscription
@try_manual
def step__integrationserviceenvironments_get_list_integration_service_environments_by_subscription(test, rg, rg_2,
                                                                                                   rg_3):
    test.cmd('az logic integration-service-environment list',
             checks=[])


# EXAMPLE: /IntegrationAccounts/get/List integration accounts by subscription
@try_manual
def step__integrationaccounts_get_list_integration_accounts_by_subscription(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account list',
             checks=[])


# EXAMPLE: /Workflows/get/List all workflows in a subscription
@try_manual
def step__workflows_get_list_all_workflows_in_a_subscription(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow list',
             checks=[])


# EXAMPLE: /WorkflowRunActionRepetitions/post/List expression traces for a repetition
@try_manual
def step__workflowrunactionrepetitions_post_list_expression_traces_for_a_repetition(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action-repetition list-expression-trace '
             '--action-name "testAction" '
             '--repetition-name "000001" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAssemblies/post/Get the callback url for an integration account assembly
@try_manual
def step__integrationaccountassemblies_post_get_the_callback_url_for_an_integration_account_assembly(test, rg, rg_2,
                                                                                                     rg_3):
    test.cmd('az logic integration-account-assembly list-content-callback-url '
             '--assembly-artifact-name "testAssembly" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAgreements/post/Get the content callback url
@try_manual
def step__integrationaccountagreements_post_get_the_content_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-agreement list-content-callback-url '
             '--agreement-name "testAgreement" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--not-after "2018-04-19T16:00:00Z" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountPartners/post/Get the content callback url
@try_manual
def step__integrationaccountpartners_post_get_the_content_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-partner list-content-callback-url '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--not-after "2018-04-19T16:00:00Z" '
             '--partner-name "testPartner" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountSchemas/post/Get the content callback url
@try_manual
def step__integrationaccountschemas_post_get_the_content_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-schema list-content-callback-url '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--not-after "2018-04-19T16:00:00Z" '
             '--resource-group "{rg_2}" '
             '--schema-name "testSchema"',
             checks=[])


# EXAMPLE: /WorkflowVersionTriggers/post/Get the callback url for a trigger of a workflow version
@try_manual
def step__workflowversiontriggers_post_get_the_callback_url_for_a_trigger_of_a_workflow_version(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-version-trigger list-callback-url '
             '--key-type "Primary" '
             '--not-after "2017-03-05T08:00:00Z" '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTriggerName" '
             '--version-id "testWorkflowVersionId" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentManagedApis/get/Gets the integration service environment managed Apis
@try_manual
def step__integrationserviceenvironmentmanagedapis_get_gets_the_integration_service_environment_managed_apis(test, rg,
                                                                                                             rg_2,
                                                                                                             rg_3):
    test.cmd('az logic integration-service-environment-managed-api list '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountMaps/post/Get the content callback url
@try_manual
def step__integrationaccountmaps_post_get_the_content_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-map list-content-callback-url '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--not-after "2018-04-19T16:00:00Z" '
             '--map-name "testMap" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowRunActions/post/List expression traces
@try_manual
def step__workflowrunactions_post_list_expression_traces(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run-action list-expression-trace '
             '--action-name "testAction" '
             '--resource-group "{rg_2}" '
             '--run-name "08586776228332053161046300351" '
             '--workflow-name "{Workflows_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggerHistories/post/Resubmit a workflow run based on the trigger history
@try_manual
def step__workflowtriggerhistories_post_resubmit_a_workflow_run_based_on_the_trigger_history(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger-history resubmit '
             '--history-name "testHistoryName" '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTriggerName" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/post/Restarts an integration service environment
@try_manual
def step__integrationserviceenvironments_post_restarts_an_integration_service_environment(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-service-environment restart '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/post/Regenerate access key
@try_manual
def step__integrationaccounts_post_regenerate_access_key(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account regenerate-access-key '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/post/Get the callback URL for a trigger
@try_manual
def step__workflowtriggers_post_get_the_callback_url_for_a_trigger(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger list-callback-url '
             '--resource-group "{rg}" '
             '--trigger-name "manual" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/post/Log a tracked event
@try_manual
def step__integrationaccounts_post_log_a_tracked_event(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account log-tracking-event '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--events "[{{\\"error\\":{{\\"code\\":\\"NotFound\\",\\"message\\":\\"Some error occurred\\"}},\\"eventLe'
             'vel\\":\\"Informational\\",\\"eventTime\\":\\"2016-08-05T01:54:49.505567Z\\",\\"record\\":{{\\"agreementP'
             'roperties\\":{{\\"agreementName\\":\\"testAgreement\\",\\"as2From\\":\\"testas2from\\",\\"as2To\\":\\"tes'
             'tas2to\\",\\"receiverPartnerName\\":\\"testPartner2\\",\\"senderPartnerName\\":\\"testPartner1\\"}},\\"me'
             'ssageProperties\\":{{\\"IsMessageEncrypted\\":false,\\"IsMessageSigned\\":false,\\"correlationMessageId\\'
             '":\\"Unique message identifier\\",\\"direction\\":\\"Receive\\",\\"dispositionType\\":\\"received-success'
             '\\",\\"fileName\\":\\"test\\",\\"isMdnExpected\\":true,\\"isMessageCompressed\\":false,\\"isMessageFailed'
             '\\":false,\\"isNrrEnabled\\":true,\\"mdnType\\":\\"Async\\",\\"messageId\\":\\"12345\\"}}}},\\"recordType'
             '\\":\\"AS2Message\\"}}]" '
             '--source-type "Microsoft.Logic/workflows" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/patch/Patch an integration service environment
@try_manual
def step__integrationserviceenvironments_patch_patch_an_integration_service_environment(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-service-environment update '
             '--sku name="Developer" capacity=0 '
             '--tags tag1="value1" '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/post/Get Integration Account callback URL
@try_manual
def step__integrationaccounts_post_get_integration_account_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account list-key-vault-key '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-vault id="subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testResourceGroup/provi'
             'ders/Microsoft.KeyVault/vaults/testKeyVault" '
             '--skip-token "testSkipToken" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/post/List IntegrationAccount callback URL
@try_manual
def step__integrationaccounts_post_list_integrationaccount_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account list-callback-url '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--key-type "Primary" '
             '--not-after "2017-03-05T08:00:00Z" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/post/Set trigger state
@try_manual
def step__workflowtriggers_post_set_trigger_state(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger set-state '
             '--resource-group "{rg_2}" '
             '--source "{{\\"id\\":\\"subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/sourceResGroup/'
             'providers/Microsoft.Logic/workflows/sourceWorkflow/triggers/sourceTrigger\\"}}" '
             '--trigger-name "testTrigger" '
             '--workflow-name "{Workflows_4}"',
             checks=[])


# EXAMPLE: /Workflows/post/Validate a workflow
@try_manual
def step__workflows_post_validate_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow validate-by-location '
             '--location "brazilsouth" '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/post/Reset trigger
@try_manual
def step__workflowtriggers_post_reset_trigger(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger reset '
             '--resource-group "{rg_2}" '
             '--trigger-name "testTrigger" '
             '--workflow-name "{Workflows_4}"',
             checks=[])


# EXAMPLE: /Workflows/post/Generate an upgraded definition
@try_manual
def step__workflows_post_generate_an_upgraded_definition(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow generate-upgraded-definition '
             '--target-schema-version "2016-06-01" '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowTriggers/post/Run a workflow trigger
@try_manual
def step__workflowtriggers_post_run_a_workflow_trigger(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-trigger run '
             '--resource-group "{rg}" '
             '--trigger-name "manual" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /WorkflowRuns/post/Cancel a workflow run
@try_manual
def step__workflowruns_post_cancel_a_workflow_run(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow-run cancel '
             '--resource-group "{rg}" '
             '--run-name "08586676746934337772206998657CU22" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /Workflows/post/Regenerate the callback URL access key for request triggers
@try_manual
def step__workflows_post_regenerate_the_callback_url_access_key_for_request_triggers(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow regenerate-access-key '
             '--key-type "Primary" '
             '--resource-group "{rg_2}" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/patch/Patch an integration account
@try_manual
def step__integrationaccounts_patch_patch_an_integration_account(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account update '
             '--location "westus" '
             '--sku name="Standard" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /Workflows/post/Get callback url
@try_manual
def step__workflows_post_get_callback_url(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow list-callback-url '
             '--key-type "Primary" '
             '--not-after "2018-04-19T16:00:00Z" '
             '--resource-group "{rg_2}" '
             '--workflow-name "{Workflows_4}"',
             checks=[])


# EXAMPLE: /Workflows/post/Get the swagger for a workflow
@try_manual
def step__workflows_post_get_the_swagger_for_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow list-swagger '
             '--resource-group "{rg_2}" '
             '--workflow-name "{Workflows_3}"',
             checks=[])


# EXAMPLE: /Workflows/post/Validate a workflow
@try_manual
def step__workflows_post_validate_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow validate-by-location '
             '--location "brazilsouth" '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /Workflows/post/Disable a workflow
@try_manual
def step__workflows_post_disable_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow disable '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /Workflows/post/Enable a workflow
@try_manual
def step__workflows_post_enable_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow enable '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /Workflows/post/Move a workflow
@try_manual
def step__workflows_post_move_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow move '
             '--resource-group "{rg_2}" '
             '--workflow-name "{Workflows_4}"',
             checks=[])


# EXAMPLE: /Workflows/patch/Patch a workflow
@try_manual
def step__workflows_patch_patch_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow update '
             '--resource-group "{rg}" '
             '--location "brazilsouth" '
             '--properties-definition "{{\\"$schema\\":\\"https://schema.management.azure.com/providers/Microsoft.Logic'
             '/schemas/2016-06-01/workflowdefinition.json#\\",\\"actions\\":{{\\"Find_pet_by_ID\\":{{\\"type\\":\\"ApiC'
             'onnection\\",\\"inputs\\":{{\\"path\\":\\"/pet/@{{encodeURIComponent(\'1\')}}\\",\\"method\\":\\"get\\",'
             '\\"host\\":{{\\"connection\\":{{\\"name\\":\\"@parameters(\'$connections\')[\'test-custom-connector\'][\''
             'connectionId\']\\"}}}}}},\\"runAfter\\":{{}}}}}},\\"contentVersion\\":\\"1.0.0.0\\",\\"outputs\\":{{}},\\'
             '"parameters\\":{{\\"$connections\\":{{\\"type\\":\\"Object\\",\\"defaultValue\\":{{}}}}}},\\"triggers\\":'
             '{{\\"manual\\":{{\\"type\\":\\"Request\\",\\"inputs\\":{{\\"schema\\":{{}}}},\\"kind\\":\\"Http\\"}}}}}}"'
             ' '
             '--properties-integration-account id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Micro'
             'soft.Logic/integrationAccounts/{test-integration-account}" '
             '--properties-parameters "{{\\"$connections\\":{{\\"value\\":{{\\"test-custom-connector\\":{{\\"connection'
             'Id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Web/connections/test-cu'
             'stom-connector\\",\\"connectionName\\":\\"test-custom-connector\\",\\"id\\":\\"/subscriptions/{subscripti'
             'on_id}/providers/Microsoft.Web/locations/brazilsouth/managedApis/test-custom-connector\\"}}}}}}}}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccountBatchConfigurations/delete/Delete a batch configuration
@try_manual
def step__integrationaccountbatchconfigurations_delete_delete_a_batch_configuration(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-batch-configuration delete '
             '--batch-configuration-name "testBatchConfiguration" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironmentManagedApis/delete/Deletes the integration service environment managed Apis
@try_manual
def step__integrationserviceenvironmentmanagedapis_delete_deletes_the_integration_service_environment_managed_apis(test,
                                                                                                                    rg,
                                                                                                                    rg_2,
                                                                                                                    rg_3):
    test.cmd('az logic integration-service-environment-managed-api delete '
             '--api-name "servicebus" '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountAssemblies/delete/Delete an integration account assembly
@try_manual
def step__integrationaccountassemblies_delete_delete_an_integration_account_assembly(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-assembly delete '
             '--assembly-artifact-name "testAssembly" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountCertificates/delete/Delete a certificate
@try_manual
def step__integrationaccountcertificates_delete_delete_a_certificate(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-certificate delete '
             '--certificate-name "testCertificate" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountAgreements/delete/Delete an agreement
@try_manual
def step__integrationaccountagreements_delete_delete_an_agreement(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-agreement delete '
             '--agreement-name "testAgreement" '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountPartners/delete/Delete a partner
@try_manual
def step__integrationaccountpartners_delete_delete_a_partner(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-partner delete '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--partner-name "testPartner" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /IntegrationAccountSessions/delete/Delete an integration account session
@try_manual
def step__integrationaccountsessions_delete_delete_an_integration_account_session(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-session delete '
             '--integration-account-name "{IntegrationAccounts_3}" '
             '--resource-group "{rg_3}" '
             '--session-name "testsession123-ICN"',
             checks=[])


# EXAMPLE: /IntegrationAccountSchemas/delete/Delete a schema by name
@try_manual
def step__integrationaccountschemas_delete_delete_a_schema_by_name(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-schema delete '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}" '
             '--schema-name "testSchema"',
             checks=[])


# EXAMPLE: /IntegrationServiceEnvironments/delete/Delete an integration account
@try_manual
def step__integrationserviceenvironments_delete_delete_an_integration_account(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-service-environment delete '
             '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
             '--resource-group "testResourceGroup"',
             checks=[])


# EXAMPLE: /IntegrationAccountMaps/delete/Delete a map
@try_manual
def step__integrationaccountmaps_delete_delete_a_map(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account-map delete '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--map-name "testMap" '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /Workflows/delete/Delete a workflow
@try_manual
def step__workflows_delete_delete_a_workflow(test, rg, rg_2, rg_3):
    test.cmd('az logic workflow delete '
             '--resource-group "{rg}" '
             '--workflow-name "{test-workflow}"',
             checks=[])


# EXAMPLE: /IntegrationAccounts/delete/Delete an integration account
@try_manual
def step__integrationaccounts_delete_delete_an_integration_account(test, rg, rg_2, rg_3):
    test.cmd('az logic integration-account delete '
             '--integration-account-name "{IntegrationAccounts_2}" '
             '--resource-group "{rg_2}"',
             checks=[])


@try_manual
def cleanup(test, rg, rg_2, rg_3):
    pass


class LogicManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestlogic_test-resource-group'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestlogic_testResourceGroup'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestlogic_testrg123'[:7], key='rg_3', parameter_name='rg_3')
    @VirtualNetworkPreparer(name_prefix='clitestlogic_testVNET'[:7], key='vn', resource_group_key='rg_2')
    def test_logic(self, rg, rg_2, rg_3):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'test-integration-account': 'test-integration-account',
            'IntegrationAccounts_2': self.create_random_name(prefix='clitestintegration_accounts'[:7], length=24),
            'IntegrationAccounts_3': 'IntegrationAccounts_3',
            'IntegrationAccounts_4': 'IntegrationAccounts_4',
            'testIntegrationServiceEnvironment': self.create_random_name(prefix='clitestintegration_service_environment'
                                                                         's'[:7], length=24),
            'test-workflow': self.create_random_name(prefix='clitestworkflows'[:7], length=24),
            'Workflows_2': 'Workflows_2',
            'Workflows_3': 'Workflows_3',
            'Workflows_4': 'Workflows_4',
        })

        setup(self, rg, rg_2, rg_3)
        step__integrationaccounts_put_create_or_update_an_integration_account(self, rg, rg_2, rg_3)
        step__workflows_put_create_or_update_a_workflow(self, rg, rg_2, rg_3)
        step__integrationaccountmaps_put_create_or_update_a_map(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_put_create_or_update_an_integration_service_environment(self, rg, rg_2,
                                                                                                     rg_3)
        step__integrationaccountschemas_put_create_or_update_schema(self, rg, rg_2, rg_3)
        step__integrationaccountsessions_put_create_or_update_an_integration_account_session(self, rg, rg_2, rg_3)
        step__integrationaccountpartners_put_create_or_update_a_partner(self, rg, rg_2, rg_3)
        step__integrationaccountagreements_put_create_or_update_an_agreement(self, rg, rg_2, rg_3)
        step__integrationaccountcertificates_put_create_or_update_a_certificate(self, rg, rg_2, rg_3)
        step__integrationaccountassemblies_put_create_or_update_an_account_assembly(self, rg, rg_2, rg_3)
        step__integrationaccountbatchconfigurations_put_create_or_update_a_batch_configuration(self, rg, rg_2, rg_3)
        step__workflowrunactionrepetitionsrequesthistories_get_get_a_repetition_request_history(self, rg, rg_2, rg_3)
        step__workflowrunactionrequesthistories_get_get_a_request_history(self, rg, rg_2, rg_3)
        step__workflowrunactionscoperepetitions_get_get_a_scoped_repetition(self, rg, rg_2, rg_3)
        step__workflowrunactionrepetitions_get_get_a_repetition(self, rg, rg_2, rg_3)
        step__integrationaccountbatchconfigurations_get_get_a_batch_configuration(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentmanagedapis_put_gets_the_integration_service_environment_managed_apis(self,
                                                                                                                 rg,
                                                                                                                 rg_2,
                                                                                                                 rg_3)
        step__integrationaccountassemblies_get_get_an_integration_account_assembly(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentnetworkhealth_get_gets_the_integration_service_environment_network_health(self,
                                                                                                                      rg,
                                                                                                                      rg_2,
                                                                                                                      rg_3)
        step__integrationaccountcertificates_get_get_certificate_by_name(self, rg, rg_2, rg_3)
        step__workflowtriggerhistories_get_get_a_workflow_trigger_history(self, rg, rg_2, rg_3)
        step__integrationaccountagreements_get_get_agreement_by_name(self, rg, rg_2, rg_3)
        step__integrationaccountpartners_get_get_partner_by_name(self, rg, rg_2, rg_3)
        step__integrationaccountsessions_get_get_an_integration_account_session(self, rg, rg_2, rg_3)
        step__integrationaccountschemas_get_get_schema_by_name(self, rg, rg_2, rg_3)
        step__workflowrunoperations_get_get_a_run_operation(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_get_get_integration_service_environment_by_name(self, rg, rg_2, rg_3)
        step__workflowtriggers_get_get_trigger_schema(self, rg, rg_2, rg_3)
        step__workflowrunactions_get_get_a_workflow_run_action(self, rg, rg_2, rg_3)
        step__integrationaccountmaps_get_get_map_by_name(self, rg, rg_2, rg_3)
        step__workflowtriggers_get_get_a_workflow_trigger(self, rg, rg_2, rg_3)
        step__workflowversions_get_get_a_workflow_version(self, rg, rg_2, rg_3)
        step__integrationaccounts_get_get_integration_account_by_name(self, rg, rg_2, rg_3)
        step__workflowruns_get_get_a_run_for_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_get_get_a_workflow(self, rg, rg_2, rg_3)
        step__workflowrunactionrepetitionsrequesthistories_get_list_repetition_request_history(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentmanagedapioperations_get_gets_the_integration_service_environment_managed_apis(self,
                                                                                                                           rg,
                                                                                                                           rg_2,
                                                                                                                           rg_3)
        step__workflowrunactionrequesthistories_get_list_a_request_history(self, rg, rg_2, rg_3)
        step__workflowrunactionscoperepetitions_get_list_the_scoped_repetitions(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentmanagedapis_get_gets_the_integration_service_environment_managed_apis(self,
                                                                                                                 rg,
                                                                                                                 rg_2,
                                                                                                                 rg_3)
        step__workflowrunactionrepetitions_get_list_repetitions(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentskus_get_list_integration_service_environment_skus(self, rg, rg_2, rg_3)
        step__integrationaccountbatchconfigurations_get_list_batch_configurations(self, rg, rg_2, rg_3)
        step__workflowtriggerhistories_get_list_a_workflow_trigger_history(self, rg, rg_2, rg_3)
        step__integrationaccountcertificates_get_get_certificates_by_integration_account_name(self, rg, rg_2, rg_3)
        step__integrationaccountassemblies_get_list_integration_account_assemblies(self, rg, rg_2, rg_3)
        step__integrationaccountagreements_get_get_agreements_by_integration_account_name(self, rg, rg_2, rg_3)
        step__integrationaccountpartners_get_get_partners_by_integration_account_name(self, rg, rg_2, rg_3)
        step__integrationaccountsessions_get_get_a_list_of_integration_account_sessions(self, rg, rg_2, rg_3)
        step__integrationaccountschemas_get_get_schemas_by_integration_account_name(self, rg, rg_2, rg_3)
        step__integrationaccountmaps_get_get_maps_by_integration_account_name(self, rg, rg_2, rg_3)
        step__workflowrunactions_get_list_a_workflow_run_actions(self, rg, rg_2, rg_3)
        step__workflowversions_get_list_a_workflows_versions(self, rg, rg_2, rg_3)
        step__workflowtriggers_get_list_workflow_triggers(self, rg, rg_2, rg_3)
        step__workflowruns_get_list_workflow_runs(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_get_list_integration_service_environments_by_resource_group_name(self, rg,
                                                                                                               rg_2,
                                                                                                              rg_3)
        step__integrationaccounts_get_list_integration_accounts_by_resource_group_name(self, rg, rg_2, rg_3)
        step__workflows_get_list_all_workflows_in_a_resource_group(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_get_list_integration_service_environments_by_subscription(self, rg, rg_2,
                                                                                                       rg_3)
        step__integrationaccounts_get_list_integration_accounts_by_subscription(self, rg, rg_2, rg_3)
        step__workflows_get_list_all_workflows_in_a_subscription(self, rg, rg_2, rg_3)
        step__workflowrunactionrepetitions_post_list_expression_traces_for_a_repetition(self, rg, rg_2, rg_3)
        step__integrationaccountassemblies_post_get_the_callback_url_for_an_integration_account_assembly(self, rg,
                                                                                                         rg_2, rg_3)
        step__integrationaccountagreements_post_get_the_content_callback_url(self, rg, rg_2, rg_3)
        step__integrationaccountpartners_post_get_the_content_callback_url(self, rg, rg_2, rg_3)
        step__integrationaccountschemas_post_get_the_content_callback_url(self, rg, rg_2, rg_3)
        step__workflowversiontriggers_post_get_the_callback_url_for_a_trigger_of_a_workflow_version(self, rg, rg_2,
                                                                                                    rg_3)
        step__integrationserviceenvironmentmanagedapis_get_gets_the_integration_service_environment_managed_apis(self,
                                                                                                                 rg,
                                                                                                                 rg_2,
                                                                                                                 rg_3)
        step__integrationaccountmaps_post_get_the_content_callback_url(self, rg, rg_2, rg_3)
        step__workflowrunactions_post_list_expression_traces(self, rg, rg_2, rg_3)
        step__workflowtriggerhistories_post_resubmit_a_workflow_run_based_on_the_trigger_history(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_post_restarts_an_integration_service_environment(self, rg, rg_2, rg_3)
        step__integrationaccounts_post_regenerate_access_key(self, rg, rg_2, rg_3)
        step__workflowtriggers_post_get_the_callback_url_for_a_trigger(self, rg, rg_2, rg_3)
        step__integrationaccounts_post_log_a_tracked_event(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_patch_patch_an_integration_service_environment(self, rg, rg_2, rg_3)
        step__integrationaccounts_post_get_integration_account_callback_url(self, rg, rg_2, rg_3)
        step__integrationaccounts_post_list_integrationaccount_callback_url(self, rg, rg_2, rg_3)
        step__workflowtriggers_post_set_trigger_state(self, rg, rg_2, rg_3)
        step__workflows_post_validate_a_workflow(self, rg, rg_2, rg_3)
        step__workflowtriggers_post_reset_trigger(self, rg, rg_2, rg_3)
        step__workflows_post_generate_an_upgraded_definition(self, rg, rg_2, rg_3)
        step__workflowtriggers_post_run_a_workflow_trigger(self, rg, rg_2, rg_3)
        step__workflowruns_post_cancel_a_workflow_run(self, rg, rg_2, rg_3)
        step__workflows_post_regenerate_the_callback_url_access_key_for_request_triggers(self, rg, rg_2, rg_3)
        step__integrationaccounts_patch_patch_an_integration_account(self, rg, rg_2, rg_3)
        step__workflows_post_get_callback_url(self, rg, rg_2, rg_3)
        step__workflows_post_get_the_swagger_for_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_post_validate_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_post_disable_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_post_enable_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_post_move_a_workflow(self, rg, rg_2, rg_3)
        step__workflows_patch_patch_a_workflow(self, rg, rg_2, rg_3)
        step__integrationaccountbatchconfigurations_delete_delete_a_batch_configuration(self, rg, rg_2, rg_3)
        step__integrationserviceenvironmentmanagedapis_delete_deletes_the_integration_service_environment_managed_apis(self,
                                                                                                                        rg,
                                                                                                                        rg_2,
                                                                                                                        rg_3)
        step__integrationaccountassemblies_delete_delete_an_integration_account_assembly(self, rg, rg_2, rg_3)
        step__integrationaccountcertificates_delete_delete_a_certificate(self, rg, rg_2, rg_3)
        step__integrationaccountagreements_delete_delete_an_agreement(self, rg, rg_2, rg_3)
        step__integrationaccountpartners_delete_delete_a_partner(self, rg, rg_2, rg_3)
        step__integrationaccountsessions_delete_delete_an_integration_account_session(self, rg, rg_2, rg_3)
        step__integrationaccountschemas_delete_delete_a_schema_by_name(self, rg, rg_2, rg_3)
        step__integrationserviceenvironments_delete_delete_an_integration_account(self, rg, rg_2, rg_3)
        step__integrationaccountmaps_delete_delete_a_map(self, rg, rg_2, rg_3)
        step__workflows_delete_delete_a_workflow(self, rg, rg_2, rg_3)
        step__integrationaccounts_delete_delete_an_integration_account(self, rg, rg_2, rg_3)
        cleanup(self, rg, rg_2, rg_3)
