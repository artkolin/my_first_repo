import unittest

from parameterized import parameterized

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ['foo', 2, 2],
        ['bar', True, 1],
        ['fizz', 3, 3],
    ])

    def test_foo(self, name, a, b):
        self.assertEqual(a, b)