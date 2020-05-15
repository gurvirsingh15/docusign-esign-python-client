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


class ChunkedUploadPart(object):
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
        'sequence': 'str',
        'size': 'str'
    }

    attribute_map = {
        'sequence': 'sequence',
        'size': 'size'
    }

    def __init__(self, sequence=None, size=None):  # noqa: E501
        """ChunkedUploadPart - a model defined in Swagger"""  # noqa: E501

        self._sequence = None
        self._size = None
        self.discriminator = None

        if sequence is not None:
            self.sequence = sequence
        if size is not None:
            self.size = size

    @property
    def sequence(self):
        """Gets the sequence of this ChunkedUploadPart.  # noqa: E501

          # noqa: E501

        :return: The sequence of this ChunkedUploadPart.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ChunkedUploadPart.

          # noqa: E501

        :param sequence: The sequence of this ChunkedUploadPart.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def size(self):
        """Gets the size of this ChunkedUploadPart.  # noqa: E501

          # noqa: E501

        :return: The size of this ChunkedUploadPart.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ChunkedUploadPart.

          # noqa: E501

        :param size: The size of this ChunkedUploadPart.  # noqa: E501
        :type: str
        """

        self._size = size

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
        if issubclass(ChunkedUploadPart, dict):
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
        if not isinstance(other, ChunkedUploadPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
