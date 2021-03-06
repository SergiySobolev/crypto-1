import unittest

import numpy as np

from com.sbk.bit.row_round import row_round


class TestRowRound(unittest.TestCase):

    def test_row_round_1(self):
        input_value = [
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000001, 0x00000000, 0x00000000, 0x00000000)
        ]
        expected_value = [
            (0x08008145, 0x00000080, 0x00010200, 0x20500000),
            (0x20100001, 0x00048044, 0x00000080, 0x00010000),
            (0x00000001, 0x00002000, 0x80040000, 0x00000000),
            (0x00000001, 0x00000200, 0x00402000, 0x88000100)
        ]
        np.testing.assert_array_equal(row_round(input_value), expected_value)

    def test_row_round_2(self):
        input_value = [
            (0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365),
            (0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6),
            (0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e),
            (0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a)
        ]
        expected_value = [
            (0xa890d39d, 0x65d71596, 0xe9487daa, 0xc8ca6a86),
            (0x949d2192, 0x764b7754, 0xe408d9b9, 0x7a41b4d1),
            (0x3402e183, 0x3c3af432, 0x50669f96, 0xd89ef0a8),
            (0x0040ede5, 0xb545fbce, 0xd257ed4f, 0x1818882d)

        ]
        np.testing.assert_array_equal(row_round(input_value), expected_value)
