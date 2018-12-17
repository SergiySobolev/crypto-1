from com.sbk.bit.little_endian import little_endian
from com.sbk.bit.reverse_little_endian import reverse_little_endian


def bytes_to_words(b):
    wordcount = len(b) // 4
    words = wordcount * [0]
    for i in range(0, wordcount):
        words[i] = little_endian((b[i * 4:(i + 1) * 4]))
    return words


def words_to_bytes(words):
    wordcount = len(words)
    bytes = []
    for i in range(0, wordcount):
        bytes += reverse_little_endian(words[i])
    return bytes
