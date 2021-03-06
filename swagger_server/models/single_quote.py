# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SingleQuote(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ch: float=None, chp: float=None, lp: float=None, ask: float=None, bid: float=None, open_price: float=None, high_price: float=None, low_price: float=None, prev_close_price: float=None, volume: float=None):  # noqa: E501
        """SingleQuote - a model defined in Swagger

        :param ch: The ch of this SingleQuote.  # noqa: E501
        :type ch: float
        :param chp: The chp of this SingleQuote.  # noqa: E501
        :type chp: float
        :param lp: The lp of this SingleQuote.  # noqa: E501
        :type lp: float
        :param ask: The ask of this SingleQuote.  # noqa: E501
        :type ask: float
        :param bid: The bid of this SingleQuote.  # noqa: E501
        :type bid: float
        :param open_price: The open_price of this SingleQuote.  # noqa: E501
        :type open_price: float
        :param high_price: The high_price of this SingleQuote.  # noqa: E501
        :type high_price: float
        :param low_price: The low_price of this SingleQuote.  # noqa: E501
        :type low_price: float
        :param prev_close_price: The prev_close_price of this SingleQuote.  # noqa: E501
        :type prev_close_price: float
        :param volume: The volume of this SingleQuote.  # noqa: E501
        :type volume: float
        """
        self.swagger_types = {
            'ch': float,
            'chp': float,
            'lp': float,
            'ask': float,
            'bid': float,
            'open_price': float,
            'high_price': float,
            'low_price': float,
            'prev_close_price': float,
            'volume': float
        }

        self.attribute_map = {
            'ch': 'ch',
            'chp': 'chp',
            'lp': 'lp',
            'ask': 'ask',
            'bid': 'bid',
            'open_price': 'open_price',
            'high_price': 'high_price',
            'low_price': 'low_price',
            'prev_close_price': 'prev_close_price',
            'volume': 'volume'
        }

        self._ch = ch
        self._chp = chp
        self._lp = lp
        self._ask = ask
        self._bid = bid
        self._open_price = open_price
        self._high_price = high_price
        self._low_price = low_price
        self._prev_close_price = prev_close_price
        self._volume = volume

    @classmethod
    def from_dict(cls, dikt) -> 'SingleQuote':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SingleQuote of this SingleQuote.  # noqa: E501
        :rtype: SingleQuote
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ch(self) -> float:
        """Gets the ch of this SingleQuote.

        Change (displayed in Watch and Detail).  # noqa: E501

        :return: The ch of this SingleQuote.
        :rtype: float
        """
        return self._ch

    @ch.setter
    def ch(self, ch: float):
        """Sets the ch of this SingleQuote.

        Change (displayed in Watch and Detail).  # noqa: E501

        :param ch: The ch of this SingleQuote.
        :type ch: float
        """

        self._ch = ch

    @property
    def chp(self) -> float:
        """Gets the chp of this SingleQuote.

        Change percent (displayed in Watch and Detail).  # noqa: E501

        :return: The chp of this SingleQuote.
        :rtype: float
        """
        return self._chp

    @chp.setter
    def chp(self, chp: float):
        """Sets the chp of this SingleQuote.

        Change percent (displayed in Watch and Detail).  # noqa: E501

        :param chp: The chp of this SingleQuote.
        :type chp: float
        """

        self._chp = chp

    @property
    def lp(self) -> float:
        """Gets the lp of this SingleQuote.

        Last price.  # noqa: E501

        :return: The lp of this SingleQuote.
        :rtype: float
        """
        return self._lp

    @lp.setter
    def lp(self, lp: float):
        """Sets the lp of this SingleQuote.

        Last price.  # noqa: E501

        :param lp: The lp of this SingleQuote.
        :type lp: float
        """

        self._lp = lp

    @property
    def ask(self) -> float:
        """Gets the ask of this SingleQuote.

        Ask price.  # noqa: E501

        :return: The ask of this SingleQuote.
        :rtype: float
        """
        return self._ask

    @ask.setter
    def ask(self, ask: float):
        """Sets the ask of this SingleQuote.

        Ask price.  # noqa: E501

        :param ask: The ask of this SingleQuote.
        :type ask: float
        """

        self._ask = ask

    @property
    def bid(self) -> float:
        """Gets the bid of this SingleQuote.

        Bid price.  # noqa: E501

        :return: The bid of this SingleQuote.
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid: float):
        """Sets the bid of this SingleQuote.

        Bid price.  # noqa: E501

        :param bid: The bid of this SingleQuote.
        :type bid: float
        """

        self._bid = bid

    @property
    def open_price(self) -> float:
        """Gets the open_price of this SingleQuote.

        Open.  # noqa: E501

        :return: The open_price of this SingleQuote.
        :rtype: float
        """
        return self._open_price

    @open_price.setter
    def open_price(self, open_price: float):
        """Sets the open_price of this SingleQuote.

        Open.  # noqa: E501

        :param open_price: The open_price of this SingleQuote.
        :type open_price: float
        """

        self._open_price = open_price

    @property
    def high_price(self) -> float:
        """Gets the high_price of this SingleQuote.

        High price.  # noqa: E501

        :return: The high_price of this SingleQuote.
        :rtype: float
        """
        return self._high_price

    @high_price.setter
    def high_price(self, high_price: float):
        """Sets the high_price of this SingleQuote.

        High price.  # noqa: E501

        :param high_price: The high_price of this SingleQuote.
        :type high_price: float
        """

        self._high_price = high_price

    @property
    def low_price(self) -> float:
        """Gets the low_price of this SingleQuote.

        Low price.  # noqa: E501

        :return: The low_price of this SingleQuote.
        :rtype: float
        """
        return self._low_price

    @low_price.setter
    def low_price(self, low_price: float):
        """Sets the low_price of this SingleQuote.

        Low price.  # noqa: E501

        :param low_price: The low_price of this SingleQuote.
        :type low_price: float
        """

        self._low_price = low_price

    @property
    def prev_close_price(self) -> float:
        """Gets the prev_close_price of this SingleQuote.

        Previous close price.  # noqa: E501

        :return: The prev_close_price of this SingleQuote.
        :rtype: float
        """
        return self._prev_close_price

    @prev_close_price.setter
    def prev_close_price(self, prev_close_price: float):
        """Sets the prev_close_price of this SingleQuote.

        Previous close price.  # noqa: E501

        :param prev_close_price: The prev_close_price of this SingleQuote.
        :type prev_close_price: float
        """

        self._prev_close_price = prev_close_price

    @property
    def volume(self) -> float:
        """Gets the volume of this SingleQuote.

        Volume.  # noqa: E501

        :return: The volume of this SingleQuote.
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume: float):
        """Sets the volume of this SingleQuote.

        Volume.  # noqa: E501

        :param volume: The volume of this SingleQuote.
        :type volume: float
        """

        self._volume = volume
