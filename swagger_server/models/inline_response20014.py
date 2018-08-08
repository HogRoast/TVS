# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse20014(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, p: float=None, s: float=None, t: float=None, f: str=None, o: float=None, h: float=None, l: float=None, c: float=None, v: float=None):  # noqa: E501
        """InlineResponse20014 - a model defined in Swagger

        :param id: The id of this InlineResponse20014.  # noqa: E501
        :type id: str
        :param p: The p of this InlineResponse20014.  # noqa: E501
        :type p: float
        :param s: The s of this InlineResponse20014.  # noqa: E501
        :type s: float
        :param t: The t of this InlineResponse20014.  # noqa: E501
        :type t: float
        :param f: The f of this InlineResponse20014.  # noqa: E501
        :type f: str
        :param o: The o of this InlineResponse20014.  # noqa: E501
        :type o: float
        :param h: The h of this InlineResponse20014.  # noqa: E501
        :type h: float
        :param l: The l of this InlineResponse20014.  # noqa: E501
        :type l: float
        :param c: The c of this InlineResponse20014.  # noqa: E501
        :type c: float
        :param v: The v of this InlineResponse20014.  # noqa: E501
        :type v: float
        """
        self.swagger_types = {
            'id': str,
            'p': float,
            's': float,
            't': float,
            'f': str,
            'o': float,
            'h': float,
            'l': float,
            'c': float,
            'v': float
        }

        self.attribute_map = {
            'id': 'id',
            'p': 'p',
            's': 's',
            't': 't',
            'f': 'f',
            'o': 'o',
            'h': 'h',
            'l': 'l',
            'c': 'c',
            'v': 'v'
        }

        self._id = id
        self._p = p
        self._s = s
        self._t = t
        self._f = f
        self._o = o
        self._h = h
        self._l = l
        self._c = c
        self._v = v

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20014':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_14 of this InlineResponse20014.  # noqa: E501
        :rtype: InlineResponse20014
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this InlineResponse20014.

        Symbol.  # noqa: E501

        :return: The id of this InlineResponse20014.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InlineResponse20014.

        Symbol.  # noqa: E501

        :param id: The id of this InlineResponse20014.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def p(self) -> float:
        """Gets the p of this InlineResponse20014.

        Price.  # noqa: E501

        :return: The p of this InlineResponse20014.
        :rtype: float
        """
        return self._p

    @p.setter
    def p(self, p: float):
        """Sets the p of this InlineResponse20014.

        Price.  # noqa: E501

        :param p: The p of this InlineResponse20014.
        :type p: float
        """

        self._p = p

    @property
    def s(self) -> float:
        """Gets the s of this InlineResponse20014.

        Size.  # noqa: E501

        :return: The s of this InlineResponse20014.
        :rtype: float
        """
        return self._s

    @s.setter
    def s(self, s: float):
        """Sets the s of this InlineResponse20014.

        Size.  # noqa: E501

        :param s: The s of this InlineResponse20014.
        :type s: float
        """

        self._s = s

    @property
    def t(self) -> float:
        """Gets the t of this InlineResponse20014.

        Time.  # noqa: E501

        :return: The t of this InlineResponse20014.
        :rtype: float
        """
        return self._t

    @t.setter
    def t(self, t: float):
        """Sets the t of this InlineResponse20014.

        Time.  # noqa: E501

        :param t: The t of this InlineResponse20014.
        :type t: float
        """
        if t is None:
            raise ValueError("Invalid value for `t`, must not be `None`")  # noqa: E501

        self._t = t

    @property
    def f(self) -> str:
        """Gets the f of this InlineResponse20014.

        Type (a - ask, b - bid, t - trade, d - daily bar). Default value is `t` (trade).  # noqa: E501

        :return: The f of this InlineResponse20014.
        :rtype: str
        """
        return self._f

    @f.setter
    def f(self, f: str):
        """Sets the f of this InlineResponse20014.

        Type (a - ask, b - bid, t - trade, d - daily bar). Default value is `t` (trade).  # noqa: E501

        :param f: The f of this InlineResponse20014.
        :type f: str
        """
        allowed_values = ["a", "b", "d", "t"]  # noqa: E501
        if f not in allowed_values:
            raise ValueError(
                "Invalid value for `f` ({0}), must be one of {1}"
                .format(f, allowed_values)
            )

        self._f = f

    @property
    def o(self) -> float:
        """Gets the o of this InlineResponse20014.

        Open.  # noqa: E501

        :return: The o of this InlineResponse20014.
        :rtype: float
        """
        return self._o

    @o.setter
    def o(self, o: float):
        """Sets the o of this InlineResponse20014.

        Open.  # noqa: E501

        :param o: The o of this InlineResponse20014.
        :type o: float
        """

        self._o = o

    @property
    def h(self) -> float:
        """Gets the h of this InlineResponse20014.

        High.  # noqa: E501

        :return: The h of this InlineResponse20014.
        :rtype: float
        """
        return self._h

    @h.setter
    def h(self, h: float):
        """Sets the h of this InlineResponse20014.

        High.  # noqa: E501

        :param h: The h of this InlineResponse20014.
        :type h: float
        """

        self._h = h

    @property
    def l(self) -> float:
        """Gets the l of this InlineResponse20014.

        Low.  # noqa: E501

        :return: The l of this InlineResponse20014.
        :rtype: float
        """
        return self._l

    @l.setter
    def l(self, l: float):
        """Sets the l of this InlineResponse20014.

        Low.  # noqa: E501

        :param l: The l of this InlineResponse20014.
        :type l: float
        """

        self._l = l

    @property
    def c(self) -> float:
        """Gets the c of this InlineResponse20014.

        Close.  # noqa: E501

        :return: The c of this InlineResponse20014.
        :rtype: float
        """
        return self._c

    @c.setter
    def c(self, c: float):
        """Sets the c of this InlineResponse20014.

        Close.  # noqa: E501

        :param c: The c of this InlineResponse20014.
        :type c: float
        """

        self._c = c

    @property
    def v(self) -> float:
        """Gets the v of this InlineResponse20014.

        Volume.  # noqa: E501

        :return: The v of this InlineResponse20014.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v: float):
        """Sets the v of this InlineResponse20014.

        Volume.  # noqa: E501

        :param v: The v of this InlineResponse20014.
        :type v: float
        """

        self._v = v
