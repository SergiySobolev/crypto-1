import unittest
import numpy as np

from com.sbk.bit.quarterround import quarter_round


class TestQuarterRound(unittest.TestCase):

    def test_quarter_round(self):
        y = [0x00000001, 0x00000000, 0x00000000, 0x00000000]
        expected_value = [0x08008145, 0x00000080, 0x00010200, 0x20500000]
        actual_value = quarter_round(y)
        np.testing.assert_array_equal(actual_value, expected_value)
