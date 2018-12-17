from functools import reduce

from com.sbk.bit.double_round import double_round_tuple
from com.sbk.bit.words_bytes import bytes_to_words, words_to_bytes


def repeated(f, n):
    def r_fun(p):
        return reduce(lambda x, _: f(x), range(n), p)

    return r_fun


def salsa20(b):
    z = bytes_to_words(b)
    x = repeated(double_round_tuple, 10)(z)
    salsa_words = z + x
    return tuple(words_to_bytes(salsa_words))
