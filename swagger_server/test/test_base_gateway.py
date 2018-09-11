from swagger_server.gateways.base_gateway import getMillisecondTimestamp
from swagger_server.test import BaseTestCase
import time

class TestBaseGateway(BaseTestCase):
    def test_getMillisecondTimestamp(self):
        self.assertTrue(getMillisecondTimestamp() > 0)
        self.assertAlmostEqual(getMillisecondTimestamp(), int(time.time()*1000))

if __name__ == '__main__':
    import unittest
    unittest.main()
