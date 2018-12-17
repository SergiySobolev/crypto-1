def little_endian(b):
    assert len(b) == 4
    return b[0] + 2 ** 8 * b[1] + 2 ** 16 * b[2] + 2 ** 24 * b[3]