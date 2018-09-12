def flipDict(d):
    return dict(zip(d.values(), d.keys()))

tv2b_instName = {   'TestInst1' : 'LTCBTC',
                    'TestInst2' : 'BTCUSDT' }
b2tv_instName = flipDict(tv2b_instName)

tv2b_side = {   'buy'   : 'BUY',
                'sell'  : 'SELL' }
b2tv_side = flipDict(tv2b_side)

tv2b_type = {   'limit'     : 'LIMIT',
                'market'    : 'MARKET',
                'stop'      : 'STOP',
                'stoplimit' : 'STOP_LIMIT' }
b2tv_type = flipDict(tv2b_type)

tv2b_tif = { 'gtc' : 'GTC' }
b2tv_tif = flipDict(tv2b_type)

tv2b_orderStatus = {    'rejected'          : 'REJECTED',
                        'filled'            : 'FILLED',
                        'cancelled'         : 'CANCELLED',
                        'new'               : 'NEW',
                        'partially_filled'  : 'PARTIALLY_FILLED',
                        'expired'           : 'EXPIRED' }
b2tb_orderStatus = flipDict(tv2b_orderStatus)

def b2tv_order(o):
    return {    'id'                : o['orderId'],
                'instrument'        : b2tv_instName(o['symbol']),
                'qty'               : o['origQty'],
                'side'              : b2tv_side(o['side']),
                'type'              : b2tv_type(o['type']),
                'filled_qty'        : o['executedQty'],
                'avg_price'         : 0.0,
                'limit_price'       : o['price'],
                'stop_price'        : o['stopPrice'],
                'parent_id'         : None,
                'parent_type'       : None,
                'duration_type'     : b2tv_tif(o['timeInForce']),
                'duration_datetime' : None,
                'status'            : b2tv_orderStatus(o['status']) }

def b2tv_instrument(s):
    i = {}
    i['name'] = 'Binance:' + s['symbol']
    i['description'] = 'Binance crypto currency pair, base asset  ' +s['baseAsset'] + ' vs quote asset ' + s['quoteAsset'] 
    # Not clear to me how you can set the pip value without the rate
    i['pip_value'] = 0.0
    # Also the lot size is questionable
    i['lot_size'] = 0.0
    for f in s['filters']:
        if f['filterType'] == 'PRICE_FILTER':
            i['pip_size'] = float(f['tickSize'])
            i['min_tick'] = float(f['tickSize'])
        if f['filterType'] == 'LOT_SIZE':
            i['min_qty'] = float(f['minQty'])
            i['max_qty'] = float(f['maxQty'])
            i['qty_step'] = float(f['stepSize'])
    return i
