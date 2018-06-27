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


class ResourceRecommendationBase(Model):
    """Advisor Recommendation.

    :param id: The fully qualified recommendation ID, for example
     /subscriptions/subscriptionId/resourceGroups/resourceGroup1/providers/Microsoft.ClassicCompute/virtualMachines/vm1/providers/Microsoft.Advisor/recommendations/recommendationGUID.
    :type id: str
    :param name: The name of recommendation.
    :type name: str
    :param category: The category of the recommendation. Possible values
     include: 'HighAvailability', 'Security', 'Performance', 'Cost'
    :type category: str or ~azure.mgmt.advisor.models.Category
    :param impact: The business impact of the recommendation. Possible values
     include: 'High', 'Medium', 'Low'
    :type impact: str or ~azure.mgmt.advisor.models.Impact
    :param impacted_field: The resource type identified by Advisor.
    :type impacted_field: str
    :param impacted_value: The resource identified by Advisor.
    :type impacted_value: str
    :param last_updated: The most recent time that Advisor checked the
     validity of the recommendation.
    :type last_updated: datetime
    :param metadata: The recommendation metadata.
    :type metadata: dict[str, object]
    :param recommendation_type_id: The recommendation-type GUID.
    :type recommendation_type_id: str
    :param risk: The potential risk of not implementing the recommendation.
     Possible values include: 'Error', 'Warning', 'None'
    :type risk: str or ~azure.mgmt.advisor.models.Risk
    :param short_description: A summary of the recommendation.
    :type short_description: ~azure.mgmt.advisor.models.ShortDescription
    :param suppression_ids: The list of snoozed and dismissed rules for the
     recommendation.
    :type suppression_ids: list[str]
    :param type: The recommendation type: Microsoft.Advisor/recommendations.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'impact': {'key': 'properties.impact', 'type': 'str'},
        'impacted_field': {'key': 'properties.impactedField', 'type': 'str'},
        'impacted_value': {'key': 'properties.impactedValue', 'type': 'str'},
        'last_updated': {'key': 'properties.lastUpdated', 'type': 'iso-8601'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
        'recommendation_type_id': {'key': 'properties.recommendationTypeId', 'type': 'str'},
        'risk': {'key': 'properties.risk', 'type': 'str'},
        'short_description': {'key': 'properties.shortDescription', 'type': 'ShortDescription'},
        'suppression_ids': {'key': 'suppressionIds', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, category=None, impact=None, impacted_field: str=None, impacted_value: str=None, last_updated=None, metadata=None, recommendation_type_id: str=None, risk=None, short_description=None, suppression_ids=None, type: str=None, **kwargs) -> None:
        super(ResourceRecommendationBase, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.category = category
        self.impact = impact
        self.impacted_field = impacted_field
        self.impacted_value = impacted_value
        self.last_updated = last_updated
        self.metadata = metadata
        self.recommendation_type_id = recommendation_type_id
        self.risk = risk
        self.short_description = short_description
        self.suppression_ids = suppression_ids
        self.type = type
