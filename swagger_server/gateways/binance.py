from swagger_server.gateways.base_gateway import established, getMillisecondTimestamp, InvalidSessionError, InvalidAccountError, AccountPermissionError, OrderValidationError
import configparser
import requests
import datetime

class BinanceGwy:
    terminalOrderStates = ('rejected', 'filled', 'cancelled')
    marketSides = ('buy', 'sell')
    validModes = ('trade', 'test')

    def __init__(self):
        self.config = configparser.RawConfigParser()
        # overriding optionxform to ensure case sensitivity in config keys
        self.config.optionxform = lambda option : option
        self.config.read('./swagger_server/gateways/binance.ini')
        connDetails = self.config['connection.details']
        self.server = connDetails['server']
        self.recvWindow = connDetails.getint('recv_window', fallback=3000)
        self.timeout = connDetails.getint('timeout', fallback=3)
        self.mode = connDetails.get('mode', fallback='test')
        if self.mode not in BinanceGwy.validModes:
            self.mode = 'test'

        self.accounts = {}
        for account in self.config['account.details']:
            self.accounts[account] = eval(self.config['account.details'][account])
        self.session = None

    def establishSession(self):
        r = requests.get(self.server + '/api/v1/exchangeInfo', timeout=self.timeout)
        if r.status_code == requests.codes.ok:
            self.session = r.json()
        else:
            raise InvalidSessionError('Could not establish session: ' + r.status_code)

    @established
    def destroySession(self):
        self.session = None

    def convertSymbolToInst(self, s):
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

    @established
    def getAllInstruments(self):
        insts = []
        for s in self.session['symbols']:
            insts.append(self.convertSymbolToInst(s))
        return insts

    @established
    def getInstruments(self, accountId):
        if accountId in self.accounts:
            return self.getAllInstruments()

        raise InvalidAccountError('Account - ' + accountId + ' - does not exist')

    @established
    def createOrder(self, accountId, instrument, qty, side, type_, limitPrice=None, stopPrice=None, durationType=None, durationDateTime=None, stopLoss=None, takeProfit=None, digitalSignature=None, requestId=None):
        url = '/api/v3/order/test'
        if self.mode == 'trade':
            url = '/api/v3/order'

        r = requests.post(self.server + url, timeout=self.timeout,
                data = {'symbol'        : convertInstrument(instrument),
                        'side'          : convertSide(side),
                        'type'          : convertType(type_),
                        'timeInForce'   : convertDurationType(durationType),
                        'quantity'      : qty,
                        'price'         : limitPrice,
                        'stopPrice'     : stopPrice,
                        'recvWindow'    : self.recvWindow,
                        'timestamp'     : getMillisecondTimestamp()
                        })
        if r.status_code == requests.codes.ok:
            pass
