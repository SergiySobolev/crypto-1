from Crypto.Cipher import AES


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
    cypherTextBlocks = [cipher_text[i:i + (block_size * 2)] for i in range(0, len(cipher_text), (block_size * 2))]
    to_byte_func = lambda x: bytes.fromhex(x)
    cipher_text_blocks_bytes = list(map(to_byte_func, cypherTextBlocks))
    k = bytes.fromhex(key)

    pt = ""

    ln = len(cipher_text_blocks_bytes)
    for c in reversed(cipher_text_blocks_bytes):
        ln = ln - 1
        if ln > 0:
            cipher = AES.new(k, AES.MODE_ECB).decrypt(c)
            plaintext = strxor(cipher, cipher_text_blocks_bytes[ln - 1])
            pt = plaintext + pt

    padding_amount = ord(pt[len(pt) - 1:])

    return pt[:-padding_amount]


def strxor(str_a, str_b):
    return "".join(chr(chrA ^ chrB) for (chrA, chrB) in zip(str_a, str_b))




