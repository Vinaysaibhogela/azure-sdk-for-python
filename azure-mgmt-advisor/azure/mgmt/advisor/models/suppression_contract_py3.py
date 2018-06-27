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

from .resource_py3 import Resource


class SuppressionContract(Resource):
    """The details of the snoozed or dismissed rule; for example, the duration,
    name, and GUID associated with the rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource. This cannot be changed
     after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param suppression_id: The GUID of the suppression.
    :type suppression_id: str
    :param ttl: The duration for which the suppression is valid.
    :type ttl: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'suppression_id': {'key': 'suppressionId', 'type': 'str'},
        'ttl': {'key': 'ttl', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, suppression_id: str=None, ttl: str=None, **kwargs) -> None:
        super(SuppressionContract, self).__init__(location=location, tags=tags, **kwargs)
        self.suppression_id = suppression_id
        self.ttl = ttl
