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


class ReportConfigDeliveryDestination(Model):
    """The destination information for the delivery of the report.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: Required. The resource id of the storage account where
     reports will be delivered.
    :type resource_id: str
    :param container: Required. The name of the container where reports will
     be uploaded.
    :type container: str
    :param root_folder_path: The name of the directory where reports will be
     uploaded.
    :type root_folder_path: str
    """

    _validation = {
        'resource_id': {'required': True},
        'container': {'required': True},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'container': {'key': 'container', 'type': 'str'},
        'root_folder_path': {'key': 'rootFolderPath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ReportConfigDeliveryDestination, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)
        self.container = kwargs.get('container', None)
        self.root_folder_path = kwargs.get('root_folder_path', None)
