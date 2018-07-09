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


class StorageAccount(Model):
    """The storage Account.

    :param name: The name of the storage account.
    :type name: str
    :param is_default: Whether or not the storage account is the default
     storage account.
    :type is_default: bool
    :param container: The container in the storage account, only to be
     specified for WASB storage accounts.
    :type container: str
    :param file_system: The filesystem, only to be specified for Azure Data
     Lake Storage type Gen 2.
    :type file_system: str
    :param key: The storage account access key.
    :type key: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'container': {'key': 'container', 'type': 'str'},
        'file_system': {'key': 'fileSystem', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, name=None, is_default=None, container=None, file_system=None, key=None):
        super(StorageAccount, self).__init__()
        self.name = name
        self.is_default = is_default
        self.container = container
        self.file_system = file_system
        self.key = key
