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


class BrandLink(object):
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
        'link_text': 'str',
        'link_type': 'str',
        'show_link': 'str',
        'url_or_mail_to': 'str'
    }

    attribute_map = {
        'link_text': 'linkText',
        'link_type': 'linkType',
        'show_link': 'showLink',
        'url_or_mail_to': 'urlOrMailTo'
    }

    def __init__(self, link_text=None, link_type=None, show_link=None, url_or_mail_to=None):  # noqa: E501
        """BrandLink - a model defined in Swagger"""  # noqa: E501

        self._link_text = None
        self._link_type = None
        self._show_link = None
        self._url_or_mail_to = None
        self.discriminator = None

        if link_text is not None:
            self.link_text = link_text
        if link_type is not None:
            self.link_type = link_type
        if show_link is not None:
            self.show_link = show_link
        if url_or_mail_to is not None:
            self.url_or_mail_to = url_or_mail_to

    @property
    def link_text(self):
        """Gets the link_text of this BrandLink.  # noqa: E501

          # noqa: E501

        :return: The link_text of this BrandLink.  # noqa: E501
        :rtype: str
        """
        return self._link_text

    @link_text.setter
    def link_text(self, link_text):
        """Sets the link_text of this BrandLink.

          # noqa: E501

        :param link_text: The link_text of this BrandLink.  # noqa: E501
        :type: str
        """

        self._link_text = link_text

    @property
    def link_type(self):
        """Gets the link_type of this BrandLink.  # noqa: E501

          # noqa: E501

        :return: The link_type of this BrandLink.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this BrandLink.

          # noqa: E501

        :param link_type: The link_type of this BrandLink.  # noqa: E501
        :type: str
        """

        self._link_type = link_type

    @property
    def show_link(self):
        """Gets the show_link of this BrandLink.  # noqa: E501

          # noqa: E501

        :return: The show_link of this BrandLink.  # noqa: E501
        :rtype: str
        """
        return self._show_link

    @show_link.setter
    def show_link(self, show_link):
        """Sets the show_link of this BrandLink.

          # noqa: E501

        :param show_link: The show_link of this BrandLink.  # noqa: E501
        :type: str
        """

        self._show_link = show_link

    @property
    def url_or_mail_to(self):
        """Gets the url_or_mail_to of this BrandLink.  # noqa: E501

          # noqa: E501

        :return: The url_or_mail_to of this BrandLink.  # noqa: E501
        :rtype: str
        """
        return self._url_or_mail_to

    @url_or_mail_to.setter
    def url_or_mail_to(self, url_or_mail_to):
        """Sets the url_or_mail_to of this BrandLink.

          # noqa: E501

        :param url_or_mail_to: The url_or_mail_to of this BrandLink.  # noqa: E501
        :type: str
        """

        self._url_or_mail_to = url_or_mail_to

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
        if issubclass(BrandLink, dict):
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
        if not isinstance(other, BrandLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
