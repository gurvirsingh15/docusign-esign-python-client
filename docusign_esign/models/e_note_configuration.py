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


class ENoteConfiguration(object):
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
        'api_key': 'str',
        'connect_configured': 'str',
        'e_note_configured': 'str',
        'organization': 'str',
        'password': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'connect_configured': 'connectConfigured',
        'e_note_configured': 'eNoteConfigured',
        'organization': 'organization',
        'password': 'password',
        'user_name': 'userName'
    }

    def __init__(self, api_key=None, connect_configured=None, e_note_configured=None, organization=None, password=None, user_name=None):  # noqa: E501
        """ENoteConfiguration - a model defined in Swagger"""  # noqa: E501

        self._api_key = None
        self._connect_configured = None
        self._e_note_configured = None
        self._organization = None
        self._password = None
        self._user_name = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if connect_configured is not None:
            self.connect_configured = connect_configured
        if e_note_configured is not None:
            self.e_note_configured = e_note_configured
        if organization is not None:
            self.organization = organization
        if password is not None:
            self.password = password
        if user_name is not None:
            self.user_name = user_name

    @property
    def api_key(self):
        """Gets the api_key of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The api_key of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ENoteConfiguration.

          # noqa: E501

        :param api_key: The api_key of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def connect_configured(self):
        """Gets the connect_configured of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The connect_configured of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._connect_configured

    @connect_configured.setter
    def connect_configured(self, connect_configured):
        """Sets the connect_configured of this ENoteConfiguration.

          # noqa: E501

        :param connect_configured: The connect_configured of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._connect_configured = connect_configured

    @property
    def e_note_configured(self):
        """Gets the e_note_configured of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The e_note_configured of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._e_note_configured

    @e_note_configured.setter
    def e_note_configured(self, e_note_configured):
        """Sets the e_note_configured of this ENoteConfiguration.

          # noqa: E501

        :param e_note_configured: The e_note_configured of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._e_note_configured = e_note_configured

    @property
    def organization(self):
        """Gets the organization of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The organization of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ENoteConfiguration.

          # noqa: E501

        :param organization: The organization of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def password(self):
        """Gets the password of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The password of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ENoteConfiguration.

          # noqa: E501

        :param password: The password of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user_name(self):
        """Gets the user_name of this ENoteConfiguration.  # noqa: E501

          # noqa: E501

        :return: The user_name of this ENoteConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ENoteConfiguration.

          # noqa: E501

        :param user_name: The user_name of this ENoteConfiguration.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(ENoteConfiguration, dict):
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
        if not isinstance(other, ENoteConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
