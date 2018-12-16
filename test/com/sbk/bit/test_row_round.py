import unittest


from com.sbk.bit.row_round import row_round


class TestRowRound(unittest.TestCase):

    def test_row_round(self):
        input = [
            (0x00000001, 0x00000000, 0x00000000, 0x00000000),
            (0x00000000, 0x00000000, 0x00000000, 0x00000001),
            (0xe7e8c006, 0xc4f9417d, 0x6479b4b2, 0x68c67137),
            (0xd3917c5b, 0x55f1c407, 0x52a58a7a, 0x8f887a3b),
        ]
        actual_value = row_round(input)
        self.assertEqual(actual_value.shape, (4,4))
        self.assertEqual(actual_value[0][0], 0x08008145)
        self.assertEqual(actual_value[0][1], 0x80)
