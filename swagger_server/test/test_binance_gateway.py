from swagger_server.gateways.binance import BinanceGwy
from swagger_server.test import BaseTestCase

class TestBinanceGateway(BaseTestCase):
    def test_initialisation(self):
        gwy = BinanceGwy();
        self.assertEqual(gwy.server, 'https://api.binance.com')
        self.assertTrue('accountId_example' in gwy.accounts)
        self.assertTrue('api_key' in gwy.accounts['accountId_example'])
        self.assertTrue('signature' in gwy.accounts['accountId_example'])

if __name__ == '__main__':
    import unittest
    unittest.main()
