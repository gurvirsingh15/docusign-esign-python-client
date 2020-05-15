# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..client.configuration import Configuration
from ..client.api_client import ApiClient


class EmailArchiveApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_bcc_email_archive(self, account_id, **kwargs):
        """
        Creates a blind carbon copy email archive entry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bcc_email_archive(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param BccEmailArchive bcc_email_archive:
        :return: BccEmailArchive
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_bcc_email_archive_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_bcc_email_archive_with_http_info(account_id, **kwargs)
            return data

    def create_bcc_email_archive_with_http_info(self, account_id, **kwargs):
        """
        Creates a blind carbon copy email archive entry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bcc_email_archive_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param BccEmailArchive bcc_email_archive:
        :return: BccEmailArchive
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'bcc_email_archive']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bcc_email_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_bcc_email_archive`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/settings/bcc_email_archives'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bcc_email_archive' in params:
            body_params = params['bcc_email_archive']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BccEmailArchive',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bcc_email_archive(self, account_id, bcc_email_archive_id, **kwargs):
        """
        Delete a blind carbon copy email archive for an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bcc_email_archive(account_id, bcc_email_archive_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str bcc_email_archive_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bcc_email_archive_with_http_info(account_id, bcc_email_archive_id, **kwargs)
        else:
            (data) = self.delete_bcc_email_archive_with_http_info(account_id, bcc_email_archive_id, **kwargs)
            return data

    def delete_bcc_email_archive_with_http_info(self, account_id, bcc_email_archive_id, **kwargs):
        """
        Delete a blind carbon copy email archive for an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bcc_email_archive_with_http_info(account_id, bcc_email_archive_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str bcc_email_archive_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'bcc_email_archive_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bcc_email_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_bcc_email_archive`")
        # verify the required parameter 'bcc_email_archive_id' is set
        if ('bcc_email_archive_id' not in params) or (params['bcc_email_archive_id'] is None):
            raise ValueError("Missing the required parameter `bcc_email_archive_id` when calling `delete_bcc_email_archive`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/settings/bcc_email_archives/{bccEmailArchiveId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'bcc_email_archive_id' in params:
            path_params['bccEmailArchiveId'] = params['bcc_email_archive_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bcc_email_archive_history_list(self, account_id, bcc_email_archive_id, **kwargs):
        """
        Get the blind carbon copy email archive history entries for the specified archive
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bcc_email_archive_history_list(account_id, bcc_email_archive_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str bcc_email_archive_id: (required)
        :param str count:
        :param str start_position:
        :return: BccEmailArchiveHistoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_bcc_email_archive_history_list_with_http_info(account_id, bcc_email_archive_id, **kwargs)
        else:
            (data) = self.get_bcc_email_archive_history_list_with_http_info(account_id, bcc_email_archive_id, **kwargs)
            return data

    def get_bcc_email_archive_history_list_with_http_info(self, account_id, bcc_email_archive_id, **kwargs):
        """
        Get the blind carbon copy email archive history entries for the specified archive
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bcc_email_archive_history_list_with_http_info(account_id, bcc_email_archive_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str bcc_email_archive_id: (required)
        :param str count:
        :param str start_position:
        :return: BccEmailArchiveHistoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'bcc_email_archive_id', 'count', 'start_position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bcc_email_archive_history_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_bcc_email_archive_history_list`")
        # verify the required parameter 'bcc_email_archive_id' is set
        if ('bcc_email_archive_id' not in params) or (params['bcc_email_archive_id'] is None):
            raise ValueError("Missing the required parameter `bcc_email_archive_id` when calling `get_bcc_email_archive_history_list`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/settings/bcc_email_archives/{bccEmailArchiveId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'bcc_email_archive_id' in params:
            path_params['bccEmailArchiveId'] = params['bcc_email_archive_id']

        query_params = {}
        if 'count' in params:
            query_params['count'] = params['count']
        if 'start_position' in params:
            query_params['start_position'] = params['start_position']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BccEmailArchiveHistoryList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bcc_email_archive_list(self, account_id, **kwargs):
        """
        Get the blind carbon copy email archive entries owned by the specified account
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bcc_email_archive_list(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str count:
        :param str start_position:
        :return: BccEmailArchiveList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_bcc_email_archive_list_with_http_info(account_id, **kwargs)
        else:
            (data) = self.get_bcc_email_archive_list_with_http_info(account_id, **kwargs)
            return data

    def get_bcc_email_archive_list_with_http_info(self, account_id, **kwargs):
        """
        Get the blind carbon copy email archive entries owned by the specified account
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bcc_email_archive_list_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str count:
        :param str start_position:
        :return: BccEmailArchiveList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'count', 'start_position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bcc_email_archive_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_bcc_email_archive_list`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/settings/bcc_email_archives'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'count' in params:
            query_params['count'] = params['count']
        if 'start_position' in params:
            query_params['start_position'] = params['start_position']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BccEmailArchiveList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
