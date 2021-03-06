import unittest

import numpy as np

from com.sbk.bit.double_round import double_round


class TestDoubleRound(unittest.TestCase):

    def test_double_round_1(self):
        input_value = [
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000000, 0x00000000, 0x00000000, 0x00000000),
            (0x00000000, 0x00000000, 0x00000000, 0x00000000),
            (0x00000000, 0x00000000, 0x00000000, 0x00000000)
        ]
        expected_value = [
            (0x8186a22d, 0x0040a284, 0x82479210, 0x06929051),
            (0x08000090, 0x02402200, 0x00004000, 0x00800000),
            (0x00010200, 0x20400000, 0x08008104, 0x00000000),
            (0x20500000, 0xa0000040, 0x0008180a, 0x612a8020)
        ]
        np.testing.assert_array_equal(double_round(input_value), expected_value)

    def test_double_round_2(self):
        input_value = [
            (0xde501066, 0x6f9eb8f7, 0xe4fbbd9b, 0x454e3f57),
            (0xb75540d3, 0x43e93a4c, 0x3a6f2aa0, 0x726d6b36),
            (0x9243f484, 0x9145d1e8, 0x4fa9d247, 0xdc8dee11),
            (0x054bf545, 0x254dd653, 0xd9421b6d, 0x67b276c1)
        ]
        expected_value = [
            (0xccaaf672, 0x23d960f7, 0x9153e63a, 0xcd9a60d0),
            (0x50440492, 0xf07cad19, 0xae344aa0, 0xdf4cfdfc),
            (0xca531c29, 0x8e7943db, 0xac1680cd, 0xd503ca00),
            (0xa74b2ad6, 0xbc331c5c, 0x1dda24c7, 0xee928277)
        ]
        np.testing.assert_array_equal(double_round(input_value), expected_value)
