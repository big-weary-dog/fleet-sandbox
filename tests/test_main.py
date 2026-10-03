import unittest

from greet.__main__ import main


class TestMain(unittest.TestCase):
    def test_default(self):
        self.assertEqual(main([]), "Hello, world!")

    def test_name(self):
        self.assertEqual(main(["Bob"]), "Hello, Bob!")

    def test_shout(self):
        self.assertEqual(main(["Bob", "--shout"]), "HELLO, BOB!")
