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


class FolderItemV2(object):
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
        'completed_date_time': 'str',
        'created_date_time': 'str',
        'envelope_id': 'str',
        'envelope_uri': 'str',
        'expire_date_time': 'str',
        'folder_id': 'str',
        'folder_uri': 'str',
        'is21_cfr_part11': 'str',
        'is_signature_provider_envelope': 'str',
        'last_modified_date_time': 'str',
        'owner_name': 'str',
        'recipients': 'Recipients',
        'recipients_uri': 'str',
        'sender_company': 'str',
        'sender_email': 'str',
        'sender_name': 'str',
        'sender_user_id': 'str',
        'sent_date_time': 'str',
        'status': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'completed_date_time': 'completedDateTime',
        'created_date_time': 'createdDateTime',
        'envelope_id': 'envelopeId',
        'envelope_uri': 'envelopeUri',
        'expire_date_time': 'expireDateTime',
        'folder_id': 'folderId',
        'folder_uri': 'folderUri',
        'is21_cfr_part11': 'is21CFRPart11',
        'is_signature_provider_envelope': 'isSignatureProviderEnvelope',
        'last_modified_date_time': 'lastModifiedDateTime',
        'owner_name': 'ownerName',
        'recipients': 'recipients',
        'recipients_uri': 'recipientsUri',
        'sender_company': 'senderCompany',
        'sender_email': 'senderEmail',
        'sender_name': 'senderName',
        'sender_user_id': 'senderUserId',
        'sent_date_time': 'sentDateTime',
        'status': 'status',
        'subject': 'subject'
    }

    def __init__(self, completed_date_time=None, created_date_time=None, envelope_id=None, envelope_uri=None, expire_date_time=None, folder_id=None, folder_uri=None, is21_cfr_part11=None, is_signature_provider_envelope=None, last_modified_date_time=None, owner_name=None, recipients=None, recipients_uri=None, sender_company=None, sender_email=None, sender_name=None, sender_user_id=None, sent_date_time=None, status=None, subject=None):  # noqa: E501
        """FolderItemV2 - a model defined in Swagger"""  # noqa: E501

        self._completed_date_time = None
        self._created_date_time = None
        self._envelope_id = None
        self._envelope_uri = None
        self._expire_date_time = None
        self._folder_id = None
        self._folder_uri = None
        self._is21_cfr_part11 = None
        self._is_signature_provider_envelope = None
        self._last_modified_date_time = None
        self._owner_name = None
        self._recipients = None
        self._recipients_uri = None
        self._sender_company = None
        self._sender_email = None
        self._sender_name = None
        self._sender_user_id = None
        self._sent_date_time = None
        self._status = None
        self._subject = None
        self.discriminator = None

        if completed_date_time is not None:
            self.completed_date_time = completed_date_time
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if envelope_id is not None:
            self.envelope_id = envelope_id
        if envelope_uri is not None:
            self.envelope_uri = envelope_uri
        if expire_date_time is not None:
            self.expire_date_time = expire_date_time
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_uri is not None:
            self.folder_uri = folder_uri
        if is21_cfr_part11 is not None:
            self.is21_cfr_part11 = is21_cfr_part11
        if is_signature_provider_envelope is not None:
            self.is_signature_provider_envelope = is_signature_provider_envelope
        if last_modified_date_time is not None:
            self.last_modified_date_time = last_modified_date_time
        if owner_name is not None:
            self.owner_name = owner_name
        if recipients is not None:
            self.recipients = recipients
        if recipients_uri is not None:
            self.recipients_uri = recipients_uri
        if sender_company is not None:
            self.sender_company = sender_company
        if sender_email is not None:
            self.sender_email = sender_email
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_user_id is not None:
            self.sender_user_id = sender_user_id
        if sent_date_time is not None:
            self.sent_date_time = sent_date_time
        if status is not None:
            self.status = status
        if subject is not None:
            self.subject = subject

    @property
    def completed_date_time(self):
        """Gets the completed_date_time of this FolderItemV2.  # noqa: E501

        Specifies the date and time this item was completed.  # noqa: E501

        :return: The completed_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._completed_date_time

    @completed_date_time.setter
    def completed_date_time(self, completed_date_time):
        """Sets the completed_date_time of this FolderItemV2.

        Specifies the date and time this item was completed.  # noqa: E501

        :param completed_date_time: The completed_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._completed_date_time = completed_date_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this FolderItemV2.  # noqa: E501

        Indicates the date and time the item was created.  # noqa: E501

        :return: The created_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this FolderItemV2.

        Indicates the date and time the item was created.  # noqa: E501

        :param created_date_time: The created_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def envelope_id(self):
        """Gets the envelope_id of this FolderItemV2.  # noqa: E501

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :return: The envelope_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """Sets the envelope_id of this FolderItemV2.

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :param envelope_id: The envelope_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def envelope_uri(self):
        """Gets the envelope_uri of this FolderItemV2.  # noqa: E501

        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.  # noqa: E501

        :return: The envelope_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._envelope_uri

    @envelope_uri.setter
    def envelope_uri(self, envelope_uri):
        """Sets the envelope_uri of this FolderItemV2.

        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.  # noqa: E501

        :param envelope_uri: The envelope_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._envelope_uri = envelope_uri

    @property
    def expire_date_time(self):
        """Gets the expire_date_time of this FolderItemV2.  # noqa: E501

        The date and time the envelope is set to expire.  # noqa: E501

        :return: The expire_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._expire_date_time

    @expire_date_time.setter
    def expire_date_time(self, expire_date_time):
        """Sets the expire_date_time of this FolderItemV2.

        The date and time the envelope is set to expire.  # noqa: E501

        :param expire_date_time: The expire_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._expire_date_time = expire_date_time

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The folder_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderItemV2.

          # noqa: E501

        :param folder_id: The folder_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_uri(self):
        """Gets the folder_uri of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The folder_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._folder_uri

    @folder_uri.setter
    def folder_uri(self, folder_uri):
        """Sets the folder_uri of this FolderItemV2.

          # noqa: E501

        :param folder_uri: The folder_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._folder_uri = folder_uri

    @property
    def is21_cfr_part11(self):
        """Gets the is21_cfr_part11 of this FolderItemV2.  # noqa: E501

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :return: The is21_cfr_part11 of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._is21_cfr_part11

    @is21_cfr_part11.setter
    def is21_cfr_part11(self, is21_cfr_part11):
        """Sets the is21_cfr_part11 of this FolderItemV2.

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :param is21_cfr_part11: The is21_cfr_part11 of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._is21_cfr_part11 = is21_cfr_part11

    @property
    def is_signature_provider_envelope(self):
        """Gets the is_signature_provider_envelope of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The is_signature_provider_envelope of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._is_signature_provider_envelope

    @is_signature_provider_envelope.setter
    def is_signature_provider_envelope(self, is_signature_provider_envelope):
        """Sets the is_signature_provider_envelope of this FolderItemV2.

          # noqa: E501

        :param is_signature_provider_envelope: The is_signature_provider_envelope of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._is_signature_provider_envelope = is_signature_provider_envelope

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this FolderItemV2.  # noqa: E501

        The date and time the item was last modified.  # noqa: E501

        :return: The last_modified_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this FolderItemV2.

        The date and time the item was last modified.  # noqa: E501

        :param last_modified_date_time: The last_modified_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._last_modified_date_time = last_modified_date_time

    @property
    def owner_name(self):
        """Gets the owner_name of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The owner_name of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this FolderItemV2.

          # noqa: E501

        :param owner_name: The owner_name of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def recipients(self):
        """Gets the recipients of this FolderItemV2.  # noqa: E501


        :return: The recipients of this FolderItemV2.  # noqa: E501
        :rtype: Recipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this FolderItemV2.


        :param recipients: The recipients of this FolderItemV2.  # noqa: E501
        :type: Recipients
        """

        self._recipients = recipients

    @property
    def recipients_uri(self):
        """Gets the recipients_uri of this FolderItemV2.  # noqa: E501

        Contains a URI for an endpoint that you can use to retrieve the recipients.  # noqa: E501

        :return: The recipients_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._recipients_uri

    @recipients_uri.setter
    def recipients_uri(self, recipients_uri):
        """Sets the recipients_uri of this FolderItemV2.

        Contains a URI for an endpoint that you can use to retrieve the recipients.  # noqa: E501

        :param recipients_uri: The recipients_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._recipients_uri = recipients_uri

    @property
    def sender_company(self):
        """Gets the sender_company of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_company of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_company

    @sender_company.setter
    def sender_company(self, sender_company):
        """Sets the sender_company of this FolderItemV2.

          # noqa: E501

        :param sender_company: The sender_company of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_company = sender_company

    @property
    def sender_email(self):
        """Gets the sender_email of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_email of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this FolderItemV2.

          # noqa: E501

        :param sender_email: The sender_email of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self):
        """Gets the sender_name of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_name of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this FolderItemV2.

          # noqa: E501

        :param sender_name: The sender_name of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_user_id(self):
        """Gets the sender_user_id of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_user_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """Sets the sender_user_id of this FolderItemV2.

          # noqa: E501

        :param sender_user_id: The sender_user_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_user_id = sender_user_id

    @property
    def sent_date_time(self):
        """Gets the sent_date_time of this FolderItemV2.  # noqa: E501

        The date and time the envelope was sent.  # noqa: E501

        :return: The sent_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sent_date_time

    @sent_date_time.setter
    def sent_date_time(self, sent_date_time):
        """Sets the sent_date_time of this FolderItemV2.

        The date and time the envelope was sent.  # noqa: E501

        :param sent_date_time: The sent_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sent_date_time = sent_date_time

    @property
    def status(self):
        """Gets the status of this FolderItemV2.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FolderItemV2.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subject(self):
        """Gets the subject of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The subject of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this FolderItemV2.

          # noqa: E501

        :param subject: The subject of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if issubclass(FolderItemV2, dict):
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
        if not isinstance(other, FolderItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
