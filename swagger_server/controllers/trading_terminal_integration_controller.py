import connexion
import six

from swagger_server.models.bars_arrays import BarsArrays  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from swagger_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server.models.inline_response20013 import InlineResponse20013  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from swagger_server.models.marks_arrays import MarksArrays  # noqa: E501
from swagger_server.models.symbol_info_arrays import SymbolInfoArrays  # noqa: E501
from swagger_server.models.timescale_mark import TimescaleMark  # noqa: E501
from swagger_server import util


def accounts_account_id_executions_get(accountId, instrument, maxCount=None):  # noqa: E501
    """accounts_account_id_executions_get

    Get a list of executions (i.e. fills or trades) for an account and an instrument. Executions are displayed on a chart. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param instrument: Broker instrument name.
    :type instrument: str
    :param maxCount: Maximum count of executions to return.
    :type maxCount: 

    :rtype: InlineResponse20010
    """
    return 'do some magic!'


def accounts_account_id_instruments_get(accountId):  # noqa: E501
    """accounts_account_id_instruments_get

    Get a list of tradeable instruments that are available for trading with the account specified. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str

    :rtype: InlineResponse20011
    """
    return 'do some magic!'


def accounts_account_id_orders_get(accountId):  # noqa: E501
    """accounts_account_id_orders_get

    Get pending orders for an account. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str

    :rtype: InlineResponse2004
    """
    return 'do some magic orderss GET (terminal)!'


def accounts_account_id_orders_history_get(accountId, maxCount=None):  # noqa: E501
    """accounts_account_id_orders_history_get

    Get order history for an account. It is expected that returned orders will have a final status (rejected, filled, cancelled). This request is optional. If you don&#39;t support history of orders set &#x60;AccountFlags::supportOrdersHistory&#x60; to &#x60;false&#x60;. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param maxCount: Maximum amount of orders to return.
    :type maxCount: 

    :rtype: InlineResponse2004
    """
    return 'do some magic!'


def accounts_account_id_orders_order_id_delete(accountId, orderId):  # noqa: E501
    """accounts_account_id_orders_order_id_delete

    Cancel an existing order. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param orderId: Order ID.
    :type orderId: str

    :rtype: InlineResponse2007
    """
    return 'do some magic!'


def accounts_account_id_orders_order_id_get(accountId, orderId):  # noqa: E501
    """accounts_account_id_orders_order_id_get

    Get an order for an account. It can be an active or historical order. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param orderId: Order ID.
    :type orderId: str

    :rtype: InlineResponse2006
    """
    return 'do some magic!'


def accounts_account_id_orders_order_id_put(accountId, orderId, qty, limitPrice=None, stopPrice=None, stopLoss=None, takeProfit=None, digitalSignature=None):  # noqa: E501
    """accounts_account_id_orders_order_id_put

    Modify an existing order. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param orderId: Order ID.
    :type orderId: str
    :param qty: Number of units.
    :type qty: 
    :param limitPrice: Limit Price for Limit or StopLimit order.
    :type limitPrice: 
    :param stopPrice: Stop Price for Stop or StopLimit order.
    :type stopPrice: 
    :param stopLoss: StopLoss price (if supported).
    :type stopLoss: 
    :param takeProfit: TakeProfit price (if supported).
    :type takeProfit: 
    :param digitalSignature: Digital signature (if supported).
    :type digitalSignature: str

    :rtype: InlineResponse2007
    """
    return 'do some magic!'


def accounts_account_id_orders_post(accountId, instrument, qty, side, type, limitPrice=None, stopPrice=None, durationType=None, durationDateTime=None, stopLoss=None, takeProfit=None, digitalSignature=None, requestId=None):  # noqa: E501
    """accounts_account_id_orders_post

    Create a new order. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param instrument: Instrument to open the order on.
    :type instrument: str
    :param qty: The number of units to open order for.
    :type qty: 
    :param side: Side. Possible values &amp;ndash; &#x60;buy&#x60; and &#x60;sell&#x60;.
    :type side: str
    :param type: Type. Possible values &amp;ndash; &#x60;market&#x60;, &#x60;stop&#x60;, &#x60;limit&#x60;, &#x60;stoplimit&#x60;.
    :type type: str
    :param limitPrice: Limit Price for Limit or StopLimit order.
    :type limitPrice: 
    :param stopPrice: Stop Price for Stop or StopLimit order.
    :type stopPrice: 
    :param durationType: Duration ID (if supported).
    :type durationType: str
    :param durationDateTime: Expiration datetime UNIX timestamp (if supported by duration type).
    :type durationDateTime: 
    :param stopLoss: StopLoss price (if supported).
    :type stopLoss: 
    :param takeProfit: TakeProfit price (if supported).
    :type takeProfit: 
    :param digitalSignature: Digital signature (if supported).
    :type digitalSignature: str
    :param requestId: Unique identifier for a request.
    :type requestId: str

    :rtype: InlineResponse2005
    """
    return 'do some magic!'


def accounts_account_id_positions_get(accountId):  # noqa: E501
    """accounts_account_id_positions_get

    Get positions for an account. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str

    :rtype: InlineResponse2008
    """
    return 'do some magic!'


def accounts_account_id_positions_position_id_delete(accountId, positionId):  # noqa: E501
    """accounts_account_id_positions_position_id_delete

    Close an existing position. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param positionId: Position ID.
    :type positionId: str

    :rtype: InlineResponse2007
    """
    return 'do some magic!'


def accounts_account_id_positions_position_id_get(accountId, positionId):  # noqa: E501
    """accounts_account_id_positions_position_id_get

    Get a position for an account. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param positionId: Position ID.
    :type positionId: str

    :rtype: InlineResponse2009
    """
    return 'do some magic!'


def accounts_account_id_positions_position_id_put(accountId, positionId, stopLoss=None, takeProfit=None):  # noqa: E501
    """accounts_account_id_positions_position_id_put

    Modify an existing position stop loss or take profit or both. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param positionId: Position ID.
    :type positionId: str
    :param stopLoss: StopLoss price.
    :type stopLoss: 
    :param takeProfit: TakeProfit price.
    :type takeProfit: 

    :rtype: InlineResponse2007
    """
    return 'do some magic!'


def accounts_account_id_state_get(accountId, locale):  # noqa: E501
    """accounts_account_id_state_get

    Get account information. # noqa: E501

    :param accountId: The account identifier.
    :type accountId: str
    :param locale: Locale (language) id.
    :type locale: str

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def accounts_get():  # noqa: E501
    """accounts_get

    Get a list of accounts owned by the user. # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def config_get(locale):  # noqa: E501
    """config_get

    Get localized configuration. # noqa: E501

    :param locale: Locale (language) id.
    :type locale: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def depth_get(symbol):  # noqa: E501
    """depth_get

    Get current depth of market for the instrument. Optional. # noqa: E501

    :param symbol: Instrument name.
    :type symbol: str

    :rtype: InlineResponse20013
    """
    return 'do some magic!'


def history_get(symbol, resolution, _from, to, countback=None):  # noqa: E501
    """history_get

    Bars request. You can find examples in the [documentation](https://github.com/tradingview/charting_library/wiki/UDF#bars). # noqa: E501

    :param symbol: Symbol name or ticker.
    :type symbol: str
    :param resolution: Symbol resolution. Possible resolutions are daily (&#x60;1D&#x60;, &#x60;2D&#x60; ... ), weekly (&#x60;1W&#x60;, &#x60;2W&#x60; ...), monthly (&#x60;1M&#x60;, &#x60;2M&#x60;...) and an intra-day resolution &amp;ndash; minutes(&#x60;1&#x60;, &#x60;2&#x60; ...).
    :type resolution: str
    :param _from: Unix timestamp (UTC) of the leftmost required bar, including &#x60;from&#x60;.
    :type _from: 
    :param to: Unix timestamp (UTC) of the rightmost required bar, including &#x60;to&#x60;.
    :type to: 
    :param countback: Number of bars (higher priority than &#x60;from&#x60;) starting with &#x60;to&#x60;. If &#x60;countback&#x60; is set, &#x60;from&#x60; should be ignorred. It is used only by tradingview.com, Trading Terminal will never use it.
    :type countback: 

    :rtype: BarsArrays
    """
    return 'do some magic!'


def marks_get(symbol, resolution, _from, to):  # noqa: E501
    """marks_get

    Request for bar marks (circles on top of bars). You can display custom marks only in the Trading Terminal. # noqa: E501

    :param symbol: Symbol name or ticker.
    :type symbol: str
    :param resolution: Symbol resolution. Possible resolutions are daily (&#x60;1D&#x60;, &#x60;2D&#x60; ... ), weekly (&#x60;1W&#x60;, &#x60;2W&#x60; ...), monthly (&#x60;1M&#x60;, &#x60;2M&#x60;...) and an intra-day resolution &amp;ndash; minutes(&#x60;1&#x60;, &#x60;2&#x60; ...).
    :type resolution: str
    :param _from: Unix timestamp (UTC) of the leftmost required bar, including &#x60;from&#x60;.
    :type _from: 
    :param to: Unix timestamp (UTC) of the rightmost required bar, including &#x60;to&#x60;.
    :type to: 

    :rtype: MarksArrays
    """
    return 'do some magic!'


def quotes_get(symbols):  # noqa: E501
    """quotes_get

    Get current prices of the instrument. You can see an example of this response [here](https://demo_feed.tradingview.com/quotes?symbols&#x3D;AAPL%2CMSFT%2CIBM%2CNasdaqNM%3AAAPL). # noqa: E501

    :param symbols: Comma separated symbols.
    :type symbols: str

    :rtype: InlineResponse20012
    """
    return 'do some magic!'


def symbol_info_get():  # noqa: E501
    """symbol_info_get

    Get a list of all instruments. # noqa: E501


    :rtype: SymbolInfoArrays
    """
    return 'do some magic!'


def timescale_marks_get(symbol, resolution, _from, to):  # noqa: E501
    """timescale_marks_get

    Request for timescale marks (circles on the timescale). You can display custom marks only in the Trading Terminal. # noqa: E501

    :param symbol: Symbol name or ticker.
    :type symbol: str
    :param resolution: Symbol resolution. Possible resolutions are daily (&#x60;1D&#x60;, &#x60;2D&#x60; ... ), weekly (&#x60;1W&#x60;, &#x60;2W&#x60; ...), monthly (&#x60;1M&#x60;, &#x60;2M&#x60;...) and an intra-day resolution &amp;ndash; minutes(&#x60;1&#x60;, &#x60;2&#x60; ...).
    :type resolution: str
    :param _from: Unix timestamp (UTC) of the leftmost required bar, including &#x60;from&#x60;.
    :type _from: 
    :param to: Unix timestamp (UTC) of the rightmost required bar, including &#x60;to&#x60;.
    :type to: 

    :rtype: List[TimescaleMark]
    """
    return 'do some magic!'
