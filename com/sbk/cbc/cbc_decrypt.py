from Crypto.Cipher import AES

from com.sbk.hex.func import str_xor


def cbc_decrypt(key, cypher_text, block_size=16):
    k = bytes.fromhex(key)
    ct = bytes.fromhex(cypher_text)
    iv = ct[:block_size]
    ct1 = ct[block_size:]
    obj = AES.new(k, AES.MODE_CBC, iv)
    padded_str = obj.decrypt(ct1)
    padding_amount = ord(padded_str[len(padded_str) - 1:])
    return padded_str[:-padding_amount]


def my_cbc_decrypt(key, cipher_text, block_size=16):
    cipher_text_blocks = [cipher_text[i:i + (block_size * 2)] for i in range(0, len(cipher_text), (block_size * 2))]
    cipher_text_blocks_bytes = list(map(lambda x: bytes.fromhex(x), cipher_text_blocks))
    k = bytes.fromhex(key)

    pt = ""

    ln = len(cipher_text_blocks_bytes)
    for i in reversed(range(1, ln)):
        current_block = cipher_text_blocks_bytes[i]
        previous_block = cipher_text_blocks_bytes[i - 1]
        cipher = AES.new(k, AES.MODE_ECB).decrypt(current_block)
        plaintext = str_xor(cipher, previous_block)
        pt = plaintext + pt

    padding_amount = ord(pt[-1:])

    return pt[:-padding_amount]

