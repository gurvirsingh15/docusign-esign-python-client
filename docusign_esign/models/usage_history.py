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


class UsageHistory(object):
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
        'last_sent_date_time': 'str',
        'last_signed_date_time': 'str',
        'sent_count': 'int',
        'signed_count': 'int'
    }

    attribute_map = {
        'last_sent_date_time': 'lastSentDateTime',
        'last_signed_date_time': 'lastSignedDateTime',
        'sent_count': 'sentCount',
        'signed_count': 'signedCount'
    }

    def __init__(self, last_sent_date_time=None, last_signed_date_time=None, sent_count=None, signed_count=None):  # noqa: E501
        """UsageHistory - a model defined in Swagger"""  # noqa: E501

        self._last_sent_date_time = None
        self._last_signed_date_time = None
        self._sent_count = None
        self._signed_count = None
        self.discriminator = None

        if last_sent_date_time is not None:
            self.last_sent_date_time = last_sent_date_time
        if last_signed_date_time is not None:
            self.last_signed_date_time = last_signed_date_time
        if sent_count is not None:
            self.sent_count = sent_count
        if signed_count is not None:
            self.signed_count = signed_count

    @property
    def last_sent_date_time(self):
        """Gets the last_sent_date_time of this UsageHistory.  # noqa: E501

        The date and time the user last sent an envelope.   # noqa: E501

        :return: The last_sent_date_time of this UsageHistory.  # noqa: E501
        :rtype: str
        """
        return self._last_sent_date_time

    @last_sent_date_time.setter
    def last_sent_date_time(self, last_sent_date_time):
        """Sets the last_sent_date_time of this UsageHistory.

        The date and time the user last sent an envelope.   # noqa: E501

        :param last_sent_date_time: The last_sent_date_time of this UsageHistory.  # noqa: E501
        :type: str
        """

        self._last_sent_date_time = last_sent_date_time

    @property
    def last_signed_date_time(self):
        """Gets the last_signed_date_time of this UsageHistory.  # noqa: E501

        The date and time the user last signed an envelope.  # noqa: E501

        :return: The last_signed_date_time of this UsageHistory.  # noqa: E501
        :rtype: str
        """
        return self._last_signed_date_time

    @last_signed_date_time.setter
    def last_signed_date_time(self, last_signed_date_time):
        """Sets the last_signed_date_time of this UsageHistory.

        The date and time the user last signed an envelope.  # noqa: E501

        :param last_signed_date_time: The last_signed_date_time of this UsageHistory.  # noqa: E501
        :type: str
        """

        self._last_signed_date_time = last_signed_date_time

    @property
    def sent_count(self):
        """Gets the sent_count of this UsageHistory.  # noqa: E501

        The number of envelopes the user has sent.   # noqa: E501

        :return: The sent_count of this UsageHistory.  # noqa: E501
        :rtype: int
        """
        return self._sent_count

    @sent_count.setter
    def sent_count(self, sent_count):
        """Sets the sent_count of this UsageHistory.

        The number of envelopes the user has sent.   # noqa: E501

        :param sent_count: The sent_count of this UsageHistory.  # noqa: E501
        :type: int
        """

        self._sent_count = sent_count

    @property
    def signed_count(self):
        """Gets the signed_count of this UsageHistory.  # noqa: E501

        The number of envelopes the user has signed.   # noqa: E501

        :return: The signed_count of this UsageHistory.  # noqa: E501
        :rtype: int
        """
        return self._signed_count

    @signed_count.setter
    def signed_count(self, signed_count):
        """Sets the signed_count of this UsageHistory.

        The number of envelopes the user has signed.   # noqa: E501

        :param signed_count: The signed_count of this UsageHistory.  # noqa: E501
        :type: int
        """

        self._signed_count = signed_count

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
        if issubclass(UsageHistory, dict):
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
        if not isinstance(other, UsageHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
