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


class Option(Model):
    """Option.

    :param additional_prop1:
    :type additional_prop1: str
    :param additional_prop2:
    :type additional_prop2: str
    :param additional_prop3:
    :type additional_prop3: str
    """

    _attribute_map = {
        'additional_prop1': {'key': 'additionalProp1', 'type': 'str'},
        'additional_prop2': {'key': 'additionalProp2', 'type': 'str'},
        'additional_prop3': {'key': 'additionalProp3', 'type': 'str'},
    }

    def __init__(self, *, additional_prop1: str=None, additional_prop2: str=None, additional_prop3: str=None, **kwargs) -> None:
        super(Option, self).__init__(**kwargs)
        self.additional_prop1 = additional_prop1
        self.additional_prop2 = additional_prop2
        self.additional_prop3 = additional_prop3
