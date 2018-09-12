from swagger_server.gateways.test_ex.gateway import TestGwy
from swagger_server.gateways.base_gateway import InvalidSessionError, InvalidAccountError, AccountPermissionError, OrderValidationError
from swagger_server.test import BaseTestCase

class TestTestExchangeGateway(BaseTestCase):
    def test_initialisation(self):
        gwy = TestGwy()
        self.assertEqual(gwy.server, './swagger_server/test/test_exchange.dat')
        self.assertTrue('accountId_example' in gwy.accounts)
        self.assertTrue('api_key' in gwy.accounts['accountId_example'])
        self.assertTrue('secret_key' in gwy.accounts['accountId_example'])

    def test_establishSession(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertTrue(isinstance(gwy.session, dict))

    def test_destroySession(self):
        gwy = TestGwy()
        gwy.establishSession()
        gwy.destroySession()
        self.assertEqual(gwy.session, None)

    def test_disestablishSession_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.destroySession()
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getPermissions(self):
        gwy = TestGwy()
        gwy.establishSession()
        perms = gwy.getPermissions('accountId_example')
        self.assertEqual(len(perms), 1)
        self.assertEqual(perms['instruments'][0], 'TestInst1')

    def test_getPermissions_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        with self.assertRaises(InvalidAccountError) as cm:
            perms = gwy.getPermissions('NoSuchAccount')
        self.assertEqual(cm.exception.msg, 'Account - NoSuchAccount - does not exist')

    def test_getPermissions_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            perms = gwy.getPermissions('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getAllInstruments(self):
        gwy = TestGwy()
        gwy.establishSession()
        insts = gwy.getAllInstruments()
        self.assertEqual(len(insts.keys()), 2)
        self.assertTrue('TestInst1' in insts)
        self.assertTrue('TestInst2' in insts)
        self.assertEqual(insts['TestInst1']['name'], 'TestInst1')
        self.assertEqual(insts['TestInst2']['name'], 'TestInst2')

    def test_getAllInstruments_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getAllInstruments()
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getInstruments(self):
        gwy = TestGwy()
        gwy.establishSession()
        insts = gwy.getInstruments('accountId_example')
        self.assertEqual(len(insts), 1)
        self.assertEqual(insts[0]['name'], 'TestInst1')

    def test_getInstruments_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        with self.assertRaises(InvalidAccountError) as cm:
            insts = gwy.getInstruments('NoSuchAccount')
        self.assertEqual(cm.exception.msg, 'Account - NoSuchAccount - does not exist')

    def test_getInstruments_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            insts = gwy.getInstruments('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getExchangeInfo(self):
        gwy = TestGwy()
        gwy.establishSession()
        exInfo = gwy.getExchangeInfo()
        self.assertEqual(exInfo['name'], 'TestEx')
        self.assertEqual(exInfo['description'], 'A dummy exchange used for testing purposes')

    def test_getExchangeInfo_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            exInfo = gwy.getExchangeInfo()
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getExecutions(self):
        gwy = TestGwy()
        gwy.establishSession()
        exes = gwy.getExecutions('accountId_example', 'TestInst2')
        self.assertEqual(len(exes), 1)
        self.assertEqual(exes[0]['id'], '1225') 

    def test_getExecutions_Multiple(self):
        gwy = TestGwy()
        gwy.establishSession()
        exes = gwy.getExecutions('accountId_example', 'TestInst1')
        self.assertEqual(len(exes), 2)
        self.assertEqual(exes[0]['id'], '1223') 
        self.assertEqual(exes[1]['id'], '1224') 

    def test_getExecutions_MaxCount(self):
        gwy = TestGwy()
        gwy.establishSession()
        exes = gwy.getExecutions('accountId_example', 'TestInst1', 1)
        self.assertEqual(len(exes), 1)
        self.assertEqual(exes[0]['id'], '1223') 

    def test_getExecutions_EmptyList(self):
        gwy = TestGwy()
        gwy.establishSession()
        exes = gwy.getExecutions('NoSuchAccount', 'TestInst2')
        self.assertEqual(len(exes), 0)

    def test_getExecutions_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            exes = gwy.getExecutions('accountId_example', 'TestInst1')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getOrders(self):
        gwy = TestGwy()
        gwy.establishSession()
        ords = gwy.getOrders('accountId_example')
        self.assertEqual(len(ords), 1)
        self.assertEqual(ords[0]['id'], '123')

    def test_getOrders_EmptyList(self):
        gwy = TestGwy()
        gwy.establishSession()
        ords = gwy.getOrders('NoSuchAccount')
        self.assertEqual(len(ords), 0)

    def test_getOrders_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            ords = gwy.getOrders('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getHistoricalOrders(self):
        gwy = TestGwy()
        gwy.establishSession()
        ords = gwy.getHistoricalOrders('accountId_example')
        self.assertEqual(len(ords), 2)
        self.assertEqual(ords[0]['id'], '124')
        self.assertEqual(ords[1]['id'], '125')

    def test_getHistoricalOrders_MaxCount(self):
        gwy = TestGwy()
        gwy.establishSession()
        ords = gwy.getHistoricalOrders('accountId_example', 1)
        self.assertEqual(len(ords), 1)
        self.assertEqual(ords[0]['id'], '124')

    def test_getHistoricalOrders_EmptyList(self):
        gwy = TestGwy()
        gwy.establishSession()
        ords = gwy.getHistoricalOrders('NoSuchAccount')
        self.assertEqual(len(ords), 0)

    def test_getHistoricalOrders_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            exes = gwy.getHistoricalOrders('accountId_example')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_cancelOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertTrue(gwy.cancelOrder('accountId_example', '123'))
        ords = gwy.getHistoricalOrders('accountId_example')
        cancelled = False
        for order in ords:
            if order['id'] == '123' and order['status'] == 'cancelled':
                cancelled = True
        self.assertTrue(cancelled)

    def test_cancelOrder_NoOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.cancelOrder('accountId_example', '789'))

    def test_cancelOrder_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.cancelOrder('NoSuchAccount', '123'))

    def test_cancelOrder_AlreadyTerminal(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.cancelOrder('accountId_example', '124'))

    def test_cancelOrder_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.cancelOrder('accountId_example', '123')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = gwy.getOrder('accountId_example', '123')
        self.assertFalse(order is None)
        self.assertEqual(order['id'], '123')

    def test_getOrder_TermOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = gwy.getOrder('accountId_example', '124')
        self.assertFalse(order is None)
        self.assertEqual(order['id'], '124')

    def test_getOrder_NoOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = gwy.getOrder('accountId_example', '343')
        self.assertTrue(order is None)

    def test_getOrder_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = gwy.getOrder('NoSuchAccount', '123')
        self.assertTrue(order is None)

    def test_getOrder_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            order = gwy.getOrder('accountId_example', '123')
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_modifyOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertTrue(gwy.modifyOrder('accountId_example', '123', 50.0, 100.05, 100.0))
        order = gwy.getOrder('accountId_example', '123')
        self.assertFalse(order is None)
        self.assertEqual(order['qty'], 50.0)
        self.assertEqual(order['limit_price'], 100.05)
        self.assertEqual(order['stop_price'], 100.0)

    def test_modifyOrder_NoOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.modifyOrder('accountId_example', '343', 50.0, 100.05, 100.0))

    def test_modifyOrder_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.modifyOrder('NoSuchAccount', '123', 50.0, 100.05, 100.0))

    def test_modifyOrder_TermOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        self.assertFalse(gwy.modifyOrder('accountId_example', '124', 50.0, 100.05, 100.0))

    def test_modifyOrder_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.modifyOrder('accountId_example', '123', 50.0)
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_getNextId(self):
        gwy = TestGwy()
        self.assertEqual(gwy.getNextId('order'), 126)
        self.assertEqual(gwy.getNextId('order'), 127)
        self.assertEqual(gwy.getNextId('execution'), 1226)
        self.assertEqual(gwy.getNextId('execution'), 1227)

    def test_getNextId_NoFountain(self):
        gwy = TestGwy()
        with self.assertRaises(KeyError) as cm:
            gwy.getNextId('trevi')

    def test_createOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        id_ = gwy.createOrder('accountId_example', 'TestInst1', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtt', 1002322.1)
        self.assertEqual(id_, '126')
        order = gwy.getOrder('accountId_example', id_)
        self.assertFalse(order is None)
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

    def test_createOrder_NoAccount(self):
        gwy = TestGwy()
        gwy.establishSession()
        with self.assertRaises(InvalidAccountError) as cm:
            gwy.createOrder('NoSuchAccount', 'TestInst1', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtt', 1002322.1)
        self.assertEqual(cm.exception.msg, 'Account - NoSuchAccount - does not exist')

    def test_createOrder_InstNotPermed(self):
        gwy = TestGwy()
        gwy.establishSession()
        with self.assertRaises(AccountPermissionError) as cm:
            gwy.createOrder('accountId_example', 'TestInst2', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtt', 1002322.1)
        self.assertEqual(cm.exception.msg, 'Account - accountId_example - is not permissioned for instrument: TestInst2')

    def test_createOrder_NotEstablished(self):
        gwy = TestGwy()
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.createOrder('accountId_example', 'TestInst1', 12.0, 'buy', 'limit', 112.12, 112.0, 'gtt', 1002322.1)
        self.assertEqual(cm.exception.msg, 'Session not established')

    def test_validateOrder(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = {}
        order['id'] = '1'
        order['instrument'] = 'TestInst1'
        order['qty'] = 10.0
        order['side'] = 'buy'
        order['type'] = 'limit'
        order['limit_price'] = 100.0
        gwy.validateOrder(order)

    def test_validateOrder_MissingId(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = {}
        order['instrument'] = 'TestInst1'
        order['qty'] = 10.0
        order['side'] = 'buy'
        order['type'] = 'limit'
        order['limit_price'] = 100.0
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order missing "id" field')

    def test_validateOrder_MissingOtherMandatory(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = {}
        order['id'] = '1'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "instrument" field')

        order['instrument'] = 'TestInst1'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "qty" field')

        order['qty'] = 10.0
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "side" field')

        order['side'] = 'buy'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "type" field')

        order['type'] = 'limit'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "limit_price" field')

    def test_validateOrder_IncorrectValues(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = {}
        order['id'] = '1'
        order['instrument'] = 'TestInst3'
        order['qty'] = -0.1
        order['side'] = 'mid'
        order['type'] = 'banana'
        order['limit_price'] = 100.0
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - has invalid "instrument": TestInst3')

        order['instrument'] = 'TestInst2'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - has invalid "qty": -0.1')

        order['qty'] = 10.0
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - has invalid "side": mid')

        order['side'] = 'sell'
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - has invalid "type": banana')

    def test_validateOrder_MissingQty(self):
        gwy = TestGwy()
        gwy.establishSession()
        order = {}
        order['id'] = '1'
        order['instrument'] = 'TestInst1'
        order['side'] = 'buy'
        order['type'] = 'limit'
        order['limit_price'] = 100.0
        with self.assertRaises(OrderValidationError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Order - 1 - missing "qty" field')

    def test_validateOrder_NotEstablished(self):
        gwy = TestGwy()
        order = {}
        order['id'] = '1'
        order['instrument'] = 'TestInst1'
        order['qty'] = 10.0
        order['side'] = 'buy'
        order['type'] = 'limit'
        order['limit_price'] = 100.0
        with self.assertRaises(InvalidSessionError) as cm:
            gwy.validateOrder(order)
        self.assertEqual(cm.exception.msg, 'Session not established')

if __name__ == '__main__':
    import unittest
    unittest.main()
