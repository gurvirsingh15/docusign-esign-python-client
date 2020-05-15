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


class RecipientPhoneNumber(object):
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
        'country_code': 'str',
        'country_code_metadata': 'PropertyMetadata',
        'number': 'str',
        'number_metadata': 'PropertyMetadata'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'country_code_metadata': 'countryCodeMetadata',
        'number': 'number',
        'number_metadata': 'numberMetadata'
    }

    def __init__(self, country_code=None, country_code_metadata=None, number=None, number_metadata=None):  # noqa: E501
        """RecipientPhoneNumber - a model defined in Swagger"""  # noqa: E501

        self._country_code = None
        self._country_code_metadata = None
        self._number = None
        self._number_metadata = None
        self.discriminator = None

        if country_code is not None:
            self.country_code = country_code
        if country_code_metadata is not None:
            self.country_code_metadata = country_code_metadata
        if number is not None:
            self.number = number
        if number_metadata is not None:
            self.number_metadata = number_metadata

    @property
    def country_code(self):
        """Gets the country_code of this RecipientPhoneNumber.  # noqa: E501

          # noqa: E501

        :return: The country_code of this RecipientPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RecipientPhoneNumber.

          # noqa: E501

        :param country_code: The country_code of this RecipientPhoneNumber.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country_code_metadata(self):
        """Gets the country_code_metadata of this RecipientPhoneNumber.  # noqa: E501


        :return: The country_code_metadata of this RecipientPhoneNumber.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._country_code_metadata

    @country_code_metadata.setter
    def country_code_metadata(self, country_code_metadata):
        """Sets the country_code_metadata of this RecipientPhoneNumber.


        :param country_code_metadata: The country_code_metadata of this RecipientPhoneNumber.  # noqa: E501
        :type: PropertyMetadata
        """

        self._country_code_metadata = country_code_metadata

    @property
    def number(self):
        """Gets the number of this RecipientPhoneNumber.  # noqa: E501

          # noqa: E501

        :return: The number of this RecipientPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RecipientPhoneNumber.

          # noqa: E501

        :param number: The number of this RecipientPhoneNumber.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def number_metadata(self):
        """Gets the number_metadata of this RecipientPhoneNumber.  # noqa: E501


        :return: The number_metadata of this RecipientPhoneNumber.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._number_metadata

    @number_metadata.setter
    def number_metadata(self, number_metadata):
        """Sets the number_metadata of this RecipientPhoneNumber.


        :param number_metadata: The number_metadata of this RecipientPhoneNumber.  # noqa: E501
        :type: PropertyMetadata
        """

        self._number_metadata = number_metadata

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
        if issubclass(RecipientPhoneNumber, dict):
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
        if not isinstance(other, RecipientPhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
