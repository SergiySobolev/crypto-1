def reverse_little_endian(word):
    bytes = 4 * [0]
    bytes[0] = word % 2 ** 8
    bytes[1] = word // 2 ** 8 % 2 ** 8
    bytes[2] = word // 2 ** 16 % 2 ** 8
    bytes[3] = word // 2 ** 24 % 2 ** 8
    return tuple(bytes)
