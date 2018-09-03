from swagger_server.gateways.binance import BinanceGwy
from swagger_server.gateways.test_exchange import TestGwy

# Map contains ecn keys with a value that is a list of gateway class and
# gateway instance. The instance is None to begin with and is created on
# first call to getGateway for the specific ecn. Subsequent calls to getGateway
# return the same instance.
ecnMap =    { 
                'Binance'   : [BinanceGwy, None],
                'Test'      : [TestGwy, None] 
            }

class NoSuchEcnError(Exception):
    def __init__(self, message):
        self.message = message

def getGateway(ecn):
    if ecn in ecnMap.keys():
        if ecnMap[ecn][1] is None:
            ecnMap[ecn][1] = ecnMap[ecn][0]();
        return ecnMap[ecn][1]
    raise NoSuchEcnError('No such gateway for ecn : ' + ecn)

def getAllGateways():
    gwys = []
    for ecn in ecnMap.keys():
        gwys.append(getGateway(ecn))
    return gwys

