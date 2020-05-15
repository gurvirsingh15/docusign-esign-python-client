# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkspaceList(object):
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
        'end_position': 'str',
        'result_set_size': 'str',
        'start_position': 'str',
        'total_set_size': 'str',
        'workspaces': 'list[Workspace]'
    }

    attribute_map = {
        'end_position': 'endPosition',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize',
        'workspaces': 'workspaces'
    }

    def __init__(self, end_position=None, result_set_size=None, start_position=None, total_set_size=None, workspaces=None):  # noqa: E501
        """WorkspaceList - a model defined in Swagger"""  # noqa: E501

        self._end_position = None
        self._result_set_size = None
        self._start_position = None
        self._total_set_size = None
        self._workspaces = None
        self.discriminator = None

        if end_position is not None:
            self.end_position = end_position
        if result_set_size is not None:
            self.result_set_size = result_set_size
        if start_position is not None:
            self.start_position = start_position
        if total_set_size is not None:
            self.total_set_size = total_set_size
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def end_position(self):
        """Gets the end_position of this WorkspaceList.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this WorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this WorkspaceList.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this WorkspaceList.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def result_set_size(self):
        """Gets the result_set_size of this WorkspaceList.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this WorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this WorkspaceList.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this WorkspaceList.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this WorkspaceList.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this WorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this WorkspaceList.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this WorkspaceList.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this WorkspaceList.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this WorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this WorkspaceList.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this WorkspaceList.  # noqa: E501
        :type: str
        """

        self._total_set_size = total_set_size

    @property
    def workspaces(self):
        """Gets the workspaces of this WorkspaceList.  # noqa: E501

        A list of workspaces.  # noqa: E501

        :return: The workspaces of this WorkspaceList.  # noqa: E501
        :rtype: list[Workspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this WorkspaceList.

        A list of workspaces.  # noqa: E501

        :param workspaces: The workspaces of this WorkspaceList.  # noqa: E501
        :type: list[Workspace]
        """

        self._workspaces = workspaces

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
        if issubclass(WorkspaceList, dict):
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
        if not isinstance(other, WorkspaceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
