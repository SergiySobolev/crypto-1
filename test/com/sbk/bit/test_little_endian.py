import unittest

from parameterized import parameterized

from com.sbk.bit.little_endian import little_endian
from com.sbk.bit.reverse_little_endian import reverse_little_endian


class TestLittleEndian(unittest.TestCase):

    @parameterized.expand([
        ["1", (0, 0, 0, 0), 0x00000000],
        ["2", (86, 75, 30, 9), 0x091e4b56],
        ["3", (255, 255, 255, 250), 0xfaffffff]
    ])
    def test_little_endian(self, name, input_value, expected_value):
        self.assertEqual(little_endian(input_value), expected_value)

    @parameterized.expand([
        ["1", (0, 0, 0, 0), 0x00000000],
        ["2", (86, 75, 30, 9), 0x091e4b56],
        ["3", (255, 255, 255, 250), 0xfaffffff]
    ])
    def test_reverse_little_endian(self, name, expected_value, input_value):
        self.assertEqual(reverse_little_endian(input_value), expected_value)


