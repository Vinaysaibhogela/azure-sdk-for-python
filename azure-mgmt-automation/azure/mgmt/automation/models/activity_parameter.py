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


class ActivityParameter(Model):
    """Definition of the activity parameter.

    :param name: Gets or sets the name of the activity parameter.
    :type name: str
    :param type: Gets or sets the type of the activity parameter.
    :type type: str
    :param is_mandatory: Gets or sets a Boolean value that indicates true if
     the parameter is required. If the value is false, the parameter is
     optional.
    :type is_mandatory: bool
    :param is_dynamic: Gets or sets a Boolean value that indicates true if the
     parameter is dynamic.
    :type is_dynamic: bool
    :param position: Gets or sets the position of the activity parameter.
    :type position: long
    :param value_from_pipeline: Gets or sets a Boolean value that indicates
     true if the parameter can take values from the incoming pipeline objects.
     This setting is used if the cmdlet must access the complete input object.
     false indicates that the parameter cannot take values from the complete
     input object.
    :type value_from_pipeline: bool
    :param value_from_pipeline_by_property_name: Gets or sets a Boolean value
     that indicates true if the parameter can be filled from a property of the
     incoming pipeline object that has the same name as this parameter. false
     indicates that the parameter cannot be filled from the incoming pipeline
     object property with the same name.
    :type value_from_pipeline_by_property_name: bool
    :param value_from_remaining_arguments: Gets or sets a Boolean value that
     indicates true if the cmdlet parameter accepts all the remaining
     command-line arguments that are associated with this parameter in the form
     of an array. false if the cmdlet parameter does not accept all the
     remaining argument values.
    :type value_from_remaining_arguments: bool
    :param description: Gets or sets the description of the activity
     parameter.
    :type description: str
    :param validation_set: Gets or sets the validation set of activity
     parameter.
    :type validation_set:
     list[~azure.mgmt.automation.models.ActivityParameterValidationSet]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'is_dynamic': {'key': 'isDynamic', 'type': 'bool'},
        'position': {'key': 'position', 'type': 'long'},
        'value_from_pipeline': {'key': 'valueFromPipeline', 'type': 'bool'},
        'value_from_pipeline_by_property_name': {'key': 'valueFromPipelineByPropertyName', 'type': 'bool'},
        'value_from_remaining_arguments': {'key': 'valueFromRemainingArguments', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'validation_set': {'key': 'validationSet', 'type': '[ActivityParameterValidationSet]'},
    }

    def __init__(self, name=None, type=None, is_mandatory=None, is_dynamic=None, position=None, value_from_pipeline=None, value_from_pipeline_by_property_name=None, value_from_remaining_arguments=None, description=None, validation_set=None):
        super(ActivityParameter, self).__init__()
        self.name = name
        self.type = type
        self.is_mandatory = is_mandatory
        self.is_dynamic = is_dynamic
        self.position = position
        self.value_from_pipeline = value_from_pipeline
        self.value_from_pipeline_by_property_name = value_from_pipeline_by_property_name
        self.value_from_remaining_arguments = value_from_remaining_arguments
        self.description = description
        self.validation_set = validation_set
