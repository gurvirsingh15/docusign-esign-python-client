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


class DateStampProperties(object):
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
        'date_area_height': 'str',
        'date_area_width': 'str',
        'date_area_x': 'str',
        'date_area_y': 'str'
    }

    attribute_map = {
        'date_area_height': 'dateAreaHeight',
        'date_area_width': 'dateAreaWidth',
        'date_area_x': 'dateAreaX',
        'date_area_y': 'dateAreaY'
    }

    def __init__(self, date_area_height=None, date_area_width=None, date_area_x=None, date_area_y=None):  # noqa: E501
        """DateStampProperties - a model defined in Swagger"""  # noqa: E501

        self._date_area_height = None
        self._date_area_width = None
        self._date_area_x = None
        self._date_area_y = None
        self.discriminator = None

        if date_area_height is not None:
            self.date_area_height = date_area_height
        if date_area_width is not None:
            self.date_area_width = date_area_width
        if date_area_x is not None:
            self.date_area_x = date_area_x
        if date_area_y is not None:
            self.date_area_y = date_area_y

    @property
    def date_area_height(self):
        """Gets the date_area_height of this DateStampProperties.  # noqa: E501

          # noqa: E501

        :return: The date_area_height of this DateStampProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_area_height

    @date_area_height.setter
    def date_area_height(self, date_area_height):
        """Sets the date_area_height of this DateStampProperties.

          # noqa: E501

        :param date_area_height: The date_area_height of this DateStampProperties.  # noqa: E501
        :type: str
        """

        self._date_area_height = date_area_height

    @property
    def date_area_width(self):
        """Gets the date_area_width of this DateStampProperties.  # noqa: E501

          # noqa: E501

        :return: The date_area_width of this DateStampProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_area_width

    @date_area_width.setter
    def date_area_width(self, date_area_width):
        """Sets the date_area_width of this DateStampProperties.

          # noqa: E501

        :param date_area_width: The date_area_width of this DateStampProperties.  # noqa: E501
        :type: str
        """

        self._date_area_width = date_area_width

    @property
    def date_area_x(self):
        """Gets the date_area_x of this DateStampProperties.  # noqa: E501

          # noqa: E501

        :return: The date_area_x of this DateStampProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_area_x

    @date_area_x.setter
    def date_area_x(self, date_area_x):
        """Sets the date_area_x of this DateStampProperties.

          # noqa: E501

        :param date_area_x: The date_area_x of this DateStampProperties.  # noqa: E501
        :type: str
        """

        self._date_area_x = date_area_x

    @property
    def date_area_y(self):
        """Gets the date_area_y of this DateStampProperties.  # noqa: E501

          # noqa: E501

        :return: The date_area_y of this DateStampProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_area_y

    @date_area_y.setter
    def date_area_y(self, date_area_y):
        """Sets the date_area_y of this DateStampProperties.

          # noqa: E501

        :param date_area_y: The date_area_y of this DateStampProperties.  # noqa: E501
        :type: str
        """

        self._date_area_y = date_area_y

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
        if issubclass(DateStampProperties, dict):
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
        if not isinstance(other, DateStampProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
