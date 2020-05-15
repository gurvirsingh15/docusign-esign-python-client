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


class AccountSharedAccess(object):
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
        'account_id': 'str',
        'end_position': 'str',
        'error_details': 'ErrorDetails',
        'next_uri': 'str',
        'previous_uri': 'str',
        'result_set_size': 'str',
        'shared_access': 'list[MemberSharedItems]',
        'start_position': 'str',
        'total_set_size': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'end_position': 'endPosition',
        'error_details': 'errorDetails',
        'next_uri': 'nextUri',
        'previous_uri': 'previousUri',
        'result_set_size': 'resultSetSize',
        'shared_access': 'sharedAccess',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize'
    }

    def __init__(self, account_id=None, end_position=None, error_details=None, next_uri=None, previous_uri=None, result_set_size=None, shared_access=None, start_position=None, total_set_size=None):  # noqa: E501
        """AccountSharedAccess - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._end_position = None
        self._error_details = None
        self._next_uri = None
        self._previous_uri = None
        self._result_set_size = None
        self._shared_access = None
        self._start_position = None
        self._total_set_size = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if end_position is not None:
            self.end_position = end_position
        if error_details is not None:
            self.error_details = error_details
        if next_uri is not None:
            self.next_uri = next_uri
        if previous_uri is not None:
            self.previous_uri = previous_uri
        if result_set_size is not None:
            self.result_set_size = result_set_size
        if shared_access is not None:
            self.shared_access = shared_access
        if start_position is not None:
            self.start_position = start_position
        if total_set_size is not None:
            self.total_set_size = total_set_size

    @property
    def account_id(self):
        """Gets the account_id of this AccountSharedAccess.  # noqa: E501

        The account ID associated with the envelope.  # noqa: E501

        :return: The account_id of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountSharedAccess.

        The account ID associated with the envelope.  # noqa: E501

        :param account_id: The account_id of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def end_position(self):
        """Gets the end_position of this AccountSharedAccess.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this AccountSharedAccess.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def error_details(self):
        """Gets the error_details of this AccountSharedAccess.  # noqa: E501


        :return: The error_details of this AccountSharedAccess.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this AccountSharedAccess.


        :param error_details: The error_details of this AccountSharedAccess.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def next_uri(self):
        """Gets the next_uri of this AccountSharedAccess.  # noqa: E501

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :return: The next_uri of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this AccountSharedAccess.

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :param next_uri: The next_uri of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """Gets the previous_uri of this AccountSharedAccess.  # noqa: E501

        The postal code for the billing address.  # noqa: E501

        :return: The previous_uri of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """Sets the previous_uri of this AccountSharedAccess.

        The postal code for the billing address.  # noqa: E501

        :param previous_uri: The previous_uri of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """Gets the result_set_size of this AccountSharedAccess.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this AccountSharedAccess.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def shared_access(self):
        """Gets the shared_access of this AccountSharedAccess.  # noqa: E501

        A complex type containing the shared access information to an envelope for the users specified in the request.  # noqa: E501

        :return: The shared_access of this AccountSharedAccess.  # noqa: E501
        :rtype: list[MemberSharedItems]
        """
        return self._shared_access

    @shared_access.setter
    def shared_access(self, shared_access):
        """Sets the shared_access of this AccountSharedAccess.

        A complex type containing the shared access information to an envelope for the users specified in the request.  # noqa: E501

        :param shared_access: The shared_access of this AccountSharedAccess.  # noqa: E501
        :type: list[MemberSharedItems]
        """

        self._shared_access = shared_access

    @property
    def start_position(self):
        """Gets the start_position of this AccountSharedAccess.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this AccountSharedAccess.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this AccountSharedAccess.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this AccountSharedAccess.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this AccountSharedAccess.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this AccountSharedAccess.  # noqa: E501
        :type: str
        """

        self._total_set_size = total_set_size

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
        if issubclass(AccountSharedAccess, dict):
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
        if not isinstance(other, AccountSharedAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
