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


class HostNameSslState(Model):
    """SSL-enabled hostname.

    :param name: Hostname.
    :type name: str
    :param ssl_state: SSL type. Possible values include: 'Disabled',
     'SniEnabled', 'IpBasedEnabled'
    :type ssl_state: str or ~azure.mgmt.web.models.SslState
    :param virtual_ip: Virtual IP address assigned to the hostname if IP based
     SSL is enabled.
    :type virtual_ip: str
    :param thumbprint: SSL certificate thumbprint.
    :type thumbprint: str
    :param to_update: Set to <code>true</code> to update existing hostname.
    :type to_update: bool
    :param host_type: Indicates whether the hostname is a standard or
     repository hostname. Possible values include: 'Standard', 'Repository'
    :type host_type: str or ~azure.mgmt.web.models.HostType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'ssl_state': {'key': 'sslState', 'type': 'SslState'},
        'virtual_ip': {'key': 'virtualIP', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'to_update': {'key': 'toUpdate', 'type': 'bool'},
        'host_type': {'key': 'hostType', 'type': 'HostType'},
    }

    def __init__(self, **kwargs):
        super(HostNameSslState, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.ssl_state = kwargs.get('ssl_state', None)
        self.virtual_ip = kwargs.get('virtual_ip', None)
        self.thumbprint = kwargs.get('thumbprint', None)
        self.to_update = kwargs.get('to_update', None)
        self.host_type = kwargs.get('host_type', None)
