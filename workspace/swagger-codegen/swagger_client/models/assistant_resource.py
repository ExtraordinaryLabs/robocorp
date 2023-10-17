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

class AssistantResource(object):
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
        'id': 'str',
        'name': 'str',
        'task': 'AssistantResourceTask',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'task': 'task',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, name=None, task=None, created_at=None):  # noqa: E501
        """AssistantResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._task = None
        self._created_at = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.task = task
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this AssistantResource.  # noqa: E501


        :return: The id of this AssistantResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssistantResource.


        :param id: The id of this AssistantResource.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssistantResource.  # noqa: E501


        :return: The name of this AssistantResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssistantResource.


        :param name: The name of this AssistantResource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def task(self):
        """Gets the task of this AssistantResource.  # noqa: E501


        :return: The task of this AssistantResource.  # noqa: E501
        :rtype: AssistantResourceTask
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this AssistantResource.


        :param task: The task of this AssistantResource.  # noqa: E501
        :type: AssistantResourceTask
        """
        if task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

    @property
    def created_at(self):
        """Gets the created_at of this AssistantResource.  # noqa: E501


        :return: The created_at of this AssistantResource.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AssistantResource.


        :param created_at: The created_at of this AssistantResource.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(AssistantResource, dict):
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
        if not isinstance(other, AssistantResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
