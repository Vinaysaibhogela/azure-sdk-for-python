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

from msrest.serialization import Model


class ResourceNameAvailabilityRequest(Model):
    """Resource name availability request content.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Resource name to verify.
    :type name: str
    :param type: Required. Resource type used for verification. Possible
     values include: 'Site', 'Slot', 'HostingEnvironment', 'PublishingUser',
     'Microsoft.Web/sites', 'Microsoft.Web/sites/slots',
     'Microsoft.Web/hostingEnvironments', 'Microsoft.Web/publishingUsers'
    :type type: str or ~azure.mgmt.web.models.CheckNameResourceTypes
    :param is_fqdn: Is fully qualified domain name.
    :type is_fqdn: bool
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_fqdn': {'key': 'isFqdn', 'type': 'bool'},
    }

    def __init__(self, *, name: str, type, is_fqdn: bool=None, **kwargs) -> None:
        super(ResourceNameAvailabilityRequest, self).__init__(**kwargs)
        self.name = name
        self.type = type
        self.is_fqdn = is_fqdn
