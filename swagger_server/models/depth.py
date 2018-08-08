# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.depth_item import DepthItem  # noqa: F401,E501
from swagger_server import util


class Depth(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, asks: List[DepthItem]=None, bids: List[DepthItem]=None):  # noqa: E501
        """Depth - a model defined in Swagger

        :param asks: The asks of this Depth.  # noqa: E501
        :type asks: List[DepthItem]
        :param bids: The bids of this Depth.  # noqa: E501
        :type bids: List[DepthItem]
        """
        self.swagger_types = {
            'asks': List[DepthItem],
            'bids': List[DepthItem]
        }

        self.attribute_map = {
            'asks': 'asks',
            'bids': 'bids'
        }

        self._asks = asks
        self._bids = bids

    @classmethod
    def from_dict(cls, dikt) -> 'Depth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Depth of this Depth.  # noqa: E501
        :rtype: Depth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asks(self) -> List[DepthItem]:
        """Gets the asks of this Depth.

        Array of Asks.  # noqa: E501

        :return: The asks of this Depth.
        :rtype: List[DepthItem]
        """
        return self._asks

    @asks.setter
    def asks(self, asks: List[DepthItem]):
        """Sets the asks of this Depth.

        Array of Asks.  # noqa: E501

        :param asks: The asks of this Depth.
        :type asks: List[DepthItem]
        """
        if asks is None:
            raise ValueError("Invalid value for `asks`, must not be `None`")  # noqa: E501

        self._asks = asks

    @property
    def bids(self) -> List[DepthItem]:
        """Gets the bids of this Depth.

        Array of Bids.  # noqa: E501

        :return: The bids of this Depth.
        :rtype: List[DepthItem]
        """
        return self._bids

    @bids.setter
    def bids(self, bids: List[DepthItem]):
        """Sets the bids of this Depth.

        Array of Bids.  # noqa: E501

        :param bids: The bids of this Depth.
        :type bids: List[DepthItem]
        """
        if bids is None:
            raise ValueError("Invalid value for `bids`, must not be `None`")  # noqa: E501

        self._bids = bids
