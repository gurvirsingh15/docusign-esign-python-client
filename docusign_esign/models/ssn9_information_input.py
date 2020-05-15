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


class Ssn9InformationInput(object):
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
        'display_level_code': 'str',
        'ssn9': 'str'
    }

    attribute_map = {
        'display_level_code': 'displayLevelCode',
        'ssn9': 'ssn9'
    }

    def __init__(self, display_level_code=None, ssn9=None):  # noqa: E501
        """Ssn9InformationInput - a model defined in Swagger"""  # noqa: E501

        self._display_level_code = None
        self._ssn9 = None
        self.discriminator = None

        if display_level_code is not None:
            self.display_level_code = display_level_code
        if ssn9 is not None:
            self.ssn9 = ssn9

    @property
    def display_level_code(self):
        """Gets the display_level_code of this Ssn9InformationInput.  # noqa: E501

        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay  # noqa: E501

        :return: The display_level_code of this Ssn9InformationInput.  # noqa: E501
        :rtype: str
        """
        return self._display_level_code

    @display_level_code.setter
    def display_level_code(self, display_level_code):
        """Sets the display_level_code of this Ssn9InformationInput.

        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay  # noqa: E501

        :param display_level_code: The display_level_code of this Ssn9InformationInput.  # noqa: E501
        :type: str
        """

        self._display_level_code = display_level_code

    @property
    def ssn9(self):
        """Gets the ssn9 of this Ssn9InformationInput.  # noqa: E501

         The recipient's Social Security Number(SSN).  # noqa: E501

        :return: The ssn9 of this Ssn9InformationInput.  # noqa: E501
        :rtype: str
        """
        return self._ssn9

    @ssn9.setter
    def ssn9(self, ssn9):
        """Sets the ssn9 of this Ssn9InformationInput.

         The recipient's Social Security Number(SSN).  # noqa: E501

        :param ssn9: The ssn9 of this Ssn9InformationInput.  # noqa: E501
        :type: str
        """

        self._ssn9 = ssn9

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
        if issubclass(Ssn9InformationInput, dict):
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
        if not isinstance(other, Ssn9InformationInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
