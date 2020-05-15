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


class OfflineAttributes(object):
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
        'account_esign_id': 'str',
        'device_model': 'str',
        'device_name': 'str',
        'gps_latitude': 'str',
        'gps_longitude': 'str',
        'offline_signing_hash': 'str'
    }

    attribute_map = {
        'account_esign_id': 'accountEsignId',
        'device_model': 'deviceModel',
        'device_name': 'deviceName',
        'gps_latitude': 'gpsLatitude',
        'gps_longitude': 'gpsLongitude',
        'offline_signing_hash': 'offlineSigningHash'
    }

    def __init__(self, account_esign_id=None, device_model=None, device_name=None, gps_latitude=None, gps_longitude=None, offline_signing_hash=None):  # noqa: E501
        """OfflineAttributes - a model defined in Swagger"""  # noqa: E501

        self._account_esign_id = None
        self._device_model = None
        self._device_name = None
        self._gps_latitude = None
        self._gps_longitude = None
        self._offline_signing_hash = None
        self.discriminator = None

        if account_esign_id is not None:
            self.account_esign_id = account_esign_id
        if device_model is not None:
            self.device_model = device_model
        if device_name is not None:
            self.device_name = device_name
        if gps_latitude is not None:
            self.gps_latitude = gps_latitude
        if gps_longitude is not None:
            self.gps_longitude = gps_longitude
        if offline_signing_hash is not None:
            self.offline_signing_hash = offline_signing_hash

    @property
    def account_esign_id(self):
        """Gets the account_esign_id of this OfflineAttributes.  # noqa: E501

        A GUID identifying the account associated with the consumer disclosure  # noqa: E501

        :return: The account_esign_id of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._account_esign_id

    @account_esign_id.setter
    def account_esign_id(self, account_esign_id):
        """Sets the account_esign_id of this OfflineAttributes.

        A GUID identifying the account associated with the consumer disclosure  # noqa: E501

        :param account_esign_id: The account_esign_id of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._account_esign_id = account_esign_id

    @property
    def device_model(self):
        """Gets the device_model of this OfflineAttributes.  # noqa: E501

        A string containing information about the model of the device used for offline signing.  # noqa: E501

        :return: The device_model of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this OfflineAttributes.

        A string containing information about the model of the device used for offline signing.  # noqa: E501

        :param device_model: The device_model of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def device_name(self):
        """Gets the device_name of this OfflineAttributes.  # noqa: E501

        A string containing information about the type of device used for offline signing.  # noqa: E501

        :return: The device_name of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this OfflineAttributes.

        A string containing information about the type of device used for offline signing.  # noqa: E501

        :param device_name: The device_name of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def gps_latitude(self):
        """Gets the gps_latitude of this OfflineAttributes.  # noqa: E501

        A string containing the latitude of the device location at the time of signing.  # noqa: E501

        :return: The gps_latitude of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._gps_latitude

    @gps_latitude.setter
    def gps_latitude(self, gps_latitude):
        """Sets the gps_latitude of this OfflineAttributes.

        A string containing the latitude of the device location at the time of signing.  # noqa: E501

        :param gps_latitude: The gps_latitude of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._gps_latitude = gps_latitude

    @property
    def gps_longitude(self):
        """Gets the gps_longitude of this OfflineAttributes.  # noqa: E501

        A string containing the longitude of the device location at the time of signing.  # noqa: E501

        :return: The gps_longitude of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._gps_longitude

    @gps_longitude.setter
    def gps_longitude(self, gps_longitude):
        """Sets the gps_longitude of this OfflineAttributes.

        A string containing the longitude of the device location at the time of signing.  # noqa: E501

        :param gps_longitude: The gps_longitude of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._gps_longitude = gps_longitude

    @property
    def offline_signing_hash(self):
        """Gets the offline_signing_hash of this OfflineAttributes.  # noqa: E501

          # noqa: E501

        :return: The offline_signing_hash of this OfflineAttributes.  # noqa: E501
        :rtype: str
        """
        return self._offline_signing_hash

    @offline_signing_hash.setter
    def offline_signing_hash(self, offline_signing_hash):
        """Sets the offline_signing_hash of this OfflineAttributes.

          # noqa: E501

        :param offline_signing_hash: The offline_signing_hash of this OfflineAttributes.  # noqa: E501
        :type: str
        """

        self._offline_signing_hash = offline_signing_hash

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
        if issubclass(OfflineAttributes, dict):
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
        if not isinstance(other, OfflineAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
