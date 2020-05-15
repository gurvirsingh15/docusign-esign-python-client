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


class CompositeTemplate(object):
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
        'composite_template_id': 'str',
        'document': 'Document',
        'inline_templates': 'list[InlineTemplate]',
        'pdf_meta_data_template_sequence': 'str',
        'server_templates': 'list[ServerTemplate]'
    }

    attribute_map = {
        'composite_template_id': 'compositeTemplateId',
        'document': 'document',
        'inline_templates': 'inlineTemplates',
        'pdf_meta_data_template_sequence': 'pdfMetaDataTemplateSequence',
        'server_templates': 'serverTemplates'
    }

    def __init__(self, composite_template_id=None, document=None, inline_templates=None, pdf_meta_data_template_sequence=None, server_templates=None):  # noqa: E501
        """CompositeTemplate - a model defined in Swagger"""  # noqa: E501

        self._composite_template_id = None
        self._document = None
        self._inline_templates = None
        self._pdf_meta_data_template_sequence = None
        self._server_templates = None
        self.discriminator = None

        if composite_template_id is not None:
            self.composite_template_id = composite_template_id
        if document is not None:
            self.document = document
        if inline_templates is not None:
            self.inline_templates = inline_templates
        if pdf_meta_data_template_sequence is not None:
            self.pdf_meta_data_template_sequence = pdf_meta_data_template_sequence
        if server_templates is not None:
            self.server_templates = server_templates

    @property
    def composite_template_id(self):
        """Gets the composite_template_id of this CompositeTemplate.  # noqa: E501

        The identify of this composite template. It is used as a reference when adding document object information. If used, the document's `content-disposition` must include the composite template ID to which the document should be added. If a composite template ID is not specified in the content-disposition, the document is applied based on the value of the `documentId` property only. If no document object is specified, the composite template inherits the first document.  # noqa: E501

        :return: The composite_template_id of this CompositeTemplate.  # noqa: E501
        :rtype: str
        """
        return self._composite_template_id

    @composite_template_id.setter
    def composite_template_id(self, composite_template_id):
        """Sets the composite_template_id of this CompositeTemplate.

        The identify of this composite template. It is used as a reference when adding document object information. If used, the document's `content-disposition` must include the composite template ID to which the document should be added. If a composite template ID is not specified in the content-disposition, the document is applied based on the value of the `documentId` property only. If no document object is specified, the composite template inherits the first document.  # noqa: E501

        :param composite_template_id: The composite_template_id of this CompositeTemplate.  # noqa: E501
        :type: str
        """

        self._composite_template_id = composite_template_id

    @property
    def document(self):
        """Gets the document of this CompositeTemplate.  # noqa: E501


        :return: The document of this CompositeTemplate.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this CompositeTemplate.


        :param document: The document of this CompositeTemplate.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def inline_templates(self):
        """Gets the inline_templates of this CompositeTemplate.  # noqa: E501

         Zero or more inline templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value.  # noqa: E501

        :return: The inline_templates of this CompositeTemplate.  # noqa: E501
        :rtype: list[InlineTemplate]
        """
        return self._inline_templates

    @inline_templates.setter
    def inline_templates(self, inline_templates):
        """Sets the inline_templates of this CompositeTemplate.

         Zero or more inline templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value.  # noqa: E501

        :param inline_templates: The inline_templates of this CompositeTemplate.  # noqa: E501
        :type: list[InlineTemplate]
        """

        self._inline_templates = inline_templates

    @property
    def pdf_meta_data_template_sequence(self):
        """Gets the pdf_meta_data_template_sequence of this CompositeTemplate.  # noqa: E501

          # noqa: E501

        :return: The pdf_meta_data_template_sequence of this CompositeTemplate.  # noqa: E501
        :rtype: str
        """
        return self._pdf_meta_data_template_sequence

    @pdf_meta_data_template_sequence.setter
    def pdf_meta_data_template_sequence(self, pdf_meta_data_template_sequence):
        """Sets the pdf_meta_data_template_sequence of this CompositeTemplate.

          # noqa: E501

        :param pdf_meta_data_template_sequence: The pdf_meta_data_template_sequence of this CompositeTemplate.  # noqa: E501
        :type: str
        """

        self._pdf_meta_data_template_sequence = pdf_meta_data_template_sequence

    @property
    def server_templates(self):
        """Gets the server_templates of this CompositeTemplate.  # noqa: E501

        0 or more server-side templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value  # noqa: E501

        :return: The server_templates of this CompositeTemplate.  # noqa: E501
        :rtype: list[ServerTemplate]
        """
        return self._server_templates

    @server_templates.setter
    def server_templates(self, server_templates):
        """Sets the server_templates of this CompositeTemplate.

        0 or more server-side templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value  # noqa: E501

        :param server_templates: The server_templates of this CompositeTemplate.  # noqa: E501
        :type: list[ServerTemplate]
        """

        self._server_templates = server_templates

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
        if issubclass(CompositeTemplate, dict):
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
        if not isinstance(other, CompositeTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
