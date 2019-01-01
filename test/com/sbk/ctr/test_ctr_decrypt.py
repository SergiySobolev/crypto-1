import unittest

from parameterized import parameterized

from com.sbk.ctr.ctr_decrypt import ctr_decrypt, my_ctr_decrypt


class TestCtrDecrypt(unittest.TestCase):

    @parameterized.expand([
        ["test_ctr_decrypt_1", '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
         '36f18357be4dbd77f050515c73fcf9f2', 'CTR mode lets you build a stream cipher from a block cipher.'],
        ["test_ctr_decrypt_2", '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451',
         '36f18357be4dbd77f050515c73fcf9f2', 'Always avoid the two time pad!']
    ])
    def test_ctr_decrypt_from_pycrypto(self, name, cipher_text, key, plain_text):
        actual_value = ctr_decrypt(key, cipher_text)
        self.assertEqual(bytes(plain_text, 'utf-8'), actual_value)

    @parameterized.expand([
        ["test_ctr_decrypt_1",
         '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
         '36f18357be4dbd77f050515c73fcf9f2', 'CTR mode lets you build a stream cipher from a block cipher.'],
        ["test_ctr_decrypt_2",
         '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451',
         '36f18357be4dbd77f050515c73fcf9f2', 'Always avoid the two time pad!']
    ])
    @unittest.skip("issues in implementing")
    def test_my_ctr_decrypt_(self, name, cipher_text, key, plain_text):
        actual_value = my_ctr_decrypt(key, cipher_text)
        self.assertEqual(bytes(plain_text, 'utf-8'), actual_value)

