from swagger_server.gateways.base_gateway import InvalidSessionError, InvalidAccountError, AccountPermissionError, OrderValidationError
from swagger_server.gateways.binance import BinanceGwy
from swagger_server.test import BaseTestCase
import datetime

class TestBinanceGateway(BaseTestCase):
    def test_initialisation(self):
        gwy = BinanceGwy()
        self.assertEqual(gwy.server, 'https://api.binance.com')
        self.assertEqual(gwy.timeout, 3)
        self.assertEqual(gwy.recvWindow, 3000)
        self.assertEqual(gwy.mode, 'test')
        self.assertEqual(gwy.today.year, datetime.datetime.utcnow().year)
        self.assertEqual(gwy.today.month, datetime.datetime.utcnow().month)
        self.assertEqual(gwy.today.day, datetime.datetime.utcnow().day)
        self.assertTrue('accountId_example' in gwy.accounts)
        self.assertTrue('api_key' in gwy.accounts['accountId_example'])
        self.assertTrue('signature' in gwy.accounts['accountId_example'])

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

if __name__ == '__main__':
    import unittest
    unittest.main()
