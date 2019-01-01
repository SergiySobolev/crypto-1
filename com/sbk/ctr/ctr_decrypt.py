import binascii

from Crypto.Cipher import AES
from Crypto.Util import Counter

from com.sbk.hex.func import str_xor


def ctr_decrypt(key, cypher_text, block_size=16):
    k = bytes.fromhex(key)
    ct = bytes.fromhex(cypher_text)
    iv = ct[:block_size]
    ct1 = ct[block_size:]
    ctr = Counter.new(block_size * 8, initial_value=int.from_bytes(iv, byteorder='big'))
    obj = AES.new(k, AES.MODE_CTR, counter=ctr)
    padded_str = obj.decrypt(ct1)
    return padded_str


def my_ctr_decrypt(key, cipher_text, block_size=16):
    cipher_text_blocks = [cipher_text[i:i + (block_size * 2)] for i in range(0, len(cipher_text), (block_size * 2))]
    iv = int.from_bytes(bytes.fromhex(cipher_text_blocks.pop(0)), byteorder='big')

    cipher_text_blocks_bytes = list(map(lambda x: bytes.fromhex(x), cipher_text_blocks))
    k = bytes.fromhex(key)

    pt = ""

    i = 0
    for c in cipher_text_blocks_bytes:
        ctr = hex(iv + i)[2:(2 * block_size) + 2]
        encIV = AES.new(k, AES.MODE_ECB).encrypt(ctr)
        plaintext = str_xor(encIV, c)
        i = i + 1
        pt = plaintext + pt

    return pt
