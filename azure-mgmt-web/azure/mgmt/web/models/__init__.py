# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .app_service_certificate_py3 import AppServiceCertificate
    from .app_service_certificate_resource_py3 import AppServiceCertificateResource
    from .certificate_details_py3 import CertificateDetails
    from .app_service_certificate_order_py3 import AppServiceCertificateOrder
    from .app_service_certificate_order_patch_resource_py3 import AppServiceCertificateOrderPatchResource
    from .app_service_certificate_patch_resource_py3 import AppServiceCertificatePatchResource
    from .certificate_email_py3 import CertificateEmail
    from .certificate_order_action_py3 import CertificateOrderAction
    from .reissue_certificate_order_request_py3 import ReissueCertificateOrderRequest
    from .renew_certificate_order_request_py3 import RenewCertificateOrderRequest
    from .site_seal_py3 import SiteSeal
    from .site_seal_request_py3 import SiteSealRequest
    from .vnet_route_py3 import VnetRoute
    from .vnet_info_py3 import VnetInfo
    from .vnet_gateway_py3 import VnetGateway
    from .user_py3 import User
    from .snapshot_py3 import Snapshot
    from .resource_metric_availability_py3 import ResourceMetricAvailability
    from .resource_metric_definition_py3 import ResourceMetricDefinition
    from .push_settings_py3 import PushSettings
    from .identifier_py3 import Identifier
    from .hybrid_connection_key_py3 import HybridConnectionKey
    from .hybrid_connection_py3 import HybridConnection
    from .proxy_only_resource_py3 import ProxyOnlyResource
    from .managed_service_identity_py3 import ManagedServiceIdentity
    from .slot_swap_status_py3 import SlotSwapStatus
    from .cloning_info_py3 import CloningInfo
    from .hosting_environment_profile_py3 import HostingEnvironmentProfile
    from .ip_security_restriction_py3 import IpSecurityRestriction
    from .api_definition_info_py3 import ApiDefinitionInfo
    from .cors_settings_py3 import CorsSettings
    from .auto_heal_custom_action_py3 import AutoHealCustomAction
    from .auto_heal_actions_py3 import AutoHealActions
    from .slow_requests_based_trigger_py3 import SlowRequestsBasedTrigger
    from .status_codes_based_trigger_py3 import StatusCodesBasedTrigger
    from .requests_based_trigger_py3 import RequestsBasedTrigger
    from .auto_heal_triggers_py3 import AutoHealTriggers
    from .auto_heal_rules_py3 import AutoHealRules
    from .site_limits_py3 import SiteLimits
    from .ramp_up_rule_py3 import RampUpRule
    from .experiments_py3 import Experiments
    from .virtual_directory_py3 import VirtualDirectory
    from .virtual_application_py3 import VirtualApplication
    from .handler_mapping_py3 import HandlerMapping
    from .site_machine_key_py3 import SiteMachineKey
    from .conn_string_info_py3 import ConnStringInfo
    from .azure_storage_info_value_py3 import AzureStorageInfoValue
    from .name_value_pair_py3 import NameValuePair
    from .site_config_py3 import SiteConfig
    from .host_name_ssl_state_py3 import HostNameSslState
    from .site_py3 import Site
    from .capability_py3 import Capability
    from .sku_capacity_py3 import SkuCapacity
    from .sku_description_py3 import SkuDescription
    from .app_service_plan_py3 import AppServicePlan
    from .resource_py3 import Resource
    from .default_error_response_error_details_item_py3 import DefaultErrorResponseErrorDetailsItem
    from .default_error_response_error_py3 import DefaultErrorResponseError
    from .default_error_response_py3 import DefaultErrorResponse, DefaultErrorResponseException
    from .name_identifier_py3 import NameIdentifier
    from .log_specification_py3 import LogSpecification
    from .metric_availability_py3 import MetricAvailability
    from .dimension_py3 import Dimension
    from .metric_specification_py3 import MetricSpecification
    from .service_specification_py3 import ServiceSpecification
    from .csm_operation_description_properties_py3 import CsmOperationDescriptionProperties
    from .csm_operation_display_py3 import CsmOperationDisplay
    from .csm_operation_description_py3 import CsmOperationDescription
    from .address_py3 import Address
    from .contact_py3 import Contact
    from .host_name_py3 import HostName
    from .domain_purchase_consent_py3 import DomainPurchaseConsent
    from .domain_py3 import Domain
    from .domain_availablility_check_result_py3 import DomainAvailablilityCheckResult
    from .domain_control_center_sso_request_py3 import DomainControlCenterSsoRequest
    from .domain_ownership_identifier_py3 import DomainOwnershipIdentifier
    from .domain_patch_resource_py3 import DomainPatchResource
    from .domain_recommendation_search_parameters_py3 import DomainRecommendationSearchParameters
    from .tld_legal_agreement_py3 import TldLegalAgreement
    from .top_level_domain_py3 import TopLevelDomain
    from .top_level_domain_agreement_option_py3 import TopLevelDomainAgreementOption
    from .certificate_py3 import Certificate
    from .certificate_patch_resource_py3 import CertificatePatchResource
    from .virtual_network_profile_py3 import VirtualNetworkProfile
    from .worker_pool_py3 import WorkerPool
    from .virtual_ip_mapping_py3 import VirtualIPMapping
    from .stamp_capacity_py3 import StampCapacity
    from .network_access_control_entry_py3 import NetworkAccessControlEntry
    from .app_service_environment_py3 import AppServiceEnvironment
    from .localizable_string_py3 import LocalizableString
    from .csm_usage_quota_py3 import CsmUsageQuota
    from .deleted_site_py3 import DeletedSite
    from .error_entity_py3 import ErrorEntity
    from .operation_py3 import Operation
    from .resource_metric_name_py3 import ResourceMetricName
    from .resource_metric_property_py3 import ResourceMetricProperty
    from .resource_metric_value_py3 import ResourceMetricValue
    from .resource_metric_py3 import ResourceMetric
    from .web_app_collection_py3 import WebAppCollection
    from .solution_py3 import Solution
    from .detector_abnormal_time_period_py3 import DetectorAbnormalTimePeriod
    from .abnormal_time_period_py3 import AbnormalTimePeriod
    from .detector_definition_py3 import DetectorDefinition
    from .diagnostic_metric_sample_py3 import DiagnosticMetricSample
    from .diagnostic_metric_set_py3 import DiagnosticMetricSet
    from .data_source_py3 import DataSource
    from .response_meta_data_py3 import ResponseMetaData
    from .analysis_data_py3 import AnalysisData
    from .analysis_definition_py3 import AnalysisDefinition
    from .data_table_response_column_py3 import DataTableResponseColumn
    from .data_table_response_object_py3 import DataTableResponseObject
    from .detector_info_py3 import DetectorInfo
    from .rendering_py3 import Rendering
    from .diagnostic_data_py3 import DiagnosticData
    from .detector_response_py3 import DetectorResponse
    from .diagnostic_analysis_py3 import DiagnosticAnalysis
    from .diagnostic_category_py3 import DiagnosticCategory
    from .diagnostic_detector_response_py3 import DiagnosticDetectorResponse
    from .stack_minor_version_py3 import StackMinorVersion
    from .stack_major_version_py3 import StackMajorVersion
    from .application_stack_py3 import ApplicationStack
    from .recommendation_py3 import Recommendation
    from .recommendation_rule_py3 import RecommendationRule
    from .billing_meter_py3 import BillingMeter
    from .csm_move_resource_envelope_py3 import CsmMoveResourceEnvelope
    from .geo_region_py3 import GeoRegion
    from .hosting_environment_deployment_info_py3 import HostingEnvironmentDeploymentInfo
    from .deployment_locations_py3 import DeploymentLocations
    from .global_csm_sku_description_py3 import GlobalCsmSkuDescription
    from .premier_add_on_offer_py3 import PremierAddOnOffer
    from .resource_name_availability_py3 import ResourceNameAvailability
    from .resource_name_availability_request_py3 import ResourceNameAvailabilityRequest
    from .sku_infos_py3 import SkuInfos
    from .source_control_py3 import SourceControl
    from .validate_request_py3 import ValidateRequest
    from .validate_response_error_py3 import ValidateResponseError
    from .validate_response_py3 import ValidateResponse
    from .vnet_parameters_py3 import VnetParameters
    from .vnet_validation_test_failure_py3 import VnetValidationTestFailure
    from .vnet_validation_failure_details_py3 import VnetValidationFailureDetails
    from .file_system_application_logs_config_py3 import FileSystemApplicationLogsConfig
    from .azure_table_storage_application_logs_config_py3 import AzureTableStorageApplicationLogsConfig
    from .azure_blob_storage_application_logs_config_py3 import AzureBlobStorageApplicationLogsConfig
    from .application_logs_config_py3 import ApplicationLogsConfig
    from .azure_blob_storage_http_logs_config_py3 import AzureBlobStorageHttpLogsConfig
    from .azure_storage_property_dictionary_resource_py3 import AzureStoragePropertyDictionaryResource
    from .database_backup_setting_py3 import DatabaseBackupSetting
    from .backup_item_py3 import BackupItem
    from .backup_schedule_py3 import BackupSchedule
    from .backup_request_py3 import BackupRequest
    from .conn_string_value_type_pair_py3 import ConnStringValueTypePair
    from .connection_string_dictionary_py3 import ConnectionStringDictionary
    from .continuous_web_job_py3 import ContinuousWebJob
    from .csm_publishing_profile_options_py3 import CsmPublishingProfileOptions
    from .csm_slot_entity_py3 import CsmSlotEntity
    from .custom_hostname_analysis_result_py3 import CustomHostnameAnalysisResult
    from .deleted_app_restore_request_py3 import DeletedAppRestoreRequest
    from .deployment_py3 import Deployment
    from .enabled_config_py3 import EnabledConfig
    from .file_system_http_logs_config_py3 import FileSystemHttpLogsConfig
    from .function_envelope_py3 import FunctionEnvelope
    from .function_secrets_py3 import FunctionSecrets
    from .host_name_binding_py3 import HostNameBinding
    from .http_logs_config_py3 import HttpLogsConfig
    from .ms_deploy_py3 import MSDeploy
    from .ms_deploy_log_entry_py3 import MSDeployLogEntry
    from .ms_deploy_log_py3 import MSDeployLog
    from .ms_deploy_status_py3 import MSDeployStatus
    from .migrate_my_sql_request_py3 import MigrateMySqlRequest
    from .migrate_my_sql_status_py3 import MigrateMySqlStatus
    from .relay_service_connection_entity_py3 import RelayServiceConnectionEntity
    from .network_features_py3 import NetworkFeatures
    from .perf_mon_sample_py3 import PerfMonSample
    from .perf_mon_set_py3 import PerfMonSet
    from .perf_mon_response_py3 import PerfMonResponse
    from .premier_add_on_py3 import PremierAddOn
    from .premier_add_on_patch_resource_py3 import PremierAddOnPatchResource
    from .private_access_subnet_py3 import PrivateAccessSubnet
    from .private_access_virtual_network_py3 import PrivateAccessVirtualNetwork
    from .private_access_py3 import PrivateAccess
    from .process_thread_info_py3 import ProcessThreadInfo
    from .process_module_info_py3 import ProcessModuleInfo
    from .process_info_py3 import ProcessInfo
    from .public_certificate_py3 import PublicCertificate
    from .restore_request_py3 import RestoreRequest
    from .site_auth_settings_py3 import SiteAuthSettings
    from .site_cloneability_criterion_py3 import SiteCloneabilityCriterion
    from .site_cloneability_py3 import SiteCloneability
    from .site_config_resource_py3 import SiteConfigResource
    from .site_configuration_snapshot_info_py3 import SiteConfigurationSnapshotInfo
    from .site_extension_info_py3 import SiteExtensionInfo
    from .site_instance_py3 import SiteInstance
    from .site_logs_config_py3 import SiteLogsConfig
    from .site_patch_resource_py3 import SitePatchResource
    from .site_php_error_log_flag_py3 import SitePhpErrorLogFlag
    from .site_source_control_py3 import SiteSourceControl
    from .slot_config_names_resource_py3 import SlotConfigNamesResource
    from .slot_difference_py3 import SlotDifference
    from .snapshot_recovery_source_py3 import SnapshotRecoverySource
    from .snapshot_restore_request_py3 import SnapshotRestoreRequest
    from .storage_migration_options_py3 import StorageMigrationOptions
    from .storage_migration_response_py3 import StorageMigrationResponse
    from .string_dictionary_py3 import StringDictionary
    from .swift_virtual_network_py3 import SwiftVirtualNetwork
    from .triggered_job_run_py3 import TriggeredJobRun
    from .triggered_job_history_py3 import TriggeredJobHistory
    from .triggered_web_job_py3 import TriggeredWebJob
    from .web_job_py3 import WebJob
    from .address_response_py3 import AddressResponse
    from .app_service_environment_resource_py3 import AppServiceEnvironmentResource
    from .app_service_environment_patch_resource_py3 import AppServiceEnvironmentPatchResource
    from .hosting_environment_diagnostics_py3 import HostingEnvironmentDiagnostics
    from .metric_availabilily_py3 import MetricAvailabilily
    from .metric_definition_py3 import MetricDefinition
    from .sku_info_py3 import SkuInfo
    from .usage_py3 import Usage
    from .worker_pool_resource_py3 import WorkerPoolResource
    from .app_service_plan_patch_resource_py3 import AppServicePlanPatchResource
    from .hybrid_connection_limits_py3 import HybridConnectionLimits
except (SyntaxError, ImportError):
    from .app_service_certificate import AppServiceCertificate
    from .app_service_certificate_resource import AppServiceCertificateResource
    from .certificate_details import CertificateDetails
    from .app_service_certificate_order import AppServiceCertificateOrder
    from .app_service_certificate_order_patch_resource import AppServiceCertificateOrderPatchResource
    from .app_service_certificate_patch_resource import AppServiceCertificatePatchResource
    from .certificate_email import CertificateEmail
    from .certificate_order_action import CertificateOrderAction
    from .reissue_certificate_order_request import ReissueCertificateOrderRequest
    from .renew_certificate_order_request import RenewCertificateOrderRequest
    from .site_seal import SiteSeal
    from .site_seal_request import SiteSealRequest
    from .vnet_route import VnetRoute
    from .vnet_info import VnetInfo
    from .vnet_gateway import VnetGateway
    from .user import User
    from .snapshot import Snapshot
    from .resource_metric_availability import ResourceMetricAvailability
    from .resource_metric_definition import ResourceMetricDefinition
    from .push_settings import PushSettings
    from .identifier import Identifier
    from .hybrid_connection_key import HybridConnectionKey
    from .hybrid_connection import HybridConnection
    from .proxy_only_resource import ProxyOnlyResource
    from .managed_service_identity import ManagedServiceIdentity
    from .slot_swap_status import SlotSwapStatus
    from .cloning_info import CloningInfo
    from .hosting_environment_profile import HostingEnvironmentProfile
    from .ip_security_restriction import IpSecurityRestriction
    from .api_definition_info import ApiDefinitionInfo
    from .cors_settings import CorsSettings
    from .auto_heal_custom_action import AutoHealCustomAction
    from .auto_heal_actions import AutoHealActions
    from .slow_requests_based_trigger import SlowRequestsBasedTrigger
    from .status_codes_based_trigger import StatusCodesBasedTrigger
    from .requests_based_trigger import RequestsBasedTrigger
    from .auto_heal_triggers import AutoHealTriggers
    from .auto_heal_rules import AutoHealRules
    from .site_limits import SiteLimits
    from .ramp_up_rule import RampUpRule
    from .experiments import Experiments
    from .virtual_directory import VirtualDirectory
    from .virtual_application import VirtualApplication
    from .handler_mapping import HandlerMapping
    from .site_machine_key import SiteMachineKey
    from .conn_string_info import ConnStringInfo
    from .azure_storage_info_value import AzureStorageInfoValue
    from .name_value_pair import NameValuePair
    from .site_config import SiteConfig
    from .host_name_ssl_state import HostNameSslState
    from .site import Site
    from .capability import Capability
    from .sku_capacity import SkuCapacity
    from .sku_description import SkuDescription
    from .app_service_plan import AppServicePlan
    from .resource import Resource
    from .default_error_response_error_details_item import DefaultErrorResponseErrorDetailsItem
    from .default_error_response_error import DefaultErrorResponseError
    from .default_error_response import DefaultErrorResponse, DefaultErrorResponseException
    from .name_identifier import NameIdentifier
    from .log_specification import LogSpecification
    from .metric_availability import MetricAvailability
    from .dimension import Dimension
    from .metric_specification import MetricSpecification
    from .service_specification import ServiceSpecification
    from .csm_operation_description_properties import CsmOperationDescriptionProperties
    from .csm_operation_display import CsmOperationDisplay
    from .csm_operation_description import CsmOperationDescription
    from .address import Address
    from .contact import Contact
    from .host_name import HostName
    from .domain_purchase_consent import DomainPurchaseConsent
    from .domain import Domain
    from .domain_availablility_check_result import DomainAvailablilityCheckResult
    from .domain_control_center_sso_request import DomainControlCenterSsoRequest
    from .domain_ownership_identifier import DomainOwnershipIdentifier
    from .domain_patch_resource import DomainPatchResource
    from .domain_recommendation_search_parameters import DomainRecommendationSearchParameters
    from .tld_legal_agreement import TldLegalAgreement
    from .top_level_domain import TopLevelDomain
    from .top_level_domain_agreement_option import TopLevelDomainAgreementOption
    from .certificate import Certificate
    from .certificate_patch_resource import CertificatePatchResource
    from .virtual_network_profile import VirtualNetworkProfile
    from .worker_pool import WorkerPool
    from .virtual_ip_mapping import VirtualIPMapping
    from .stamp_capacity import StampCapacity
    from .network_access_control_entry import NetworkAccessControlEntry
    from .app_service_environment import AppServiceEnvironment
    from .localizable_string import LocalizableString
    from .csm_usage_quota import CsmUsageQuota
    from .deleted_site import DeletedSite
    from .error_entity import ErrorEntity
    from .operation import Operation
    from .resource_metric_name import ResourceMetricName
    from .resource_metric_property import ResourceMetricProperty
    from .resource_metric_value import ResourceMetricValue
    from .resource_metric import ResourceMetric
    from .web_app_collection import WebAppCollection
    from .solution import Solution
    from .detector_abnormal_time_period import DetectorAbnormalTimePeriod
    from .abnormal_time_period import AbnormalTimePeriod
    from .detector_definition import DetectorDefinition
    from .diagnostic_metric_sample import DiagnosticMetricSample
    from .diagnostic_metric_set import DiagnosticMetricSet
    from .data_source import DataSource
    from .response_meta_data import ResponseMetaData
    from .analysis_data import AnalysisData
    from .analysis_definition import AnalysisDefinition
    from .data_table_response_column import DataTableResponseColumn
    from .data_table_response_object import DataTableResponseObject
    from .detector_info import DetectorInfo
    from .rendering import Rendering
    from .diagnostic_data import DiagnosticData
    from .detector_response import DetectorResponse
    from .diagnostic_analysis import DiagnosticAnalysis
    from .diagnostic_category import DiagnosticCategory
    from .diagnostic_detector_response import DiagnosticDetectorResponse
    from .stack_minor_version import StackMinorVersion
    from .stack_major_version import StackMajorVersion
    from .application_stack import ApplicationStack
    from .recommendation import Recommendation
    from .recommendation_rule import RecommendationRule
    from .billing_meter import BillingMeter
    from .csm_move_resource_envelope import CsmMoveResourceEnvelope
    from .geo_region import GeoRegion
    from .hosting_environment_deployment_info import HostingEnvironmentDeploymentInfo
    from .deployment_locations import DeploymentLocations
    from .global_csm_sku_description import GlobalCsmSkuDescription
    from .premier_add_on_offer import PremierAddOnOffer
    from .resource_name_availability import ResourceNameAvailability
    from .resource_name_availability_request import ResourceNameAvailabilityRequest
    from .sku_infos import SkuInfos
    from .source_control import SourceControl
    from .validate_request import ValidateRequest
    from .validate_response_error import ValidateResponseError
    from .validate_response import ValidateResponse
    from .vnet_parameters import VnetParameters
    from .vnet_validation_test_failure import VnetValidationTestFailure
    from .vnet_validation_failure_details import VnetValidationFailureDetails
    from .file_system_application_logs_config import FileSystemApplicationLogsConfig
    from .azure_table_storage_application_logs_config import AzureTableStorageApplicationLogsConfig
    from .azure_blob_storage_application_logs_config import AzureBlobStorageApplicationLogsConfig
    from .application_logs_config import ApplicationLogsConfig
    from .azure_blob_storage_http_logs_config import AzureBlobStorageHttpLogsConfig
    from .azure_storage_property_dictionary_resource import AzureStoragePropertyDictionaryResource
    from .database_backup_setting import DatabaseBackupSetting
    from .backup_item import BackupItem
    from .backup_schedule import BackupSchedule
    from .backup_request import BackupRequest
    from .conn_string_value_type_pair import ConnStringValueTypePair
    from .connection_string_dictionary import ConnectionStringDictionary
    from .continuous_web_job import ContinuousWebJob
    from .csm_publishing_profile_options import CsmPublishingProfileOptions
    from .csm_slot_entity import CsmSlotEntity
    from .custom_hostname_analysis_result import CustomHostnameAnalysisResult
    from .deleted_app_restore_request import DeletedAppRestoreRequest
    from .deployment import Deployment
    from .enabled_config import EnabledConfig
    from .file_system_http_logs_config import FileSystemHttpLogsConfig
    from .function_envelope import FunctionEnvelope
    from .function_secrets import FunctionSecrets
    from .host_name_binding import HostNameBinding
    from .http_logs_config import HttpLogsConfig
    from .ms_deploy import MSDeploy
    from .ms_deploy_log_entry import MSDeployLogEntry
    from .ms_deploy_log import MSDeployLog
    from .ms_deploy_status import MSDeployStatus
    from .migrate_my_sql_request import MigrateMySqlRequest
    from .migrate_my_sql_status import MigrateMySqlStatus
    from .relay_service_connection_entity import RelayServiceConnectionEntity
    from .network_features import NetworkFeatures
    from .perf_mon_sample import PerfMonSample
    from .perf_mon_set import PerfMonSet
    from .perf_mon_response import PerfMonResponse
    from .premier_add_on import PremierAddOn
    from .premier_add_on_patch_resource import PremierAddOnPatchResource
    from .private_access_subnet import PrivateAccessSubnet
    from .private_access_virtual_network import PrivateAccessVirtualNetwork
    from .private_access import PrivateAccess
    from .process_thread_info import ProcessThreadInfo
    from .process_module_info import ProcessModuleInfo
    from .process_info import ProcessInfo
    from .public_certificate import PublicCertificate
    from .restore_request import RestoreRequest
    from .site_auth_settings import SiteAuthSettings
    from .site_cloneability_criterion import SiteCloneabilityCriterion
    from .site_cloneability import SiteCloneability
    from .site_config_resource import SiteConfigResource
    from .site_configuration_snapshot_info import SiteConfigurationSnapshotInfo
    from .site_extension_info import SiteExtensionInfo
    from .site_instance import SiteInstance
    from .site_logs_config import SiteLogsConfig
    from .site_patch_resource import SitePatchResource
    from .site_php_error_log_flag import SitePhpErrorLogFlag
    from .site_source_control import SiteSourceControl
    from .slot_config_names_resource import SlotConfigNamesResource
    from .slot_difference import SlotDifference
    from .snapshot_recovery_source import SnapshotRecoverySource
    from .snapshot_restore_request import SnapshotRestoreRequest
    from .storage_migration_options import StorageMigrationOptions
    from .storage_migration_response import StorageMigrationResponse
    from .string_dictionary import StringDictionary
    from .swift_virtual_network import SwiftVirtualNetwork
    from .triggered_job_run import TriggeredJobRun
    from .triggered_job_history import TriggeredJobHistory
    from .triggered_web_job import TriggeredWebJob
    from .web_job import WebJob
    from .address_response import AddressResponse
    from .app_service_environment_resource import AppServiceEnvironmentResource
    from .app_service_environment_patch_resource import AppServiceEnvironmentPatchResource
    from .hosting_environment_diagnostics import HostingEnvironmentDiagnostics
    from .metric_availabilily import MetricAvailabilily
    from .metric_definition import MetricDefinition
    from .sku_info import SkuInfo
    from .usage import Usage
    from .worker_pool_resource import WorkerPoolResource
    from .app_service_plan_patch_resource import AppServicePlanPatchResource
    from .hybrid_connection_limits import HybridConnectionLimits
from .app_service_certificate_order_paged import AppServiceCertificateOrderPaged
from .app_service_certificate_resource_paged import AppServiceCertificateResourcePaged
from .csm_operation_description_paged import CsmOperationDescriptionPaged
from .domain_paged import DomainPaged
from .name_identifier_paged import NameIdentifierPaged
from .domain_ownership_identifier_paged import DomainOwnershipIdentifierPaged
from .top_level_domain_paged import TopLevelDomainPaged
from .tld_legal_agreement_paged import TldLegalAgreementPaged
from .certificate_paged import CertificatePaged
from .deleted_site_paged import DeletedSitePaged
from .detector_response_paged import DetectorResponsePaged
from .diagnostic_category_paged import DiagnosticCategoryPaged
from .analysis_definition_paged import AnalysisDefinitionPaged
from .detector_definition_paged import DetectorDefinitionPaged
from .application_stack_paged import ApplicationStackPaged
from .recommendation_paged import RecommendationPaged
from .source_control_paged import SourceControlPaged
from .billing_meter_paged import BillingMeterPaged
from .geo_region_paged import GeoRegionPaged
from .identifier_paged import IdentifierPaged
from .premier_add_on_offer_paged import PremierAddOnOfferPaged
from .site_paged import SitePaged
from .backup_item_paged import BackupItemPaged
from .site_config_resource_paged import SiteConfigResourcePaged
from .site_configuration_snapshot_info_paged import SiteConfigurationSnapshotInfoPaged
from .continuous_web_job_paged import ContinuousWebJobPaged
from .deployment_paged import DeploymentPaged
from .function_envelope_paged import FunctionEnvelopePaged
from .host_name_binding_paged import HostNameBindingPaged
from .site_instance_paged import SiteInstancePaged
from .process_info_paged import ProcessInfoPaged
from .process_module_info_paged import ProcessModuleInfoPaged
from .process_thread_info_paged import ProcessThreadInfoPaged
from .resource_metric_definition_paged import ResourceMetricDefinitionPaged
from .resource_metric_paged import ResourceMetricPaged
from .perf_mon_response_paged import PerfMonResponsePaged
from .public_certificate_paged import PublicCertificatePaged
from .site_extension_info_paged import SiteExtensionInfoPaged
from .slot_difference_paged import SlotDifferencePaged
from .snapshot_paged import SnapshotPaged
from .triggered_web_job_paged import TriggeredWebJobPaged
from .triggered_job_history_paged import TriggeredJobHistoryPaged
from .csm_usage_quota_paged import CsmUsageQuotaPaged
from .web_job_paged import WebJobPaged
from .app_service_environment_resource_paged import AppServiceEnvironmentResourcePaged
from .stamp_capacity_paged import StampCapacityPaged
from .worker_pool_resource_paged import WorkerPoolResourcePaged
from .sku_info_paged import SkuInfoPaged
from .usage_paged import UsagePaged
from .app_service_plan_paged import AppServicePlanPaged
from .str_paged import StrPaged
from .hybrid_connection_paged import HybridConnectionPaged
from .web_site_management_client_enums import (
    KeyVaultSecretStatus,
    CertificateProductType,
    ProvisioningState,
    CertificateOrderStatus,
    CertificateOrderActionType,
    RouteType,
    ManagedServiceIdentityType,
    IpFilterTag,
    AutoHealActionType,
    ConnectionStringType,
    AzureStorageType,
    AzureStorageState,
    ScmType,
    ManagedPipelineMode,
    SiteLoadBalancing,
    SupportedTlsVersions,
    FtpsState,
    SslState,
    HostType,
    UsageState,
    SiteAvailabilityState,
    StatusOptions,
    DomainStatus,
    AzureResourceType,
    CustomHostNameDnsRecordType,
    HostNameType,
    DnsType,
    DomainType,
    HostingEnvironmentStatus,
    InternalLoadBalancingMode,
    ComputeModeOptions,
    WorkerSizeOptions,
    AccessControlEntryAction,
    OperationStatus,
    IssueType,
    SolutionType,
    RenderingType,
    ResourceScopeType,
    NotificationLevel,
    Channels,
    AppServicePlanRestrictions,
    InAvailabilityReasonType,
    CheckNameResourceTypes,
    ValidateResourceTypes,
    LogLevel,
    BackupItemStatus,
    DatabaseType,
    FrequencyUnit,
    ContinuousWebJobStatus,
    WebJobType,
    PublishingProfileFormat,
    DnsVerificationTestResult,
    MSDeployLogEntryType,
    MSDeployProvisioningState,
    MySqlMigrationType,
    PublicCertificateLocation,
    BackupRestoreOperationType,
    UnauthenticatedClientAction,
    BuiltInAuthenticationProvider,
    CloneAbilityResult,
    SiteExtensionType,
    TriggeredWebJobStatus,
    SkuName,
)

__all__ = [
    'AppServiceCertificate',
    'AppServiceCertificateResource',
    'CertificateDetails',
    'AppServiceCertificateOrder',
    'AppServiceCertificateOrderPatchResource',
    'AppServiceCertificatePatchResource',
    'CertificateEmail',
    'CertificateOrderAction',
    'ReissueCertificateOrderRequest',
    'RenewCertificateOrderRequest',
    'SiteSeal',
    'SiteSealRequest',
    'VnetRoute',
    'VnetInfo',
    'VnetGateway',
    'User',
    'Snapshot',
    'ResourceMetricAvailability',
    'ResourceMetricDefinition',
    'PushSettings',
    'Identifier',
    'HybridConnectionKey',
    'HybridConnection',
    'ProxyOnlyResource',
    'ManagedServiceIdentity',
    'SlotSwapStatus',
    'CloningInfo',
    'HostingEnvironmentProfile',
    'IpSecurityRestriction',
    'ApiDefinitionInfo',
    'CorsSettings',
    'AutoHealCustomAction',
    'AutoHealActions',
    'SlowRequestsBasedTrigger',
    'StatusCodesBasedTrigger',
    'RequestsBasedTrigger',
    'AutoHealTriggers',
    'AutoHealRules',
    'SiteLimits',
    'RampUpRule',
    'Experiments',
    'VirtualDirectory',
    'VirtualApplication',
    'HandlerMapping',
    'SiteMachineKey',
    'ConnStringInfo',
    'AzureStorageInfoValue',
    'NameValuePair',
    'SiteConfig',
    'HostNameSslState',
    'Site',
    'Capability',
    'SkuCapacity',
    'SkuDescription',
    'AppServicePlan',
    'Resource',
    'DefaultErrorResponseErrorDetailsItem',
    'DefaultErrorResponseError',
    'DefaultErrorResponse', 'DefaultErrorResponseException',
    'NameIdentifier',
    'LogSpecification',
    'MetricAvailability',
    'Dimension',
    'MetricSpecification',
    'ServiceSpecification',
    'CsmOperationDescriptionProperties',
    'CsmOperationDisplay',
    'CsmOperationDescription',
    'Address',
    'Contact',
    'HostName',
    'DomainPurchaseConsent',
    'Domain',
    'DomainAvailablilityCheckResult',
    'DomainControlCenterSsoRequest',
    'DomainOwnershipIdentifier',
    'DomainPatchResource',
    'DomainRecommendationSearchParameters',
    'TldLegalAgreement',
    'TopLevelDomain',
    'TopLevelDomainAgreementOption',
    'Certificate',
    'CertificatePatchResource',
    'VirtualNetworkProfile',
    'WorkerPool',
    'VirtualIPMapping',
    'StampCapacity',
    'NetworkAccessControlEntry',
    'AppServiceEnvironment',
    'LocalizableString',
    'CsmUsageQuota',
    'DeletedSite',
    'ErrorEntity',
    'Operation',
    'ResourceMetricName',
    'ResourceMetricProperty',
    'ResourceMetricValue',
    'ResourceMetric',
    'WebAppCollection',
    'Solution',
    'DetectorAbnormalTimePeriod',
    'AbnormalTimePeriod',
    'DetectorDefinition',
    'DiagnosticMetricSample',
    'DiagnosticMetricSet',
    'DataSource',
    'ResponseMetaData',
    'AnalysisData',
    'AnalysisDefinition',
    'DataTableResponseColumn',
    'DataTableResponseObject',
    'DetectorInfo',
    'Rendering',
    'DiagnosticData',
    'DetectorResponse',
    'DiagnosticAnalysis',
    'DiagnosticCategory',
    'DiagnosticDetectorResponse',
    'StackMinorVersion',
    'StackMajorVersion',
    'ApplicationStack',
    'Recommendation',
    'RecommendationRule',
    'BillingMeter',
    'CsmMoveResourceEnvelope',
    'GeoRegion',
    'HostingEnvironmentDeploymentInfo',
    'DeploymentLocations',
    'GlobalCsmSkuDescription',
    'PremierAddOnOffer',
    'ResourceNameAvailability',
    'ResourceNameAvailabilityRequest',
    'SkuInfos',
    'SourceControl',
    'ValidateRequest',
    'ValidateResponseError',
    'ValidateResponse',
    'VnetParameters',
    'VnetValidationTestFailure',
    'VnetValidationFailureDetails',
    'FileSystemApplicationLogsConfig',
    'AzureTableStorageApplicationLogsConfig',
    'AzureBlobStorageApplicationLogsConfig',
    'ApplicationLogsConfig',
    'AzureBlobStorageHttpLogsConfig',
    'AzureStoragePropertyDictionaryResource',
    'DatabaseBackupSetting',
    'BackupItem',
    'BackupSchedule',
    'BackupRequest',
    'ConnStringValueTypePair',
    'ConnectionStringDictionary',
    'ContinuousWebJob',
    'CsmPublishingProfileOptions',
    'CsmSlotEntity',
    'CustomHostnameAnalysisResult',
    'DeletedAppRestoreRequest',
    'Deployment',
    'EnabledConfig',
    'FileSystemHttpLogsConfig',
    'FunctionEnvelope',
    'FunctionSecrets',
    'HostNameBinding',
    'HttpLogsConfig',
    'MSDeploy',
    'MSDeployLogEntry',
    'MSDeployLog',
    'MSDeployStatus',
    'MigrateMySqlRequest',
    'MigrateMySqlStatus',
    'RelayServiceConnectionEntity',
    'NetworkFeatures',
    'PerfMonSample',
    'PerfMonSet',
    'PerfMonResponse',
    'PremierAddOn',
    'PremierAddOnPatchResource',
    'PrivateAccessSubnet',
    'PrivateAccessVirtualNetwork',
    'PrivateAccess',
    'ProcessThreadInfo',
    'ProcessModuleInfo',
    'ProcessInfo',
    'PublicCertificate',
    'RestoreRequest',
    'SiteAuthSettings',
    'SiteCloneabilityCriterion',
    'SiteCloneability',
    'SiteConfigResource',
    'SiteConfigurationSnapshotInfo',
    'SiteExtensionInfo',
    'SiteInstance',
    'SiteLogsConfig',
    'SitePatchResource',
    'SitePhpErrorLogFlag',
    'SiteSourceControl',
    'SlotConfigNamesResource',
    'SlotDifference',
    'SnapshotRecoverySource',
    'SnapshotRestoreRequest',
    'StorageMigrationOptions',
    'StorageMigrationResponse',
    'StringDictionary',
    'SwiftVirtualNetwork',
    'TriggeredJobRun',
    'TriggeredJobHistory',
    'TriggeredWebJob',
    'WebJob',
    'AddressResponse',
    'AppServiceEnvironmentResource',
    'AppServiceEnvironmentPatchResource',
    'HostingEnvironmentDiagnostics',
    'MetricAvailabilily',
    'MetricDefinition',
    'SkuInfo',
    'Usage',
    'WorkerPoolResource',
    'AppServicePlanPatchResource',
    'HybridConnectionLimits',
    'AppServiceCertificateOrderPaged',
    'AppServiceCertificateResourcePaged',
    'CsmOperationDescriptionPaged',
    'DomainPaged',
    'NameIdentifierPaged',
    'DomainOwnershipIdentifierPaged',
    'TopLevelDomainPaged',
    'TldLegalAgreementPaged',
    'CertificatePaged',
    'DeletedSitePaged',
    'DetectorResponsePaged',
    'DiagnosticCategoryPaged',
    'AnalysisDefinitionPaged',
    'DetectorDefinitionPaged',
    'ApplicationStackPaged',
    'RecommendationPaged',
    'SourceControlPaged',
    'BillingMeterPaged',
    'GeoRegionPaged',
    'IdentifierPaged',
    'PremierAddOnOfferPaged',
    'SitePaged',
    'BackupItemPaged',
    'SiteConfigResourcePaged',
    'SiteConfigurationSnapshotInfoPaged',
    'ContinuousWebJobPaged',
    'DeploymentPaged',
    'FunctionEnvelopePaged',
    'HostNameBindingPaged',
    'SiteInstancePaged',
    'ProcessInfoPaged',
    'ProcessModuleInfoPaged',
    'ProcessThreadInfoPaged',
    'ResourceMetricDefinitionPaged',
    'ResourceMetricPaged',
    'PerfMonResponsePaged',
    'PublicCertificatePaged',
    'SiteExtensionInfoPaged',
    'SlotDifferencePaged',
    'SnapshotPaged',
    'TriggeredWebJobPaged',
    'TriggeredJobHistoryPaged',
    'CsmUsageQuotaPaged',
    'WebJobPaged',
    'AppServiceEnvironmentResourcePaged',
    'StampCapacityPaged',
    'WorkerPoolResourcePaged',
    'SkuInfoPaged',
    'UsagePaged',
    'AppServicePlanPaged',
    'StrPaged',
    'HybridConnectionPaged',
    'KeyVaultSecretStatus',
    'CertificateProductType',
    'ProvisioningState',
    'CertificateOrderStatus',
    'CertificateOrderActionType',
    'RouteType',
    'ManagedServiceIdentityType',
    'IpFilterTag',
    'AutoHealActionType',
    'ConnectionStringType',
    'AzureStorageType',
    'AzureStorageState',
    'ScmType',
    'ManagedPipelineMode',
    'SiteLoadBalancing',
    'SupportedTlsVersions',
    'FtpsState',
    'SslState',
    'HostType',
    'UsageState',
    'SiteAvailabilityState',
    'StatusOptions',
    'DomainStatus',
    'AzureResourceType',
    'CustomHostNameDnsRecordType',
    'HostNameType',
    'DnsType',
    'DomainType',
    'HostingEnvironmentStatus',
    'InternalLoadBalancingMode',
    'ComputeModeOptions',
    'WorkerSizeOptions',
    'AccessControlEntryAction',
    'OperationStatus',
    'IssueType',
    'SolutionType',
    'RenderingType',
    'ResourceScopeType',
    'NotificationLevel',
    'Channels',
    'AppServicePlanRestrictions',
    'InAvailabilityReasonType',
    'CheckNameResourceTypes',
    'ValidateResourceTypes',
    'LogLevel',
    'BackupItemStatus',
    'DatabaseType',
    'FrequencyUnit',
    'ContinuousWebJobStatus',
    'WebJobType',
    'PublishingProfileFormat',
    'DnsVerificationTestResult',
    'MSDeployLogEntryType',
    'MSDeployProvisioningState',
    'MySqlMigrationType',
    'PublicCertificateLocation',
    'BackupRestoreOperationType',
    'UnauthenticatedClientAction',
    'BuiltInAuthenticationProvider',
    'CloneAbilityResult',
    'SiteExtensionType',
    'TriggeredWebJobStatus',
    'SkuName',
]
