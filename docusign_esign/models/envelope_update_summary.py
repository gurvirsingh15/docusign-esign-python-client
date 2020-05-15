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


class EnvelopeUpdateSummary(object):
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
        'bulk_envelope_status': 'BulkEnvelopeStatus',
        'envelope_id': 'str',
        'error_details': 'ErrorDetails',
        'list_custom_field_update_results': 'list[ListCustomField]',
        'lock_information': 'LockInformation',
        'purge_state': 'str',
        'recipient_update_results': 'list[RecipientUpdateResponse]',
        'tab_update_results': 'Tabs',
        'text_custom_field_update_results': 'list[TextCustomField]'
    }

    attribute_map = {
        'bulk_envelope_status': 'bulkEnvelopeStatus',
        'envelope_id': 'envelopeId',
        'error_details': 'errorDetails',
        'list_custom_field_update_results': 'listCustomFieldUpdateResults',
        'lock_information': 'lockInformation',
        'purge_state': 'purgeState',
        'recipient_update_results': 'recipientUpdateResults',
        'tab_update_results': 'tabUpdateResults',
        'text_custom_field_update_results': 'textCustomFieldUpdateResults'
    }

    def __init__(self, bulk_envelope_status=None, envelope_id=None, error_details=None, list_custom_field_update_results=None, lock_information=None, purge_state=None, recipient_update_results=None, tab_update_results=None, text_custom_field_update_results=None):  # noqa: E501
        """EnvelopeUpdateSummary - a model defined in Swagger"""  # noqa: E501

        self._bulk_envelope_status = None
        self._envelope_id = None
        self._error_details = None
        self._list_custom_field_update_results = None
        self._lock_information = None
        self._purge_state = None
        self._recipient_update_results = None
        self._tab_update_results = None
        self._text_custom_field_update_results = None
        self.discriminator = None

        if bulk_envelope_status is not None:
            self.bulk_envelope_status = bulk_envelope_status
        if envelope_id is not None:
            self.envelope_id = envelope_id
        if error_details is not None:
            self.error_details = error_details
        if list_custom_field_update_results is not None:
            self.list_custom_field_update_results = list_custom_field_update_results
        if lock_information is not None:
            self.lock_information = lock_information
        if purge_state is not None:
            self.purge_state = purge_state
        if recipient_update_results is not None:
            self.recipient_update_results = recipient_update_results
        if tab_update_results is not None:
            self.tab_update_results = tab_update_results
        if text_custom_field_update_results is not None:
            self.text_custom_field_update_results = text_custom_field_update_results

    @property
    def bulk_envelope_status(self):
        """Gets the bulk_envelope_status of this EnvelopeUpdateSummary.  # noqa: E501


        :return: The bulk_envelope_status of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: BulkEnvelopeStatus
        """
        return self._bulk_envelope_status

    @bulk_envelope_status.setter
    def bulk_envelope_status(self, bulk_envelope_status):
        """Sets the bulk_envelope_status of this EnvelopeUpdateSummary.


        :param bulk_envelope_status: The bulk_envelope_status of this EnvelopeUpdateSummary.  # noqa: E501
        :type: BulkEnvelopeStatus
        """

        self._bulk_envelope_status = bulk_envelope_status

    @property
    def envelope_id(self):
        """Gets the envelope_id of this EnvelopeUpdateSummary.  # noqa: E501

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :return: The envelope_id of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """Sets the envelope_id of this EnvelopeUpdateSummary.

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :param envelope_id: The envelope_id of this EnvelopeUpdateSummary.  # noqa: E501
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def error_details(self):
        """Gets the error_details of this EnvelopeUpdateSummary.  # noqa: E501


        :return: The error_details of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this EnvelopeUpdateSummary.


        :param error_details: The error_details of this EnvelopeUpdateSummary.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def list_custom_field_update_results(self):
        """Gets the list_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501

          # noqa: E501

        :return: The list_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: list[ListCustomField]
        """
        return self._list_custom_field_update_results

    @list_custom_field_update_results.setter
    def list_custom_field_update_results(self, list_custom_field_update_results):
        """Sets the list_custom_field_update_results of this EnvelopeUpdateSummary.

          # noqa: E501

        :param list_custom_field_update_results: The list_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :type: list[ListCustomField]
        """

        self._list_custom_field_update_results = list_custom_field_update_results

    @property
    def lock_information(self):
        """Gets the lock_information of this EnvelopeUpdateSummary.  # noqa: E501


        :return: The lock_information of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: LockInformation
        """
        return self._lock_information

    @lock_information.setter
    def lock_information(self, lock_information):
        """Sets the lock_information of this EnvelopeUpdateSummary.


        :param lock_information: The lock_information of this EnvelopeUpdateSummary.  # noqa: E501
        :type: LockInformation
        """

        self._lock_information = lock_information

    @property
    def purge_state(self):
        """Gets the purge_state of this EnvelopeUpdateSummary.  # noqa: E501

          # noqa: E501

        :return: The purge_state of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: str
        """
        return self._purge_state

    @purge_state.setter
    def purge_state(self, purge_state):
        """Sets the purge_state of this EnvelopeUpdateSummary.

          # noqa: E501

        :param purge_state: The purge_state of this EnvelopeUpdateSummary.  # noqa: E501
        :type: str
        """

        self._purge_state = purge_state

    @property
    def recipient_update_results(self):
        """Gets the recipient_update_results of this EnvelopeUpdateSummary.  # noqa: E501

          # noqa: E501

        :return: The recipient_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: list[RecipientUpdateResponse]
        """
        return self._recipient_update_results

    @recipient_update_results.setter
    def recipient_update_results(self, recipient_update_results):
        """Sets the recipient_update_results of this EnvelopeUpdateSummary.

          # noqa: E501

        :param recipient_update_results: The recipient_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :type: list[RecipientUpdateResponse]
        """

        self._recipient_update_results = recipient_update_results

    @property
    def tab_update_results(self):
        """Gets the tab_update_results of this EnvelopeUpdateSummary.  # noqa: E501


        :return: The tab_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: Tabs
        """
        return self._tab_update_results

    @tab_update_results.setter
    def tab_update_results(self, tab_update_results):
        """Sets the tab_update_results of this EnvelopeUpdateSummary.


        :param tab_update_results: The tab_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :type: Tabs
        """

        self._tab_update_results = tab_update_results

    @property
    def text_custom_field_update_results(self):
        """Gets the text_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501

          # noqa: E501

        :return: The text_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :rtype: list[TextCustomField]
        """
        return self._text_custom_field_update_results

    @text_custom_field_update_results.setter
    def text_custom_field_update_results(self, text_custom_field_update_results):
        """Sets the text_custom_field_update_results of this EnvelopeUpdateSummary.

          # noqa: E501

        :param text_custom_field_update_results: The text_custom_field_update_results of this EnvelopeUpdateSummary.  # noqa: E501
        :type: list[TextCustomField]
        """

        self._text_custom_field_update_results = text_custom_field_update_results

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
        if issubclass(EnvelopeUpdateSummary, dict):
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
        if not isinstance(other, EnvelopeUpdateSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
