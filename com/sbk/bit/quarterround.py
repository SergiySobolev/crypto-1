def quarter_round(y):
    assert len(y) == 4
    word_size = 32
    p = 2 ** word_size
    z1 = y[1] ^ left_rotate((y[0] + y[3]) % p,  7, word_size)
    z2 = y[2] ^ left_rotate((z1 + y[0]) % p,  9, word_size)
    z3 = y[3] ^ left_rotate((z2 + z1) % p, 13, word_size)
    z0 = y[0] ^ left_rotate((z3 + z2) % p, 18, word_size)
    return [z0, z1, z2, z3]




def left_rotate(number, bits, word_size=32):
    wraparound = number >> word_size - bits
    shifted = number << bits & 2 ** word_size - 1
    return shifted | wraparound
