from swagger_server.gateways.base_gateway import * 
import swagger_server.gateways.binance.mapping as BinanceMapping
import configparser
import requests
import datetime
import hmac
import hashlib

class BinanceGwy:
    validModes = ('trade', 'test')

    def __init__(self):
        self.config = configparser.RawConfigParser()
        # overriding optionxform to ensure case sensitivity in config keys
        self.config.optionxform = lambda option : option
        self.config.read('./swagger_server/gateways/binance/binance.ini')
        connDetails = self.config['connection.details']
        self.server = connDetails['server']
        self.recvWindow = connDetails.getint('recv_window', fallback=3000)
        self.timeout = connDetails.getint('timeout', fallback=5)
        self.mode = connDetails.get('mode', fallback='test')
        if self.mode not in BinanceGwy.validModes:
            self.mode = 'test'

        self.accounts = {}
        for account in self.config['account.details']:
            self.accounts[account] = eval(self.config['account.details'][account])
        self.session = None

    def serverRequest(self, request, url, hdrs=None, data=None):
        r = request(
            self.server + url, timeout=self.timeout, headers=hdrs, data=data)

        print('******** SHM ********')
        print(r.url)
        print(r.status_code)
        print(r.text)
        print('******** SHM ********')

        if r.status_code != requests.codes.ok:
            raise ServerRequestError(r.status_code, r.text)
        return r

    def inTestMode(self):
        return self.mode == 'test'

    def establishSession(self):
        try:
            r = self.serverRequest(requests.get,  '/api/v1/exchangeInfo')
            self.session = r.json()
        except ServerRequestError as e:
            raise InvalidSessionError('Could not establish session: ' + e.msg)

    @established
    def destroySession(self):
        self.session = None

    @established
    def getAllInstruments(self):
        insts = []
        for s in self.session['symbols']:
            insts.append(BinanceMapping.b2tv_instrument(s))
        return insts

    @established
    def getInstruments(self, accountId):
        if accountId in self.accounts:
            return self.getAllInstruments()

        raise InvalidAccountError('Account - ' + accountId + ' - does not exist')

    def dictToRequestBody(self, dict_):
        rb = ''
        for (k, v) in dict_.items():
            rb += str(k) + '=' + str(v) + '&'
        return rb[:len(rb)-1]

    def encodeMsg(self, data, signature):
        return hmac.new(
                bytes(signature, 'utf-8'), msg=bytes(data, 'utf-8'), 
                digestmod=hashlib.sha256).hexdigest()

    @established
    def createOrder(self, accountId, instrument, qty, side, type_, limitPrice=None, stopPrice=None, durationType=None, durationDateTime=None, stopLoss=None, takeProfit=None, digitalSignature=None, requestId=None):

        if accountId not in self.accounts:
            raise InvalidAccountError('Account - ' + accountId + ' - does not exist')
        apiKey = self.accounts[accountId]['api_key']
        secretKey = self.accounts[accountId]['secret_key']

        url = '/api/v3/order/test'
        # !!!!
        # BEWARE WHEN ENGAGING TRADE MODE! YOU CAN NOW PLACE LIVE ORDERS AT
        # BINANCE
        # !!!!
        if self.mode == 'trade':
            url = '/api/v3/order'

        hdrs = {'X-MBX-APIKEY': apiKey}
        data = {    'symbol'        : BinanceMapping.tv2b_instName[instrument],
                    'side'          : BinanceMapping.tv2b_side[side],
                    'type'          : BinanceMapping.tv2b_type[type_],
                    'timeInForce'   : BinanceMapping.tv2b_tif[durationType],
                    'quantity'      : qty,
                    'price'         : limitPrice,
                    'recvWindow'    : self.recvWindow,
                    'timestamp'     : getMillisecondTimestamp()
               } 
        signature = self.encodeMsg(self.dictToRequestBody(data), secretKey)
        data['signature'] = signature

        r = self.serverRequest(requests.post, url, hdrs, data)

        if self.mode == 'test':
            return 'TEST_ID'

        response = r.json()
        orderId = response['orderId']
        return orderId


    @established
    def getOrders(self, accountId, instrument=None):
        if accountId not in self.accounts:
            raise InvalidAccountError('Account - ' + accountId + ' - does not exist')
        apiKey = self.accounts[accountId]['api_key']
        secretKey = self.accounts[accountId]['secret_key']
        url = '/api/v3/openOrders'

        hdrs = {'X-MBX-APIKEY'  : apiKey}
        data = {'recvWindow'    : self.recvWindow,
                'timestamp'     : getMillisecondTimestamp() }
        if instrument:
            data['symbol'] = BinanceMapping.tv2b_instName(instrument)

        signature = self.encodeMsg(self.dictToRequestBody(data), secretKey)
        data['signature'] = signature

        try:
            r = self.serverRequest(requests.get, url, hdrs, data)
        except ServerRequestError as e:
            # Binance appears to return a 403 if there are no orders available
            if e.errorCode == 403:
                return []
            raise e

        ords = []
        response = r.json()
        for o in response:
            ords.append(BinanceMapping.b2tv_order(o))
        return ords        

    @established
    def getOrder(self, accountId, orderId):
        if accountId not in self.accounts:
            raise InvalidAccountError('Account - ' + accountId + ' - does not exist')
        apiKey = self.accounts[accountId]['api_key']
        secretKey = self.accounts[accountId]['secret_key']
        url = '/api/v3/order'

        hdrs = {'X-MBX-APIKEY'  : apiKey}
        data = {    'symbol'        : BinanceMapping.tv2b_instName(instrument),
                    'orderId'       : orderId,
                    'recvWindow'    : self.recvWindow,
                    'timestamp'     : getMillisecondTimestamp() }
        signature = self.encodeMsg(self.dictToRequestBody(data), secretKey)
        data['signature'] = signature

        r = self.serverRequest(requests.get, url, hdrs, data)

        response = r.json()
        order = BinanceMapping.b2tv_order(response)
        return order        

