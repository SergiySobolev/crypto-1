def _chunks(str, chunk_size):
    for i in range(0, len(str), chunk_size):
        yield str[i:i+chunk_size]


def hex_to_str(h):
    return ''.join(chr(int(x, 16)) for x in _chunks(h, 2))


def str_to_hex(s):
    return ''.join('{:02x}'.format(ord(c)) for c in s)


def str_to_hex_oct(s):
    return ''.join(''.join(oct(ord(c)))[2:] for c in s)

