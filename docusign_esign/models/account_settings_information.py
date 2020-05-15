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


class AccountSettingsInformation(object):
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
        'account_settings': 'list[NameValue]'
    }

    attribute_map = {
        'account_settings': 'accountSettings'
    }

    def __init__(self, account_settings=None):  # noqa: E501
        """AccountSettingsInformation - a model defined in Swagger"""  # noqa: E501

        self._account_settings = None
        self.discriminator = None

        if account_settings is not None:
            self.account_settings = account_settings

    @property
    def account_settings(self):
        """Gets the account_settings of this AccountSettingsInformation.  # noqa: E501

        The list of account settings. These determine the features available for the account. Note that some features are determined by the plan used to create the account, and cannot be overridden.  # noqa: E501

        :return: The account_settings of this AccountSettingsInformation.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._account_settings

    @account_settings.setter
    def account_settings(self, account_settings):
        """Sets the account_settings of this AccountSettingsInformation.

        The list of account settings. These determine the features available for the account. Note that some features are determined by the plan used to create the account, and cannot be overridden.  # noqa: E501

        :param account_settings: The account_settings of this AccountSettingsInformation.  # noqa: E501
        :type: list[NameValue]
        """

        self._account_settings = account_settings

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
        if issubclass(AccountSettingsInformation, dict):
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
        if not isinstance(other, AccountSettingsInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
