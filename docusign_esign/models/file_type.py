# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileType(object):
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
        'file_extension': 'str',
        'mime_type': 'str'
    }

    attribute_map = {
        'file_extension': 'fileExtension',
        'mime_type': 'mimeType'
    }

    def __init__(self, file_extension=None, mime_type=None):  # noqa: E501
        """FileType - a model defined in Swagger"""  # noqa: E501

        self._file_extension = None
        self._mime_type = None
        self.discriminator = None

        if file_extension is not None:
            self.file_extension = file_extension
        if mime_type is not None:
            self.mime_type = mime_type

    @property
    def file_extension(self):
        """Gets the file_extension of this FileType.  # noqa: E501

          # noqa: E501

        :return: The file_extension of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this FileType.

          # noqa: E501

        :param file_extension: The file_extension of this FileType.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def mime_type(self):
        """Gets the mime_type of this FileType.  # noqa: E501

        The mime-type of a file type listed in a fileTypes collection.  # noqa: E501

        :return: The mime_type of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this FileType.

        The mime-type of a file type listed in a fileTypes collection.  # noqa: E501

        :param mime_type: The mime_type of this FileType.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

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
        if issubclass(FileType, dict):
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
        if not isinstance(other, FileType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
