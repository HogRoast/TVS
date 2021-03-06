# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from swagger_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server.models.inline_response20013 import InlineResponse20013  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from swagger_server.models.symbol_mapping import SymbolMapping  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTradingPanelBridgeOrdersOnlyController(BaseTestCase):
    """TradingPanelBridgeOrdersOnlyController integration test stubs"""

    def test_accounts_account_id_executions_get(self):
        """Test case for accounts_account_id_executions_get

        
        """
        query_string = [('instrument', 'instrument_example'),
                        ('maxCount', 8.14)]
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/executions'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_instruments_get(self):
        """Test case for accounts_account_id_instruments_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/instruments'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_get(self):
        """Test case for accounts_account_id_orders_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/orders'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_history_get(self):
        """Test case for accounts_account_id_orders_history_get

        
        """
        query_string = [('maxCount', 8.14)]
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/ordersHistory'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_order_id_delete(self):
        """Test case for accounts_account_id_orders_order_id_delete

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/orders/{orderId}'.format(accountId='accountId_example', orderId='orderId_example'),
            method='DELETE',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_order_id_get(self):
        """Test case for accounts_account_id_orders_order_id_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/orders/{orderId}'.format(accountId='accountId_example', orderId='orderId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_order_id_put(self):
        """Test case for accounts_account_id_orders_order_id_put

        
        """
        data = dict(qty=8.14,
                    limitPrice=8.14,
                    stopPrice=8.14,
                    stopLoss=8.14,
                    takeProfit=8.14,
                    digitalSignature='digitalSignature_example')
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/orders/{orderId}'.format(accountId='accountId_example', orderId='orderId_example'),
            method='PUT',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_orders_post(self):
        """Test case for accounts_account_id_orders_post

        
        """
        query_string = [('requestId', 'requestId_example')]
        data = dict(instrument='instrument_example',
                    qty=8.14,
                    side='buy',
                    type='limit',
                    limitPrice=8.14,
                    stopPrice=8.14,
                    durationType='durationType_example',
                    durationDateTime=8.14,
                    stopLoss=8.14,
                    takeProfit=8.14,
                    digitalSignature='digitalSignature_example')
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/orders'.format(accountId='accountId_example'),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_positions_get(self):
        """Test case for accounts_account_id_positions_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/positions'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_positions_position_id_delete(self):
        """Test case for accounts_account_id_positions_position_id_delete

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/positions/{positionId}'.format(accountId='accountId_example', positionId='positionId_example'),
            method='DELETE',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_positions_position_id_get(self):
        """Test case for accounts_account_id_positions_position_id_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/positions/{positionId}'.format(accountId='accountId_example', positionId='positionId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_positions_position_id_put(self):
        """Test case for accounts_account_id_positions_position_id_put

        
        """
        data = dict(stopLoss=8.14,
                    takeProfit=8.14)
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/positions/{positionId}'.format(accountId='accountId_example', positionId='positionId_example'),
            method='PUT',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_account_id_state_get(self):
        """Test case for accounts_account_id_state_get

        
        """
        query_string = [('locale', 'en')]
        response = self.client.open(
            '/tradingview/v1/accounts/{accountId}/state'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accounts_get(self):
        """Test case for accounts_get

        
        """
        response = self.client.open(
            '/tradingview/v1/accounts',
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_authorize_post(self):
        """Test case for authorize_post

        
        """
        data = dict(login='login_example',
                    password='password_example',
                    twoFaCode='twoFaCode_example')
        response = self.client.open(
            '/tradingview/v1/authorize',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_config_get(self):
        """Test case for config_get

        
        """
        query_string = [('locale', 'en')]
        response = self.client.open(
            '/tradingview/v1/config',
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_depth_get(self):
        """Test case for depth_get

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/tradingview/v1/depth',
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mapping_get(self):
        """Test case for mapping_get

        
        """
        response = self.client.open(
            '/tradingview/v1/mapping',
            method='GET',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_get(self):
        """Test case for quotes_get

        
        """
        query_string = [('symbols', 'symbols_example')]
        response = self.client.open(
            '/tradingview/v1/quotes',
            method='GET',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
