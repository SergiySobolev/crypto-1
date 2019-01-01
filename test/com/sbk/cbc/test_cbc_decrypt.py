import unittest

from parameterized import parameterized

from com.sbk.cbc.cbc_decrypt import cbc_decrypt, my_cbc_decrypt


class TestCbcDecrypt(unittest.TestCase):

    @parameterized.expand([
        ["test_cbc_decrypt_1", '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81',
         '140b41b22a29beb4061bda66b6747e14', 'Basic CBC mode encryption needs padding.'],
        ["test_cbc_decrypt_2", '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253',
         '140b41b22a29beb4061bda66b6747e14', 'Our implementation uses rand. IV']
    ])
    def test_cbc_decrypt_from_pycrypto(self, name, cipher_text, key, plain_text):
        actual_value = cbc_decrypt(key, cipher_text)
        self.assertEqual(bytes(plain_text, 'utf-8'), actual_value)

    @parameterized.expand([
        ["test_cbc_decrypt_1",
         '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81',
         '140b41b22a29beb4061bda66b6747e14', 'Basic CBC mode encryption needs padding.'],
        ["test_cbc_decrypt_2",
         '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253',
         '140b41b22a29beb4061bda66b6747e14', 'Our implementation uses rand. IV']
    ])
    def test_cbc_decrypt_own_implement(self, name, cipher_text, key, plain_text):
        actual_value = my_cbc_decrypt(key, cipher_text)
        self.assertEqual(plain_text, actual_value)

