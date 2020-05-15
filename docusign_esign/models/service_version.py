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


class ServiceVersion(object):
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
        'version': 'str',
        'version_url': 'str'
    }

    attribute_map = {
        'version': 'version',
        'version_url': 'versionUrl'
    }

    def __init__(self, version=None, version_url=None):  # noqa: E501
        """ServiceVersion - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._version_url = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if version_url is not None:
            self.version_url = version_url

    @property
    def version(self):
        """Gets the version of this ServiceVersion.  # noqa: E501

        The version of the rest API.  # noqa: E501

        :return: The version of this ServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServiceVersion.

        The version of the rest API.  # noqa: E501

        :param version: The version of this ServiceVersion.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def version_url(self):
        """Gets the version_url of this ServiceVersion.  # noqa: E501

          # noqa: E501

        :return: The version_url of this ServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._version_url

    @version_url.setter
    def version_url(self, version_url):
        """Sets the version_url of this ServiceVersion.

          # noqa: E501

        :param version_url: The version_url of this ServiceVersion.  # noqa: E501
        :type: str
        """

        self._version_url = version_url

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
        if issubclass(ServiceVersion, dict):
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
        if not isinstance(other, ServiceVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
