import unittest
import numpy as np
from parameterized import parameterized

from com.sbk.hex.func import _chunks as ch, str_to_hex, str_to_hex_oct


class TestHexFunc(unittest.TestCase):

    @parameterized.expand([
        ["test_string 3-chunks", 'test_string', 3, ['tes', 't_s', 'tri', 'ng']],
        ["test_string 2-chunks", 'test_string', 2, ['te', 'st', '_s', 'tr', 'in', 'g']],
        ["test_string 4-chunks", 'test_string', 4, ['test', '_str', 'ing']]
    ])
    def test_coefficient_of_determination_parametrized(self, name, test_string, chunk_num, expected_array):
        actual_array = np.array(list(ch(test_string, chunk_num)))
        np.testing.assert_array_equal(actual_array, expected_array)

    @parameterized.expand([
        ["test_string", 'test_string', '746573745f737472696e67'],
        ["abcde", 'abcde', '6162636465']
    ])
    def test_str_to_hex(self, name, test_string, expected_result):
        self.assertEqual(str_to_hex(test_string), expected_result)