import unittest
from unittest.mock import MagicMock
from redis import Redis

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.redis = Redis(host='redis', port=6379, decode_responses=True)

    def tearDown(self):
        pass

    def test_redis_increment(self):
        self.redis.get = MagicMock(return_value=3)
        plunders = self.redis.get('plunders')
        self.assertEqual(plunders, 2)
        pass

if __name__ == '__main__':
    unittest.main()
