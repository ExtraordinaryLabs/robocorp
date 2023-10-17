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

class ProcessWebhookPayload(object):
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
        'endpoint': 'str',
        'enabled_events': 'ProcessWebhookEnabledEvents',
        'process': 'WorkspacesworkspaceIdworkergroupsworkerGroupIdworkersWorker'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'enabled_events': 'enabled_events',
        'process': 'process'
    }

    def __init__(self, endpoint=None, enabled_events=None, process=None):  # noqa: E501
        """ProcessWebhookPayload - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._enabled_events = None
        self._process = None
        self.discriminator = None
        self.endpoint = endpoint
        self.enabled_events = enabled_events
        self.process = process

    @property
    def endpoint(self):
        """Gets the endpoint of this ProcessWebhookPayload.  # noqa: E501


        :return: The endpoint of this ProcessWebhookPayload.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ProcessWebhookPayload.


        :param endpoint: The endpoint of this ProcessWebhookPayload.  # noqa: E501
        :type: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def enabled_events(self):
        """Gets the enabled_events of this ProcessWebhookPayload.  # noqa: E501


        :return: The enabled_events of this ProcessWebhookPayload.  # noqa: E501
        :rtype: ProcessWebhookEnabledEvents
        """
        return self._enabled_events

    @enabled_events.setter
    def enabled_events(self, enabled_events):
        """Sets the enabled_events of this ProcessWebhookPayload.


        :param enabled_events: The enabled_events of this ProcessWebhookPayload.  # noqa: E501
        :type: ProcessWebhookEnabledEvents
        """
        if enabled_events is None:
            raise ValueError("Invalid value for `enabled_events`, must not be `None`")  # noqa: E501

        self._enabled_events = enabled_events

    @property
    def process(self):
        """Gets the process of this ProcessWebhookPayload.  # noqa: E501


        :return: The process of this ProcessWebhookPayload.  # noqa: E501
        :rtype: WorkspacesworkspaceIdworkergroupsworkerGroupIdworkersWorker
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this ProcessWebhookPayload.


        :param process: The process of this ProcessWebhookPayload.  # noqa: E501
        :type: WorkspacesworkspaceIdworkergroupsworkerGroupIdworkersWorker
        """
        if process is None:
            raise ValueError("Invalid value for `process`, must not be `None`")  # noqa: E501

        self._process = process

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
        if issubclass(ProcessWebhookPayload, dict):
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
        if not isinstance(other, ProcessWebhookPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
