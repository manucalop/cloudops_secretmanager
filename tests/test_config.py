import unittest
from cloudops_secretmanager.config import config


class TestConfig(unittest.TestCase):
    def setUp(self):
        pass

    def test_config(self):
        self.assertEqual(True, True, "I leave Python!")


if __name__ == "__main__":
    unittest.main()
