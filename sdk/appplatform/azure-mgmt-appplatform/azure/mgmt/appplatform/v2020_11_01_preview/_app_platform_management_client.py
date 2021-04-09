# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import AppPlatformManagementClientConfiguration
from .operations import ServicesOperations
from .operations import ConfigServersOperations
from .operations import MonitoringSettingsOperations
from .operations import AppsOperations
from .operations import BindingsOperations
from .operations import CertificatesOperations
from .operations import CustomDomainsOperations
from .operations import DeploymentsOperations
from .operations import Operations
from .operations import RuntimeVersionsOperations
from .operations import SkusOperations
from . import models


class AppPlatformManagementClient(object):
    """REST API for Azure Spring Cloud.

    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.appplatform.v2020_11_01_preview.operations.ServicesOperations
    :ivar config_servers: ConfigServersOperations operations
    :vartype config_servers: azure.mgmt.appplatform.v2020_11_01_preview.operations.ConfigServersOperations
    :ivar monitoring_settings: MonitoringSettingsOperations operations
    :vartype monitoring_settings: azure.mgmt.appplatform.v2020_11_01_preview.operations.MonitoringSettingsOperations
    :ivar apps: AppsOperations operations
    :vartype apps: azure.mgmt.appplatform.v2020_11_01_preview.operations.AppsOperations
    :ivar bindings: BindingsOperations operations
    :vartype bindings: azure.mgmt.appplatform.v2020_11_01_preview.operations.BindingsOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.appplatform.v2020_11_01_preview.operations.CertificatesOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains: azure.mgmt.appplatform.v2020_11_01_preview.operations.CustomDomainsOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.appplatform.v2020_11_01_preview.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.v2020_11_01_preview.operations.Operations
    :ivar runtime_versions: RuntimeVersionsOperations operations
    :vartype runtime_versions: azure.mgmt.appplatform.v2020_11_01_preview.operations.RuntimeVersionsOperations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.appplatform.v2020_11_01_preview.operations.SkusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AppPlatformManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.services = ServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.config_servers = ConfigServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitoring_settings = MonitoringSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bindings = BindingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.runtime_versions = RuntimeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AppPlatformManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)