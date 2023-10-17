# coding: utf-8

"""
    Robocorp Control Room API

    Robocorp Control Room API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkitemsBatchBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'batch_operation': 'str',
        'work_item_ids': 'list[str]'
    }

    attribute_map = {
        'batch_operation': 'batch_operation',
        'work_item_ids': 'work_item_ids'
    }

    def __init__(self, batch_operation=None, work_item_ids=None):  # noqa: E501
        """WorkitemsBatchBody - a model defined in Swagger"""  # noqa: E501
        self._batch_operation = None
        self._work_item_ids = None
        self.discriminator = None
        self.batch_operation = batch_operation
        self.work_item_ids = work_item_ids

    @property
    def batch_operation(self):
        """Gets the batch_operation of this WorkitemsBatchBody.  # noqa: E501


        :return: The batch_operation of this WorkitemsBatchBody.  # noqa: E501
        :rtype: str
        """
        return self._batch_operation

    @batch_operation.setter
    def batch_operation(self, batch_operation):
        """Sets the batch_operation of this WorkitemsBatchBody.


        :param batch_operation: The batch_operation of this WorkitemsBatchBody.  # noqa: E501
        :type: str
        """
        if batch_operation is None:
            raise ValueError("Invalid value for `batch_operation`, must not be `None`")  # noqa: E501
        allowed_values = ["retry", "delete", "mark_as_done"]  # noqa: E501
        if batch_operation not in allowed_values:
            raise ValueError(
                "Invalid value for `batch_operation` ({0}), must be one of {1}"  # noqa: E501
                .format(batch_operation, allowed_values)
            )

        self._batch_operation = batch_operation

    @property
    def work_item_ids(self):
        """Gets the work_item_ids of this WorkitemsBatchBody.  # noqa: E501


        :return: The work_item_ids of this WorkitemsBatchBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._work_item_ids

    @work_item_ids.setter
    def work_item_ids(self, work_item_ids):
        """Sets the work_item_ids of this WorkitemsBatchBody.


        :param work_item_ids: The work_item_ids of this WorkitemsBatchBody.  # noqa: E501
        :type: list[str]
        """
        if work_item_ids is None:
            raise ValueError("Invalid value for `work_item_ids`, must not be `None`")  # noqa: E501

        self._work_item_ids = work_item_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WorkitemsBatchBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkitemsBatchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
