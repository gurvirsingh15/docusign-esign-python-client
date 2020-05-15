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


class RecipientDomain(object):
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
        'active': 'str',
        'domain_code': 'str',
        'domain_name': 'str',
        'recipient_domain_id': 'str'
    }

    attribute_map = {
        'active': 'active',
        'domain_code': 'domainCode',
        'domain_name': 'domainName',
        'recipient_domain_id': 'recipientDomainId'
    }

    def __init__(self, active=None, domain_code=None, domain_name=None, recipient_domain_id=None):  # noqa: E501
        """RecipientDomain - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._domain_code = None
        self._domain_name = None
        self._recipient_domain_id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if domain_code is not None:
            self.domain_code = domain_code
        if domain_name is not None:
            self.domain_name = domain_name
        if recipient_domain_id is not None:
            self.recipient_domain_id = recipient_domain_id

    @property
    def active(self):
        """Gets the active of this RecipientDomain.  # noqa: E501

          # noqa: E501

        :return: The active of this RecipientDomain.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RecipientDomain.

          # noqa: E501

        :param active: The active of this RecipientDomain.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def domain_code(self):
        """Gets the domain_code of this RecipientDomain.  # noqa: E501

          # noqa: E501

        :return: The domain_code of this RecipientDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain_code

    @domain_code.setter
    def domain_code(self, domain_code):
        """Sets the domain_code of this RecipientDomain.

          # noqa: E501

        :param domain_code: The domain_code of this RecipientDomain.  # noqa: E501
        :type: str
        """

        self._domain_code = domain_code

    @property
    def domain_name(self):
        """Gets the domain_name of this RecipientDomain.  # noqa: E501

          # noqa: E501

        :return: The domain_name of this RecipientDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this RecipientDomain.

          # noqa: E501

        :param domain_name: The domain_name of this RecipientDomain.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def recipient_domain_id(self):
        """Gets the recipient_domain_id of this RecipientDomain.  # noqa: E501

          # noqa: E501

        :return: The recipient_domain_id of this RecipientDomain.  # noqa: E501
        :rtype: str
        """
        return self._recipient_domain_id

    @recipient_domain_id.setter
    def recipient_domain_id(self, recipient_domain_id):
        """Sets the recipient_domain_id of this RecipientDomain.

          # noqa: E501

        :param recipient_domain_id: The recipient_domain_id of this RecipientDomain.  # noqa: E501
        :type: str
        """

        self._recipient_domain_id = recipient_domain_id

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
        if issubclass(RecipientDomain, dict):
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
        if not isinstance(other, RecipientDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
