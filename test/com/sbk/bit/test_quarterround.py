import unittest
import numpy as np
from parameterized import parameterized

from com.sbk.bit.quarter_round import quarter_round


class TestQuarterRound(unittest.TestCase):

    @parameterized.expand([
        ["1", (0x00000001, 0x00000000, 0x00000000, 0x00000000), (0x08008145, 0x00000080, 0x00010200, 0x20500000)],
        ["2", (0x00000000, 0x00000000, 0x00000000, 0x00000001), (0x00048044, 0x00000080, 0x00010000, 0x20100001)],
        ["3", (0xe7e8c006, 0xc4f9417d, 0x6479b4b2, 0x68c67137), (0xe876d72b, 0x9361dfd5, 0xf1460244, 0x948541a3)],
        ["4", (0xd3917c5b, 0x55f1c407, 0x52a58a7a, 0x8f887a3b), (0x3e2f308c, 0xd90a8f36, 0x6ab2a923, 0x2883524c)]
    ])
    def test_quarter_round(self, name, input_value, expected_value):
        np.testing.assert_array_equal(quarter_round(input_value), expected_value)

