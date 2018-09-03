from swagger_server.gateways.gateway_factory import getGateway, NoSuchEcnError
from swagger_server.gateways.binance import BinanceGwy
from swagger_server.test import BaseTestCase

class TestGatewayFactory(BaseTestCase):
    def test_getGateway(self):
        x = getGateway('Binance')
        self.assertTrue(isinstance(x, BinanceGwy))

    def test_getGateway_NoSuchECN(self):
        with self.assertRaises(NoSuchEcnError) as cm:
            getGateway('Nonsense')
        self.assertEqual(cm.exception.message, 'No such gateway for ecn : Nonsense')


if __name__ == '__main__':
    import unittest
    unittest.main()
