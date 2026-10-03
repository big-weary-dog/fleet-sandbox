import unittest

from greet import goodbye, hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Ada"), "Hello, Ada!")


class TestGoodbye(unittest.TestCase):
    def test_goodbye(self):
        self.assertEqual(goodbye("Ada"), "Goodbye, Ada!")
