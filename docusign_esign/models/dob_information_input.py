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


class DobInformationInput(object):
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
        'date_of_birth': 'str',
        'display_level_code': 'str',
        'receive_in_response': 'str'
    }

    attribute_map = {
        'date_of_birth': 'dateOfBirth',
        'display_level_code': 'displayLevelCode',
        'receive_in_response': 'receiveInResponse'
    }

    def __init__(self, date_of_birth=None, display_level_code=None, receive_in_response=None):  # noqa: E501
        """DobInformationInput - a model defined in Swagger"""  # noqa: E501

        self._date_of_birth = None
        self._display_level_code = None
        self._receive_in_response = None
        self.discriminator = None

        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if display_level_code is not None:
            self.display_level_code = display_level_code
        if receive_in_response is not None:
            self.receive_in_response = receive_in_response

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this DobInformationInput.  # noqa: E501

        Specifies the recipient's date, month, and year of birth.  # noqa: E501

        :return: The date_of_birth of this DobInformationInput.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this DobInformationInput.

        Specifies the recipient's date, month, and year of birth.  # noqa: E501

        :param date_of_birth: The date_of_birth of this DobInformationInput.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def display_level_code(self):
        """Gets the display_level_code of this DobInformationInput.  # noqa: E501

        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay  # noqa: E501

        :return: The display_level_code of this DobInformationInput.  # noqa: E501
        :rtype: str
        """
        return self._display_level_code

    @display_level_code.setter
    def display_level_code(self, display_level_code):
        """Sets the display_level_code of this DobInformationInput.

        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay  # noqa: E501

        :param display_level_code: The display_level_code of this DobInformationInput.  # noqa: E501
        :type: str
        """

        self._display_level_code = display_level_code

    @property
    def receive_in_response(self):
        """Gets the receive_in_response of this DobInformationInput.  # noqa: E501

        When set to **true**, the information needs to be returned in the response.  # noqa: E501

        :return: The receive_in_response of this DobInformationInput.  # noqa: E501
        :rtype: str
        """
        return self._receive_in_response

    @receive_in_response.setter
    def receive_in_response(self, receive_in_response):
        """Sets the receive_in_response of this DobInformationInput.

        When set to **true**, the information needs to be returned in the response.  # noqa: E501

        :param receive_in_response: The receive_in_response of this DobInformationInput.  # noqa: E501
        :type: str
        """

        self._receive_in_response = receive_in_response

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
        if issubclass(DobInformationInput, dict):
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
        if not isinstance(other, DobInformationInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
