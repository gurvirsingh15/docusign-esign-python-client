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


class NewAccountDefinition(object):
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
        'account_name': 'str',
        'account_settings': 'AccountSettingsInformation',
        'address_information': 'AccountAddress',
        'credit_card_information': 'CreditCardInformation',
        'direct_debit_processor_information': 'DirectDebitProcessorInformation',
        'distributor_code': 'str',
        'distributor_password': 'str',
        'envelope_partition_id': 'str',
        'initial_user': 'UserInformation',
        'payment_method': 'str',
        'payment_processor_information': 'PaymentProcessorInformation',
        'plan_information': 'PlanInformation',
        'referral_information': 'ReferralInformation',
        'social_account_information': 'SocialAccountInformation'
    }

    attribute_map = {
        'account_name': 'accountName',
        'account_settings': 'accountSettings',
        'address_information': 'addressInformation',
        'credit_card_information': 'creditCardInformation',
        'direct_debit_processor_information': 'directDebitProcessorInformation',
        'distributor_code': 'distributorCode',
        'distributor_password': 'distributorPassword',
        'envelope_partition_id': 'envelopePartitionId',
        'initial_user': 'initialUser',
        'payment_method': 'paymentMethod',
        'payment_processor_information': 'paymentProcessorInformation',
        'plan_information': 'planInformation',
        'referral_information': 'referralInformation',
        'social_account_information': 'socialAccountInformation'
    }

    def __init__(self, account_name=None, account_settings=None, address_information=None, credit_card_information=None, direct_debit_processor_information=None, distributor_code=None, distributor_password=None, envelope_partition_id=None, initial_user=None, payment_method=None, payment_processor_information=None, plan_information=None, referral_information=None, social_account_information=None):  # noqa: E501
        """NewAccountDefinition - a model defined in Swagger"""  # noqa: E501

        self._account_name = None
        self._account_settings = None
        self._address_information = None
        self._credit_card_information = None
        self._direct_debit_processor_information = None
        self._distributor_code = None
        self._distributor_password = None
        self._envelope_partition_id = None
        self._initial_user = None
        self._payment_method = None
        self._payment_processor_information = None
        self._plan_information = None
        self._referral_information = None
        self._social_account_information = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if account_settings is not None:
            self.account_settings = account_settings
        if address_information is not None:
            self.address_information = address_information
        if credit_card_information is not None:
            self.credit_card_information = credit_card_information
        if direct_debit_processor_information is not None:
            self.direct_debit_processor_information = direct_debit_processor_information
        if distributor_code is not None:
            self.distributor_code = distributor_code
        if distributor_password is not None:
            self.distributor_password = distributor_password
        if envelope_partition_id is not None:
            self.envelope_partition_id = envelope_partition_id
        if initial_user is not None:
            self.initial_user = initial_user
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_processor_information is not None:
            self.payment_processor_information = payment_processor_information
        if plan_information is not None:
            self.plan_information = plan_information
        if referral_information is not None:
            self.referral_information = referral_information
        if social_account_information is not None:
            self.social_account_information = social_account_information

    @property
    def account_name(self):
        """Gets the account_name of this NewAccountDefinition.  # noqa: E501

        The account name for the new account.  # noqa: E501

        :return: The account_name of this NewAccountDefinition.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this NewAccountDefinition.

        The account name for the new account.  # noqa: E501

        :param account_name: The account_name of this NewAccountDefinition.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_settings(self):
        """Gets the account_settings of this NewAccountDefinition.  # noqa: E501


        :return: The account_settings of this NewAccountDefinition.  # noqa: E501
        :rtype: AccountSettingsInformation
        """
        return self._account_settings

    @account_settings.setter
    def account_settings(self, account_settings):
        """Sets the account_settings of this NewAccountDefinition.


        :param account_settings: The account_settings of this NewAccountDefinition.  # noqa: E501
        :type: AccountSettingsInformation
        """

        self._account_settings = account_settings

    @property
    def address_information(self):
        """Gets the address_information of this NewAccountDefinition.  # noqa: E501


        :return: The address_information of this NewAccountDefinition.  # noqa: E501
        :rtype: AccountAddress
        """
        return self._address_information

    @address_information.setter
    def address_information(self, address_information):
        """Sets the address_information of this NewAccountDefinition.


        :param address_information: The address_information of this NewAccountDefinition.  # noqa: E501
        :type: AccountAddress
        """

        self._address_information = address_information

    @property
    def credit_card_information(self):
        """Gets the credit_card_information of this NewAccountDefinition.  # noqa: E501


        :return: The credit_card_information of this NewAccountDefinition.  # noqa: E501
        :rtype: CreditCardInformation
        """
        return self._credit_card_information

    @credit_card_information.setter
    def credit_card_information(self, credit_card_information):
        """Sets the credit_card_information of this NewAccountDefinition.


        :param credit_card_information: The credit_card_information of this NewAccountDefinition.  # noqa: E501
        :type: CreditCardInformation
        """

        self._credit_card_information = credit_card_information

    @property
    def direct_debit_processor_information(self):
        """Gets the direct_debit_processor_information of this NewAccountDefinition.  # noqa: E501


        :return: The direct_debit_processor_information of this NewAccountDefinition.  # noqa: E501
        :rtype: DirectDebitProcessorInformation
        """
        return self._direct_debit_processor_information

    @direct_debit_processor_information.setter
    def direct_debit_processor_information(self, direct_debit_processor_information):
        """Sets the direct_debit_processor_information of this NewAccountDefinition.


        :param direct_debit_processor_information: The direct_debit_processor_information of this NewAccountDefinition.  # noqa: E501
        :type: DirectDebitProcessorInformation
        """

        self._direct_debit_processor_information = direct_debit_processor_information

    @property
    def distributor_code(self):
        """Gets the distributor_code of this NewAccountDefinition.  # noqa: E501

        The code that identifies the billing plan groups and plans for the new account.  # noqa: E501

        :return: The distributor_code of this NewAccountDefinition.  # noqa: E501
        :rtype: str
        """
        return self._distributor_code

    @distributor_code.setter
    def distributor_code(self, distributor_code):
        """Sets the distributor_code of this NewAccountDefinition.

        The code that identifies the billing plan groups and plans for the new account.  # noqa: E501

        :param distributor_code: The distributor_code of this NewAccountDefinition.  # noqa: E501
        :type: str
        """

        self._distributor_code = distributor_code

    @property
    def distributor_password(self):
        """Gets the distributor_password of this NewAccountDefinition.  # noqa: E501

        The password for the distributorCode.  # noqa: E501

        :return: The distributor_password of this NewAccountDefinition.  # noqa: E501
        :rtype: str
        """
        return self._distributor_password

    @distributor_password.setter
    def distributor_password(self, distributor_password):
        """Sets the distributor_password of this NewAccountDefinition.

        The password for the distributorCode.  # noqa: E501

        :param distributor_password: The distributor_password of this NewAccountDefinition.  # noqa: E501
        :type: str
        """

        self._distributor_password = distributor_password

    @property
    def envelope_partition_id(self):
        """Gets the envelope_partition_id of this NewAccountDefinition.  # noqa: E501

          # noqa: E501

        :return: The envelope_partition_id of this NewAccountDefinition.  # noqa: E501
        :rtype: str
        """
        return self._envelope_partition_id

    @envelope_partition_id.setter
    def envelope_partition_id(self, envelope_partition_id):
        """Sets the envelope_partition_id of this NewAccountDefinition.

          # noqa: E501

        :param envelope_partition_id: The envelope_partition_id of this NewAccountDefinition.  # noqa: E501
        :type: str
        """

        self._envelope_partition_id = envelope_partition_id

    @property
    def initial_user(self):
        """Gets the initial_user of this NewAccountDefinition.  # noqa: E501


        :return: The initial_user of this NewAccountDefinition.  # noqa: E501
        :rtype: UserInformation
        """
        return self._initial_user

    @initial_user.setter
    def initial_user(self, initial_user):
        """Sets the initial_user of this NewAccountDefinition.


        :param initial_user: The initial_user of this NewAccountDefinition.  # noqa: E501
        :type: UserInformation
        """

        self._initial_user = initial_user

    @property
    def payment_method(self):
        """Gets the payment_method of this NewAccountDefinition.  # noqa: E501

          # noqa: E501

        :return: The payment_method of this NewAccountDefinition.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this NewAccountDefinition.

          # noqa: E501

        :param payment_method: The payment_method of this NewAccountDefinition.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment_processor_information(self):
        """Gets the payment_processor_information of this NewAccountDefinition.  # noqa: E501


        :return: The payment_processor_information of this NewAccountDefinition.  # noqa: E501
        :rtype: PaymentProcessorInformation
        """
        return self._payment_processor_information

    @payment_processor_information.setter
    def payment_processor_information(self, payment_processor_information):
        """Sets the payment_processor_information of this NewAccountDefinition.


        :param payment_processor_information: The payment_processor_information of this NewAccountDefinition.  # noqa: E501
        :type: PaymentProcessorInformation
        """

        self._payment_processor_information = payment_processor_information

    @property
    def plan_information(self):
        """Gets the plan_information of this NewAccountDefinition.  # noqa: E501


        :return: The plan_information of this NewAccountDefinition.  # noqa: E501
        :rtype: PlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """Sets the plan_information of this NewAccountDefinition.


        :param plan_information: The plan_information of this NewAccountDefinition.  # noqa: E501
        :type: PlanInformation
        """

        self._plan_information = plan_information

    @property
    def referral_information(self):
        """Gets the referral_information of this NewAccountDefinition.  # noqa: E501


        :return: The referral_information of this NewAccountDefinition.  # noqa: E501
        :rtype: ReferralInformation
        """
        return self._referral_information

    @referral_information.setter
    def referral_information(self, referral_information):
        """Sets the referral_information of this NewAccountDefinition.


        :param referral_information: The referral_information of this NewAccountDefinition.  # noqa: E501
        :type: ReferralInformation
        """

        self._referral_information = referral_information

    @property
    def social_account_information(self):
        """Gets the social_account_information of this NewAccountDefinition.  # noqa: E501


        :return: The social_account_information of this NewAccountDefinition.  # noqa: E501
        :rtype: SocialAccountInformation
        """
        return self._social_account_information

    @social_account_information.setter
    def social_account_information(self, social_account_information):
        """Sets the social_account_information of this NewAccountDefinition.


        :param social_account_information: The social_account_information of this NewAccountDefinition.  # noqa: E501
        :type: SocialAccountInformation
        """

        self._social_account_information = social_account_information

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
        if issubclass(NewAccountDefinition, dict):
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
        if not isinstance(other, NewAccountDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
