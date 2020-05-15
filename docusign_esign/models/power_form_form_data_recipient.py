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


class PowerFormFormDataRecipient(object):
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
        'email': 'str',
        'form_data': 'list[NameValue]',
        'name': 'str',
        'recipient_id': 'str'
    }

    attribute_map = {
        'email': 'email',
        'form_data': 'formData',
        'name': 'name',
        'recipient_id': 'recipientId'
    }

    def __init__(self, email=None, form_data=None, name=None, recipient_id=None):  # noqa: E501
        """PowerFormFormDataRecipient - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._form_data = None
        self._name = None
        self._recipient_id = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if form_data is not None:
            self.form_data = form_data
        if name is not None:
            self.name = name
        if recipient_id is not None:
            self.recipient_id = recipient_id

    @property
    def email(self):
        """Gets the email of this PowerFormFormDataRecipient.  # noqa: E501

          # noqa: E501

        :return: The email of this PowerFormFormDataRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PowerFormFormDataRecipient.

          # noqa: E501

        :param email: The email of this PowerFormFormDataRecipient.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def form_data(self):
        """Gets the form_data of this PowerFormFormDataRecipient.  # noqa: E501

          # noqa: E501

        :return: The form_data of this PowerFormFormDataRecipient.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """Sets the form_data of this PowerFormFormDataRecipient.

          # noqa: E501

        :param form_data: The form_data of this PowerFormFormDataRecipient.  # noqa: E501
        :type: list[NameValue]
        """

        self._form_data = form_data

    @property
    def name(self):
        """Gets the name of this PowerFormFormDataRecipient.  # noqa: E501

          # noqa: E501

        :return: The name of this PowerFormFormDataRecipient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PowerFormFormDataRecipient.

          # noqa: E501

        :param name: The name of this PowerFormFormDataRecipient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recipient_id(self):
        """Gets the recipient_id of this PowerFormFormDataRecipient.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this PowerFormFormDataRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this PowerFormFormDataRecipient.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this PowerFormFormDataRecipient.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

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
        if issubclass(PowerFormFormDataRecipient, dict):
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
        if not isinstance(other, PowerFormFormDataRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
