from swagger_server.gateways.base_gateway import InvalidSessionError, InvalidAccountError, AccountPermissionError, OrderValidationError
from swagger_server.gateways.binance import BinanceGwy
from swagger_server.test import BaseTestCase
import datetime
import requests

class TestBinanceGateway(BaseTestCase):
    def test_initialisation(self):
        gwy = BinanceGwy()
        self.assertEqual(gwy.server, 'https://api.binance.com')
        self.assertEqual(gwy.timeout, 3)
        self.assertEqual(gwy.recvWindow, 3000)
        self.assertEqual(gwy.mode, 'test')
        self.assertTrue('accountId_example' in gwy.accounts)
        self.assertTrue('api_key' in gwy.accounts['accountId_example'])
        self.assertTrue('secret_key' in gwy.accounts['accountId_example'])

    def test_establishDestroySession(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        self.assertFalse(gwy.session is None)

        gwy.destroySession()
        self.assertTrue(gwy.session is None)

    def test_getAllInstruments(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        insts = gwy.getAllInstruments()
        self.assertTrue(len(insts) > 0)

    def test_getAllInstruments_NotEstablished(self):
        gwy = BinanceGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getAllInstruments()
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getInstruments(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        insts = gwy.getInstruments('accountId_example')
        self.assertTrue(len(insts) > 0)

    def test_getInstruments_NoAccount(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        with self.assertRaises(InvalidAccountError) as cm:
            insts = gwy.getInstruments('NoSuchAccount')
        self.assertEqual(cm.exception.msg, 'Account - NoSuchAccount - does not exist')

    def test_getInstruments_NotEstablished(self):
        gwy = BinanceGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getInstruments('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_dictToRequestBody(self):
        gwy = BinanceGwy()
        data = gwy.dictToRequestBody(
                {   'symbol'        : 'LTCBTC',
                    'side'          : 'BUY',
                    'type'          : 'LIMIT',
                    'timeInForce'   : 'GTC',
                    'quantity'      : '1',
                    'price'         : '0.1',
                    'recvWindow'    : '5000',
                    'timestamp'     : '1499827319559'})
        self.assertEqual(data, 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559')

    def test_encodeMsg(self):
        gwy = BinanceGwy()
        data = gwy.dictToRequestBody(
                {   'symbol'        : 'LTCBTC',
                    'side'          : 'BUY',
                    'type'          : 'LIMIT',
                    'timeInForce'   : 'GTC',
                    'quantity'      : '1',
                    'price'         : '0.1',
                    'recvWindow'    : '5000',
                    'timestamp'     : '1499827319559'})
        signature = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
        self.assertEqual(gwy.encodeMsg(data, signature),
            'c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71')

    def test_getOrders(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        ords = gwy.getOrders('accountId_example')
        self.assertEqual(len(ords), 0)

    def test_getOrders_NotEstablished(self):
        gwy = BinanceGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            ords = gwy.getOrders('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_createOrder(self):
        gwy = BinanceGwy()
        gwy.establishSession()
        id_ = gwy.createOrder('accountId_example', 'TestInst1', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtc')
        self.assertEqual(id_[0], 123)
        self.assertFalse(id_ is None)
        order = gwy.getOrder('accountId_example', id_)
        self.assertFalse(order is None)
        '''
        self.assertEqual(order['id'], '126')
        self.assertEqual(order['instrument'], 'TestInst1')
        self.assertEqual(order['qty'], 12.0)
        self.assertEqual(order['side'], 'buy')
        self.assertEqual(order['type'], 'limit')
        self.assertEqual(order['filled_qty'], 0.0)
        self.assertEqual(order['avg_price'], None)
        self.assertEqual(order['limit_price'], 112.12)
        self.assertEqual(order['stop_price'], 112.0)
        self.assertEqual(order['parent_id'], None)
        self.assertEqual(order['parent_type'], None)
        self.assertEqual(order['duration_type'], 'gtt')
        self.assertEqual(order['duration_datetime'], 1002322.1)
        self.assertEqual(order['status'], 'placing')
        '''

    def test_createOrder_NotEstablished(self):
        gwy = BinanceGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            id_ = gwy.createOrder('accountId_example', 'BTCETH', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtc')
        self.assertEqual(cm.exception.msg, 'Session not established')


if __name__ == '__main__':
    import unittest
    unittest.main()
