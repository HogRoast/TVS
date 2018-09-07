from swagger_server.gateways.base_gateway import getMillisecondTimestamp
from swagger_server.test import BaseTestCase
import datetime

class TestBaseGateway(BaseTestCase):
    def test_getMillisecondTimestamp(self):
        self.assertTrue(getMillisecondTimestamp() > 0)
        today = datetime.datetime.utcnow()
        self.assertEqual(getMillisecondTimestamp(
            datetime.datetime(today.year, today.month, today.day)), 0)
        self.assertEqual(getMillisecondTimestamp(
            datetime.datetime(today.year, today.month, today.day),
            datetime.datetime(today.year, today.month, today.day)), 0)
        self.assertEqual(getMillisecondTimestamp(
            datetime.datetime(
                today.year, today.month, today.day, hour=2, minute=10, microsecond=120000),
            datetime.datetime(
                today.year, today.month, today.day, hour=2, minute=10, microsecond=119000)), 1)

if __name__ == '__main__':
    import unittest
    unittest.main()
