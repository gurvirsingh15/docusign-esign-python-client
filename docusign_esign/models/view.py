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


class View(object):
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
        'anchor_case_sensitive': 'str',
        'anchor_horizontal_alignment': 'str',
        'anchor_ignore_if_not_present': 'str',
        'anchor_match_whole_word': 'str',
        'anchor_string': 'str',
        'anchor_units': 'str',
        'anchor_x_offset': 'str',
        'anchor_y_offset': 'str',
        'bold': 'str',
        'button_text': 'str',
        'conditional_parent_label': 'str',
        'conditional_parent_value': 'str',
        'custom_tab_id': 'str',
        'document_id': 'str',
        'error_details': 'ErrorDetails',
        'font': 'str',
        'font_color': 'str',
        'font_size': 'str',
        'height': 'int',
        'italic': 'str',
        'merge_field': 'MergeField',
        'page_number': 'str',
        'recipient_id': 'str',
        'required': 'str',
        'required_read': 'str',
        'status': 'str',
        'tab_group_labels': 'list[str]',
        'tab_id': 'str',
        'tab_label': 'str',
        'tab_order': 'str',
        'template_locked': 'str',
        'template_required': 'str',
        'tooltip': 'str',
        'underline': 'str',
        'width': 'int',
        'x_position': 'str',
        'y_position': 'str'
    }

    attribute_map = {
        'anchor_case_sensitive': 'anchorCaseSensitive',
        'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
        'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
        'anchor_match_whole_word': 'anchorMatchWholeWord',
        'anchor_string': 'anchorString',
        'anchor_units': 'anchorUnits',
        'anchor_x_offset': 'anchorXOffset',
        'anchor_y_offset': 'anchorYOffset',
        'bold': 'bold',
        'button_text': 'buttonText',
        'conditional_parent_label': 'conditionalParentLabel',
        'conditional_parent_value': 'conditionalParentValue',
        'custom_tab_id': 'customTabId',
        'document_id': 'documentId',
        'error_details': 'errorDetails',
        'font': 'font',
        'font_color': 'fontColor',
        'font_size': 'fontSize',
        'height': 'height',
        'italic': 'italic',
        'merge_field': 'mergeField',
        'page_number': 'pageNumber',
        'recipient_id': 'recipientId',
        'required': 'required',
        'required_read': 'requiredRead',
        'status': 'status',
        'tab_group_labels': 'tabGroupLabels',
        'tab_id': 'tabId',
        'tab_label': 'tabLabel',
        'tab_order': 'tabOrder',
        'template_locked': 'templateLocked',
        'template_required': 'templateRequired',
        'tooltip': 'tooltip',
        'underline': 'underline',
        'width': 'width',
        'x_position': 'xPosition',
        'y_position': 'yPosition'
    }

    def __init__(self, anchor_case_sensitive=None, anchor_horizontal_alignment=None, anchor_ignore_if_not_present=None, anchor_match_whole_word=None, anchor_string=None, anchor_units=None, anchor_x_offset=None, anchor_y_offset=None, bold=None, button_text=None, conditional_parent_label=None, conditional_parent_value=None, custom_tab_id=None, document_id=None, error_details=None, font=None, font_color=None, font_size=None, height=None, italic=None, merge_field=None, page_number=None, recipient_id=None, required=None, required_read=None, status=None, tab_group_labels=None, tab_id=None, tab_label=None, tab_order=None, template_locked=None, template_required=None, tooltip=None, underline=None, width=None, x_position=None, y_position=None):  # noqa: E501
        """View - a model defined in Swagger"""  # noqa: E501

        self._anchor_case_sensitive = None
        self._anchor_horizontal_alignment = None
        self._anchor_ignore_if_not_present = None
        self._anchor_match_whole_word = None
        self._anchor_string = None
        self._anchor_units = None
        self._anchor_x_offset = None
        self._anchor_y_offset = None
        self._bold = None
        self._button_text = None
        self._conditional_parent_label = None
        self._conditional_parent_value = None
        self._custom_tab_id = None
        self._document_id = None
        self._error_details = None
        self._font = None
        self._font_color = None
        self._font_size = None
        self._height = None
        self._italic = None
        self._merge_field = None
        self._page_number = None
        self._recipient_id = None
        self._required = None
        self._required_read = None
        self._status = None
        self._tab_group_labels = None
        self._tab_id = None
        self._tab_label = None
        self._tab_order = None
        self._template_locked = None
        self._template_required = None
        self._tooltip = None
        self._underline = None
        self._width = None
        self._x_position = None
        self._y_position = None
        self.discriminator = None

        if anchor_case_sensitive is not None:
            self.anchor_case_sensitive = anchor_case_sensitive
        if anchor_horizontal_alignment is not None:
            self.anchor_horizontal_alignment = anchor_horizontal_alignment
        if anchor_ignore_if_not_present is not None:
            self.anchor_ignore_if_not_present = anchor_ignore_if_not_present
        if anchor_match_whole_word is not None:
            self.anchor_match_whole_word = anchor_match_whole_word
        if anchor_string is not None:
            self.anchor_string = anchor_string
        if anchor_units is not None:
            self.anchor_units = anchor_units
        if anchor_x_offset is not None:
            self.anchor_x_offset = anchor_x_offset
        if anchor_y_offset is not None:
            self.anchor_y_offset = anchor_y_offset
        if bold is not None:
            self.bold = bold
        if button_text is not None:
            self.button_text = button_text
        if conditional_parent_label is not None:
            self.conditional_parent_label = conditional_parent_label
        if conditional_parent_value is not None:
            self.conditional_parent_value = conditional_parent_value
        if custom_tab_id is not None:
            self.custom_tab_id = custom_tab_id
        if document_id is not None:
            self.document_id = document_id
        if error_details is not None:
            self.error_details = error_details
        if font is not None:
            self.font = font
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if height is not None:
            self.height = height
        if italic is not None:
            self.italic = italic
        if merge_field is not None:
            self.merge_field = merge_field
        if page_number is not None:
            self.page_number = page_number
        if recipient_id is not None:
            self.recipient_id = recipient_id
        if required is not None:
            self.required = required
        if required_read is not None:
            self.required_read = required_read
        if status is not None:
            self.status = status
        if tab_group_labels is not None:
            self.tab_group_labels = tab_group_labels
        if tab_id is not None:
            self.tab_id = tab_id
        if tab_label is not None:
            self.tab_label = tab_label
        if tab_order is not None:
            self.tab_order = tab_order
        if template_locked is not None:
            self.template_locked = template_locked
        if template_required is not None:
            self.template_required = template_required
        if tooltip is not None:
            self.tooltip = tooltip
        if underline is not None:
            self.underline = underline
        if width is not None:
            self.width = width
        if x_position is not None:
            self.x_position = x_position
        if y_position is not None:
            self.y_position = y_position

    @property
    def anchor_case_sensitive(self):
        """Gets the anchor_case_sensitive of this View.  # noqa: E501

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :return: The anchor_case_sensitive of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """Sets the anchor_case_sensitive of this View.

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :param anchor_case_sensitive: The anchor_case_sensitive of this View.  # noqa: E501
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """Gets the anchor_horizontal_alignment of this View.  # noqa: E501

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :return: The anchor_horizontal_alignment of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """Sets the anchor_horizontal_alignment of this View.

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this View.  # noqa: E501
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """Gets the anchor_ignore_if_not_present of this View.  # noqa: E501

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :return: The anchor_ignore_if_not_present of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """Sets the anchor_ignore_if_not_present of this View.

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this View.  # noqa: E501
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """Gets the anchor_match_whole_word of this View.  # noqa: E501

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :return: The anchor_match_whole_word of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """Sets the anchor_match_whole_word of this View.

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :param anchor_match_whole_word: The anchor_match_whole_word of this View.  # noqa: E501
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_string(self):
        """Gets the anchor_string of this View.  # noqa: E501

        Anchor text information for a radio button.  # noqa: E501

        :return: The anchor_string of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_string

    @anchor_string.setter
    def anchor_string(self, anchor_string):
        """Sets the anchor_string of this View.

        Anchor text information for a radio button.  # noqa: E501

        :param anchor_string: The anchor_string of this View.  # noqa: E501
        :type: str
        """

        self._anchor_string = anchor_string

    @property
    def anchor_units(self):
        """Gets the anchor_units of this View.  # noqa: E501

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :return: The anchor_units of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """Sets the anchor_units of this View.

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :param anchor_units: The anchor_units of this View.  # noqa: E501
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """Gets the anchor_x_offset of this View.  # noqa: E501

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_x_offset of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """Sets the anchor_x_offset of this View.

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_x_offset: The anchor_x_offset of this View.  # noqa: E501
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """Gets the anchor_y_offset of this View.  # noqa: E501

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_y_offset of this View.  # noqa: E501
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """Sets the anchor_y_offset of this View.

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_y_offset: The anchor_y_offset of this View.  # noqa: E501
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def bold(self):
        """Gets the bold of this View.  # noqa: E501

        When set to **true**, the information in the tab is bold.  # noqa: E501

        :return: The bold of this View.  # noqa: E501
        :rtype: str
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this View.

        When set to **true**, the information in the tab is bold.  # noqa: E501

        :param bold: The bold of this View.  # noqa: E501
        :type: str
        """

        self._bold = bold

    @property
    def button_text(self):
        """Gets the button_text of this View.  # noqa: E501

          # noqa: E501

        :return: The button_text of this View.  # noqa: E501
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this View.

          # noqa: E501

        :param button_text: The button_text of this View.  # noqa: E501
        :type: str
        """

        self._button_text = button_text

    @property
    def conditional_parent_label(self):
        """Gets the conditional_parent_label of this View.  # noqa: E501

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :return: The conditional_parent_label of this View.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_label

    @conditional_parent_label.setter
    def conditional_parent_label(self, conditional_parent_label):
        """Sets the conditional_parent_label of this View.

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :param conditional_parent_label: The conditional_parent_label of this View.  # noqa: E501
        :type: str
        """

        self._conditional_parent_label = conditional_parent_label

    @property
    def conditional_parent_value(self):
        """Gets the conditional_parent_value of this View.  # noqa: E501

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :return: The conditional_parent_value of this View.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_value

    @conditional_parent_value.setter
    def conditional_parent_value(self, conditional_parent_value):
        """Sets the conditional_parent_value of this View.

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :param conditional_parent_value: The conditional_parent_value of this View.  # noqa: E501
        :type: str
        """

        self._conditional_parent_value = conditional_parent_value

    @property
    def custom_tab_id(self):
        """Gets the custom_tab_id of this View.  # noqa: E501

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :return: The custom_tab_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._custom_tab_id

    @custom_tab_id.setter
    def custom_tab_id(self, custom_tab_id):
        """Sets the custom_tab_id of this View.

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :param custom_tab_id: The custom_tab_id of this View.  # noqa: E501
        :type: str
        """

        self._custom_tab_id = custom_tab_id

    @property
    def document_id(self):
        """Gets the document_id of this View.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this View.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this View.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def error_details(self):
        """Gets the error_details of this View.  # noqa: E501


        :return: The error_details of this View.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this View.


        :param error_details: The error_details of this View.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def font(self):
        """Gets the font of this View.  # noqa: E501

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :return: The font of this View.  # noqa: E501
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this View.

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :param font: The font of this View.  # noqa: E501
        :type: str
        """

        self._font = font

    @property
    def font_color(self):
        """Gets the font_color of this View.  # noqa: E501

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :return: The font_color of this View.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this View.

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :param font_color: The font_color of this View.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """Gets the font_size of this View.  # noqa: E501

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :return: The font_size of this View.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this View.

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :param font_size: The font_size of this View.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def height(self):
        """Gets the height of this View.  # noqa: E501

        Height of the tab in pixels.  # noqa: E501

        :return: The height of this View.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this View.

        Height of the tab in pixels.  # noqa: E501

        :param height: The height of this View.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def italic(self):
        """Gets the italic of this View.  # noqa: E501

        When set to **true**, the information in the tab is italic.  # noqa: E501

        :return: The italic of this View.  # noqa: E501
        :rtype: str
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """Sets the italic of this View.

        When set to **true**, the information in the tab is italic.  # noqa: E501

        :param italic: The italic of this View.  # noqa: E501
        :type: str
        """

        self._italic = italic

    @property
    def merge_field(self):
        """Gets the merge_field of this View.  # noqa: E501


        :return: The merge_field of this View.  # noqa: E501
        :rtype: MergeField
        """
        return self._merge_field

    @merge_field.setter
    def merge_field(self, merge_field):
        """Sets the merge_field of this View.


        :param merge_field: The merge_field of this View.  # noqa: E501
        :type: MergeField
        """

        self._merge_field = merge_field

    @property
    def page_number(self):
        """Gets the page_number of this View.  # noqa: E501

        Specifies the page number on which the tab is located.  # noqa: E501

        :return: The page_number of this View.  # noqa: E501
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this View.

        Specifies the page number on which the tab is located.  # noqa: E501

        :param page_number: The page_number of this View.  # noqa: E501
        :type: str
        """

        self._page_number = page_number

    @property
    def recipient_id(self):
        """Gets the recipient_id of this View.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this View.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this View.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def required(self):
        """Gets the required of this View.  # noqa: E501

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :return: The required of this View.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this View.

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :param required: The required of this View.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def required_read(self):
        """Gets the required_read of this View.  # noqa: E501

          # noqa: E501

        :return: The required_read of this View.  # noqa: E501
        :rtype: str
        """
        return self._required_read

    @required_read.setter
    def required_read(self, required_read):
        """Sets the required_read of this View.

          # noqa: E501

        :param required_read: The required_read of this View.  # noqa: E501
        :type: str
        """

        self._required_read = required_read

    @property
    def status(self):
        """Gets the status of this View.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this View.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this View.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this View.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tab_group_labels(self):
        """Gets the tab_group_labels of this View.  # noqa: E501

          # noqa: E501

        :return: The tab_group_labels of this View.  # noqa: E501
        :rtype: list[str]
        """
        return self._tab_group_labels

    @tab_group_labels.setter
    def tab_group_labels(self, tab_group_labels):
        """Sets the tab_group_labels of this View.

          # noqa: E501

        :param tab_group_labels: The tab_group_labels of this View.  # noqa: E501
        :type: list[str]
        """

        self._tab_group_labels = tab_group_labels

    @property
    def tab_id(self):
        """Gets the tab_id of this View.  # noqa: E501

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :return: The tab_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """Sets the tab_id of this View.

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :param tab_id: The tab_id of this View.  # noqa: E501
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_label(self):
        """Gets the tab_label of this View.  # noqa: E501

        The label string associated with the tab.  # noqa: E501

        :return: The tab_label of this View.  # noqa: E501
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """Sets the tab_label of this View.

        The label string associated with the tab.  # noqa: E501

        :param tab_label: The tab_label of this View.  # noqa: E501
        :type: str
        """

        self._tab_label = tab_label

    @property
    def tab_order(self):
        """Gets the tab_order of this View.  # noqa: E501

          # noqa: E501

        :return: The tab_order of this View.  # noqa: E501
        :rtype: str
        """
        return self._tab_order

    @tab_order.setter
    def tab_order(self, tab_order):
        """Sets the tab_order of this View.

          # noqa: E501

        :param tab_order: The tab_order of this View.  # noqa: E501
        :type: str
        """

        self._tab_order = tab_order

    @property
    def template_locked(self):
        """Gets the template_locked of this View.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this View.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this View.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this View.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """Gets the template_required of this View.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this View.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this View.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this View.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def tooltip(self):
        """Gets the tooltip of this View.  # noqa: E501

          # noqa: E501

        :return: The tooltip of this View.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this View.

          # noqa: E501

        :param tooltip: The tooltip of this View.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def underline(self):
        """Gets the underline of this View.  # noqa: E501

        When set to **true**, the information in the tab is underlined.  # noqa: E501

        :return: The underline of this View.  # noqa: E501
        :rtype: str
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """Sets the underline of this View.

        When set to **true**, the information in the tab is underlined.  # noqa: E501

        :param underline: The underline of this View.  # noqa: E501
        :type: str
        """

        self._underline = underline

    @property
    def width(self):
        """Gets the width of this View.  # noqa: E501

        Width of the tab in pixels.  # noqa: E501

        :return: The width of this View.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this View.

        Width of the tab in pixels.  # noqa: E501

        :param width: The width of this View.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def x_position(self):
        """Gets the x_position of this View.  # noqa: E501

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The x_position of this View.  # noqa: E501
        :rtype: str
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """Sets the x_position of this View.

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param x_position: The x_position of this View.  # noqa: E501
        :type: str
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """Gets the y_position of this View.  # noqa: E501

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The y_position of this View.  # noqa: E501
        :rtype: str
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """Sets the y_position of this View.

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param y_position: The y_position of this View.  # noqa: E501
        :type: str
        """

        self._y_position = y_position

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
        if issubclass(View, dict):
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
        if not isinstance(other, View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
