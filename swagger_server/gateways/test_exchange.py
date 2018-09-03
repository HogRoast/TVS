import configparser

class InvalidSessionError(Exception):
    def __init__(self, msg):
        self.msg = msg

# decorator to ensure applicable methods have a valid session when called
def connected(fn):
    def wrapper(*args, **kwargs):
        if args[0].session:
            return fn(*args, **kwargs)
        raise InvalidSessionError('Not connected')
    return wrapper

class TestGwy:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        # overriding optionxform to ensure case sensitivity in config keys
        self.config.optionxform = lambda option : option
        self.config.read('./swagger_server/gateways/test_exchange.ini')
        self.server = self.config['connection.details']['server']
        self.accounts = {}
        for account in self.config['account.details']:
            self.accounts[account] = eval(self.config['account.details'][account])
        self.session = None

    def connect(self):
        if self.session:
            return

        f = open(self.server, 'r')
        self.session = eval(f.read())
        f.close()

    @connected
    def disconnect(self):
        self.session = None

    @connected
    def getAllInstruments(self):
        return self.session['instruments']

    @connected
    def getPermissions(self, accountId):
        return self.session['permissions'][accountId]

    @connected
    def getInstruments(self, accountId):
        allInsts = self.getAllInstruments()
        permInsts = self.getPermissions(accountId)['instruments']
        insts = []
        for inst in allInsts:
            if inst['name'] in permInsts:
                insts.append(inst)
                # break out early if we have all the permed insts already
                if len(insts) == len(permInsts):
                    return insts
        return insts

    @connected
    def getExchangeInfo(self):
        return self.session['exchange_info']

