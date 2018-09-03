import configparser

class BinanceGwy:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        # overriding optionxform to ensure case sensitivity in config keys
        self.config.optionxform = lambda option : option
        self.config.read('./swagger_server/gateways/binance.ini')
        self.server = self.config['connection.details']['server']
        self.accounts = {}
        for account in self.config['account.details']:
            self.accounts[account] = eval(self.config['account.details'][account])
