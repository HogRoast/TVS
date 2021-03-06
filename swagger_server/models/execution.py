# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Execution(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, instrument: str=None, price: float=None, time: float=None, qty: float=None, side: str=None):  # noqa: E501
        """Execution - a model defined in Swagger

        :param id: The id of this Execution.  # noqa: E501
        :type id: str
        :param instrument: The instrument of this Execution.  # noqa: E501
        :type instrument: str
        :param price: The price of this Execution.  # noqa: E501
        :type price: float
        :param time: The time of this Execution.  # noqa: E501
        :type time: float
        :param qty: The qty of this Execution.  # noqa: E501
        :type qty: float
        :param side: The side of this Execution.  # noqa: E501
        :type side: str
        """
        self.swagger_types = {
            'id': str,
            'instrument': str,
            'price': float,
            'time': float,
            'qty': float,
            'side': str
        }

        self.attribute_map = {
            'id': 'id',
            'instrument': 'instrument',
            'price': 'price',
            'time': 'time',
            'qty': 'qty',
            'side': 'side'
        }

        self._id = id
        self._instrument = instrument
        self._price = price
        self._time = time
        self._qty = qty
        self._side = side

    @classmethod
    def from_dict(cls, dikt) -> 'Execution':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Execution of this Execution.  # noqa: E501
        :rtype: Execution
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Execution.

        Unique identifier.  # noqa: E501

        :return: The id of this Execution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Execution.

        Unique identifier.  # noqa: E501

        :param id: The id of this Execution.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instrument(self) -> str:
        """Gets the instrument of this Execution.

        Instrument id.  # noqa: E501

        :return: The instrument of this Execution.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument: str):
        """Sets the instrument of this Execution.

        Instrument id.  # noqa: E501

        :param instrument: The instrument of this Execution.
        :type instrument: str
        """
        if instrument is None:
            raise ValueError("Invalid value for `instrument`, must not be `None`")  # noqa: E501

        self._instrument = instrument

    @property
    def price(self) -> float:
        """Gets the price of this Execution.

        Execution price.  # noqa: E501

        :return: The price of this Execution.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """Sets the price of this Execution.

        Execution price.  # noqa: E501

        :param price: The price of this Execution.
        :type price: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def time(self) -> float:
        """Gets the time of this Execution.

        Execution time.  # noqa: E501

        :return: The time of this Execution.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time: float):
        """Sets the time of this Execution.

        Execution time.  # noqa: E501

        :param time: The time of this Execution.
        :type time: float
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def qty(self) -> float:
        """Gets the qty of this Execution.

        Execution quantity.  # noqa: E501

        :return: The qty of this Execution.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty: float):
        """Sets the qty of this Execution.

        Execution quantity.  # noqa: E501

        :param qty: The qty of this Execution.
        :type qty: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def side(self) -> str:
        """Gets the side of this Execution.

        Side. Possible values &ndash; \"buy\" and \"sell\".  # noqa: E501

        :return: The side of this Execution.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side: str):
        """Sets the side of this Execution.

        Side. Possible values &ndash; \"buy\" and \"sell\".  # noqa: E501

        :param side: The side of this Execution.
        :type side: str
        """
        allowed_values = ["buy", "sell"]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"
                .format(side, allowed_values)
            )

        self._side = side
