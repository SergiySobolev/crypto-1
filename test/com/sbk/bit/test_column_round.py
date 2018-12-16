import unittest

import numpy as np

from com.sbk.bit.column_round import column_round


class TestColumnRound(unittest.TestCase):

    def test_column_round_1(self):
        input_value = [
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000)
        ]
        expected_value = [
            (0x10090288, 0x00000000, 0x00000000, 0x00000000),
            (0x00000101, 0x00000000, 0x00000000, 0x00000000),
            (0x00020401, 0x00000000, 0x00000000, 0x00000000),
            (0x40a04001, 0x00000000, 0x00000000, 0x00000000)
        ]
        np.testing.assert_array_equal(column_round(input_value), expected_value)

    def test_column_round_2(self):
        input_value = [
            (0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365),
            (0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6),
            (0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e),
            (0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a)
        ]
        expected_value = [
            (0x8c9d190a, 0xce8e4c90, 0x1ef8e9d3, 0x1326a71a),
            (0x90a20123, 0xead3c4f3, 0x63a091a0, 0xf0708d69),
            (0x789b010c, 0xd195a681, 0xeb7d5504, 0xa774135c),
            (0x481c2027, 0x53a8e4b5, 0x4c1f89c5, 0x3f78c9c8)

        ]
        np.testing.assert_array_equal(column_round(input_value), expected_value)
