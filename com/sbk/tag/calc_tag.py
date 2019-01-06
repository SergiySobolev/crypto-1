import hashlib
import os


def calc_tag(path_to_file):
    chunks = block_split(path_to_file, 1024)

    for i in range(len(chunks) - 1, 0, -1):
        chunks[i - 1] = chunks[i - 1] + hashlib.sha256(chunks[i]).digest()

    return hashlib.sha256(chunks[0])


def block_split(path_to_file, chunk_size):
    file_size = os.path.getsize(path_to_file)
    chunks = []
    with open(path_to_file, 'rb') as f:
        for i in range(0, file_size, chunk_size):
            f.seek(i)
            current_chunk = f.read(chunk_size)
            chunks.append(current_chunk)
    return chunks