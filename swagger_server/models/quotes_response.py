# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.single_quote import SingleQuote  # noqa: F401,E501
from swagger_server.models.status import Status  # noqa: F401,E501
from swagger_server import util


class QuotesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, s: Status=None, n: str=None, v: SingleQuote=None):  # noqa: E501
        """QuotesResponse - a model defined in Swagger

        :param s: The s of this QuotesResponse.  # noqa: E501
        :type s: Status
        :param n: The n of this QuotesResponse.  # noqa: E501
        :type n: str
        :param v: The v of this QuotesResponse.  # noqa: E501
        :type v: SingleQuote
        """
        self.swagger_types = {
            's': Status,
            'n': str,
            'v': SingleQuote
        }

        self.attribute_map = {
            's': 's',
            'n': 'n',
            'v': 'v'
        }

        self._s = s
        self._n = n
        self._v = v

    @classmethod
    def from_dict(cls, dikt) -> 'QuotesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QuotesResponse of this QuotesResponse.  # noqa: E501
        :rtype: QuotesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s(self) -> Status:
        """Gets the s of this QuotesResponse.


        :return: The s of this QuotesResponse.
        :rtype: Status
        """
        return self._s

    @s.setter
    def s(self, s: Status):
        """Sets the s of this QuotesResponse.


        :param s: The s of this QuotesResponse.
        :type s: Status
        """
        if s is None:
            raise ValueError("Invalid value for `s`, must not be `None`")  # noqa: E501

        self._s = s

    @property
    def n(self) -> str:
        """Gets the n of this QuotesResponse.

        Symbol name. Should be equal to the requested one.  # noqa: E501

        :return: The n of this QuotesResponse.
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n: str):
        """Sets the n of this QuotesResponse.

        Symbol name. Should be equal to the requested one.  # noqa: E501

        :param n: The n of this QuotesResponse.
        :type n: str
        """
        if n is None:
            raise ValueError("Invalid value for `n`, must not be `None`")  # noqa: E501

        self._n = n

    @property
    def v(self) -> SingleQuote:
        """Gets the v of this QuotesResponse.


        :return: The v of this QuotesResponse.
        :rtype: SingleQuote
        """
        return self._v

    @v.setter
    def v(self, v: SingleQuote):
        """Sets the v of this QuotesResponse.


        :param v: The v of this QuotesResponse.
        :type v: SingleQuote
        """
        if v is None:
            raise ValueError("Invalid value for `v`, must not be `None`")  # noqa: E501

        self._v = v
