def words_from_bytes(raw_bytes):
    words = [int.from_bytes(raw_bytes[i:i+4], 'big') for i in range(0, len(raw_bytes), 4)]
    words.reverse()
    return words

def bytes_from_words(raw_words):
    return b''.join([raw_words[i-1].to_bytes((raw_words[i-1].bit_length() + 7) // 8, 'big') for i in range(len(raw_words), 0, -1)])
