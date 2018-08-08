# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.status import Status  # noqa: F401,E501
from swagger_server import util


class InlineResponse2007(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, s: Status=None, errmsg: str=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger

        :param s: The s of this InlineResponse2007.  # noqa: E501
        :type s: Status
        :param errmsg: The errmsg of this InlineResponse2007.  # noqa: E501
        :type errmsg: str
        """
        self.swagger_types = {
            's': Status,
            'errmsg': str
        }

        self.attribute_map = {
            's': 's',
            'errmsg': 'errmsg'
        }

        self._s = s
        self._errmsg = errmsg

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2007':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_7 of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2007
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s(self) -> Status:
        """Gets the s of this InlineResponse2007.


        :return: The s of this InlineResponse2007.
        :rtype: Status
        """
        return self._s

    @s.setter
    def s(self, s: Status):
        """Sets the s of this InlineResponse2007.


        :param s: The s of this InlineResponse2007.
        :type s: Status
        """
        if s is None:
            raise ValueError("Invalid value for `s`, must not be `None`")  # noqa: E501

        self._s = s

    @property
    def errmsg(self) -> str:
        """Gets the errmsg of this InlineResponse2007.


        :return: The errmsg of this InlineResponse2007.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg: str):
        """Sets the errmsg of this InlineResponse2007.


        :param errmsg: The errmsg of this InlineResponse2007.
        :type errmsg: str
        """

        self._errmsg = errmsg
