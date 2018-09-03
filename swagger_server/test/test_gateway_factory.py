from swagger_server.gateways.gateway_factory import getGateway, NoSuchEcnError, getAllGateways
from swagger_server.gateways.binance import BinanceGwy
from swagger_server.gateways.test_exchange import TestGwy
from swagger_server.test import BaseTestCase

class TestGatewayFactory(BaseTestCase):
    def test_getGateway(self):
        x = getGateway('Binance')
        self.assertTrue(isinstance(x, BinanceGwy))

    def test_getGateway_NoSuchECN(self):
        with self.assertRaises(NoSuchEcnError) as cm:
            getGateway('Nonsense')
        self.assertEqual(cm.exception.message, 'No such gateway for ecn : Nonsense')

    def test_getGateway_SameInstance(self):
        x = getGateway('Binance')
        y = getGateway('Binance')
        self.assertIs(x, y)

    def test_getAllGateways(self):
        gwys = getAllGateways()
        self.assertEqual(len(gwys), 2)
        self.assertTrue(isinstance(gwys[0], BinanceGwy))
        self.assertTrue(isinstance(gwys[1], TestGwy))


if __name__ == '__main__':
    import unittest
    unittest.main()
