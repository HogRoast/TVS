from swagger_server.gateways.base_gateway import established, InvalidSessionError, InvalidAccountError, AccountPermissionError, OrderValidationError
import configparser


class TestGwy:
    terminalOrderStates = ('rejected', 'filled', 'cancelled')
    marketSides = ('buy', 'sell')
    orderTypes = ('limit', 'market', 'stop', 'stoplimit')
    durationTypes = ('gtt', 'gtd', 'gtc')

    def __init__(self):
        self.config = configparser.RawConfigParser()
        # overriding optionxform to ensure case sensitivity in config keys
        self.config.optionxform = lambda option : option
        self.config.read('./swagger_server/gateways/test_ex/test_exchange.ini')
        self.server = self.config['connection.details']['server']
        self.accounts = {}
        for account in self.config['account.details']:
            self.accounts[account] = eval(self.config['account.details'][account])
        self.session = None
        self.numberFountains = {    'order'      : 126,
                                    'execution'  : 1226 }

    def getNextId(self, fountain):
        id_ = self.numberFountains[fountain]
        self.numberFountains[fountain] = id_ + 1
        return id_

    def establishSession(self):
        if self.session:
            return

        f = open(self.server, 'r')
        self.session = eval(f.read())
        f.close()

    @established
    def destroySession(self):
        self.session = None

    @established
    def getAllInstruments(self):
        return self.session['instruments']

    @established
    def getPermissions(self, accountId):
        try:
            if accountId in self.accounts:
                return self.session['permissions'][accountId]
        except KeyError:
            pass

        raise InvalidAccountError('Account - ' + accountId + ' - does not exist')

    @established
    def getInstruments(self, accountId):
        allInsts = self.getAllInstruments()
        permInsts = self.getPermissions(accountId)['instruments']
        insts = []
        for inst in permInsts:
            if inst in allInsts:
                insts.append(allInsts[inst])
        return insts

    @established
    def getExchangeInfo(self):
        return self.session['exchange_info']

    @established
    def getExecutions(self, accountId, instrument, maxCount=None):
        exes = []
        cnt = 0
        try:
            userExes = self.session['executions'][accountId]
            for exe in userExes:
                if exe['instrument'] == instrument:
                    exes.append(exe)
                    cnt += 1
                    if maxCount == cnt:
                        break
        except KeyError:
            pass
        return exes

    @established
    def getOrders(self, accountId):
        ords = []
        try:
            userOrds = self.session['orders'][accountId]
            for order in userOrds:
                # only collect those order that are not terminal
                if order['status'] not in TestGwy.terminalOrderStates:
                    ords.append(order)
        except KeyError:
            pass
        return ords

    @established
    def getOrder(self, accountId, orderId):
        try:
            userOrds = self.session['orders'][accountId]
            for order in userOrds:
                if order['id'] == orderId:
                    return order
        except KeyError:
            pass
        return None

    @established
    def getHistoricalOrders(self, accountId, maxCount=None):
        ords = []
        cnt = 0
        try:
            userOrds = self.session['orders'][accountId]
            for order in userOrds:
                print(order['status'])
                if order['status'] in TestGwy.terminalOrderStates:
                    ords.append(order)
                    cnt += 1
                    if maxCount == cnt:
                        break
        except KeyError:
            pass
        return ords

    @established
    def cancelOrder(self, accountId, orderId):
        ords = self.getOrders(accountId)
        for order in ords:
            if order['id'] == orderId:
                order['status'] = 'cancelled'
                return True
        return False

    @established
    def modifyOrder(self, accountId, orderId, qty, limitPrice=None, stopPrice=None, stopLoss=None, takeProfit=None, digitalSignature=None):
        # NOTE: digitialSignature, stopLoss and takeProfit are odd, as they
        # are not supported by the swagger Order class, leaving them here as 
        # optional params but will ignore for now.
        # Also, stopLoss and takeProfit are not obvious parameters for a 
        # single order in any case, so not quite sure what the aim was.
        ords = self.getOrders(accountId)
        for order in ords:
            if order['id'] == orderId:
                order['qty'] = qty;
                if limitPrice is not None: 
                    order['limit_price'] = limitPrice
                if stopPrice is not None: 
                    order['stop_price'] = stopPrice
                return True
        return False

    @established
    def createOrder(self, accountId, instrument, qty, side, type_, limitPrice=None, stopPrice=None, durationType=None, durationDateTime=None, stopLoss=None, takeProfit=None, digitalSignature=None, requestId=None):
        # See comment above regarding digitialSignature, stopLoss and takeProfit
        # Also, ignoring requestId for now.
        perms = self.getPermissions(accountId)
        if instrument not in perms['instruments']:
            raise AccountPermissionError('Account - ' + accountId + ' - is not permissioned for instrument: ' + instrument)

        order = {}
        order['id'] = str(self.getNextId('order'))
        order['instrument'] = instrument
        order['qty'] = qty
        order['side'] = side
        order['type'] = type_
        order['filled_qty'] = 0.0
        order['avg_price'] = None
        order['limit_price'] = limitPrice
        order['stop_price'] = stopPrice
        order['parent_id'] = None
        order['parent_type'] = None
        order['duration_type'] = durationType
        order['duration_datetime'] = durationDateTime
        order['status'] = 'placing'
        self.validateOrder(order)

        orders = []
        try:
            orders = self.session['orders'][accountId]
        except KeyError:
            self.session['orders'][accountId] = orders
        orders.append(order)
        return order['id']

    def validateOrder(self, order):
        if 'id' not in order:
            raise OrderValidationError('Order missing "id" field')
        if 'instrument' not in order:
            raise OrderValidationError('Order - ' + order['id'] + ' - missing "instrument" field')
        if 'qty' not in order:
            raise OrderValidationError('Order - ' + order['id'] + ' - missing "qty" field')
        if 'side' not in order:
            raise OrderValidationError('Order - ' + order['id'] + ' - missing "side" field')
        if 'type' not in order:
            raise OrderValidationError('Order - ' + order['id'] + ' - missing "type" field')
        if 'limit_price' not in order:
            raise OrderValidationError('Order - ' + order['id'] + ' - missing "limit_price" field')

        if order['instrument'] not in self.getAllInstruments():
            raise OrderValidationError('Order - ' + order['id'] + ' - has invalid "instrument": ' + order['instrument'])
        if order['qty'] <= 0.0:
            raise OrderValidationError('Order - ' + order['id'] + ' - has invalid "qty": ' + str(order['qty']))
        if order['side'] not in TestGwy.marketSides:
            raise OrderValidationError('Order - ' + order['id'] + ' - has invalid "side": ' + order['side'])
        if order['type'] not in TestGwy.orderTypes:
            raise OrderValidationError('Order - ' + order['id'] + ' - has invalid "type": ' + order['type'])

