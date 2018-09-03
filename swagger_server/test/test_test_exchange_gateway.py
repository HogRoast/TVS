from swagger_server.gateways.test_exchange import TestGwy, InvalidSessionError
from swagger_server.test import BaseTestCase

class TestTestExchangeGateway(BaseTestCase):
    def test_initialisation(self):
        gwy = TestGwy()
        self.assertEqual(gwy.server, './swagger_server/test/test_exchange.dat')
        self.assertTrue('accountId_example' in gwy.accounts)
        self.assertTrue('api_key' in gwy.accounts['accountId_example'])
        self.assertTrue('signature' in gwy.accounts['accountId_example'])

    def test_connect(self):
        gwy = TestGwy()
        gwy.connect()
        self.assertTrue(isinstance(gwy.session, dict))

    def test_disconnect(self):
        gwy = TestGwy()
        gwy.connect()
        gwy.disconnect()
        self.assertEqual(gwy.session, None)

    def test_disconnect_NotConnected(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.disconnect()
        self.assertEqual(cm.exception.msg, 'Not connected')

    def test_getPermissions(self):
        gwy = TestGwy()
        gwy.connect()
        perms = gwy.getPermissions('accountId_example')
        self.assertEqual(len(perms), 1)
        self.assertEqual(perms['instruments'][0], 'TestInst1')

    def test_getPermissions_NotConnected(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            perms = gwy.getPermissions('accountId_example')
        self.assertEqual(cm.exception.msg, 'Not connected')

    def test_getAllInstruments(self):
        gwy = TestGwy()
        gwy.connect()
        insts = gwy.getAllInstruments()
        self.assertEqual(len(insts), 2)
        self.assertEqual(insts[0]['name'], 'TestInst1')
        self.assertEqual(insts[1]['name'], 'TestInst2')

    def test_getAllInstruments_NotConnected(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getAllInstruments()
        self.assertEqual(cm.exception.msg, 'Not connected')

    def test_getInstruments(self):
        gwy = TestGwy()
        gwy.connect()
        insts = gwy.getInstruments('accountId_example')
        self.assertEqual(len(insts), 1)
        self.assertEqual(insts[0]['name'], 'TestInst1')

    def test_getInstruments_NotConnected(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getInstruments('accountId_example')
        self.assertEqual(cm.exception.msg, 'Not connected')

    def test_getExchangeInfo(self):
        gwy = TestGwy()
        gwy.connect()
        exInfo = gwy.getExchangeInfo()
        self.assertEqual(exInfo['name'], 'TestEx')
        self.assertEqual(exInfo['description'], 'A dummy exchange used for testing purposes')

    def test_getExchangeInfo_NotConnected(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            exInfo = gwy.getExchangeInfo()
        self.assertEqual(cm.exception.msg, 'Not connected')

if __name__ == '__main__':
    import unittest
    unittest.main()
