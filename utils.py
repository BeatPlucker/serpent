

def words_from_bytes(raw_bytes):
    return [int.from_bytes(raw_bytes[i-4:i], 'big') for i in range(len(raw_bytes), 0, -4)]


def bytes_from_words(raw_words):
    return b''.join([raw_words[i-1].to_bytes((raw_words[i-1].bit_length() + 7) // 8, 'big') for i in range(len(raw_words), 0, -1)])


def xor_blocks(block1, block2):
    return [block1[i] ^ block2[i] for i in range(len(block1))]
