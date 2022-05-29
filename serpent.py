phi = 0x9e3779b9

def s_box_0(block_words):
    w0, w1, w2, w3 = block_words
    w3 ^= w0
    w4 = w1
    w1 &= w3
    w4 ^= w2
    w1 ^= w0
    w0 |= w3
    w0 ^= w4
    w4 ^= w3
    w3 ^= w2
    w2 |= w1
    w2 ^= w4
    w4 ^= 0xffffffff
    w4 |= w1
    w1 ^= w3
    w1 ^= w4
    w3 |= w0
    w1 ^= w3
    w4 ^= w3
    return w1, w4, w2, w0

def s_box_1(block_words):
    w0, w1, w2, w3 = block_words
    w0 ^= 0xffffffff
    w2 ^= 0xffffffff
    w4 = w0
    w0 &= w1
    w2 ^= w0
    w0 |= w3
    w3 ^= w2
    w1 ^= w0
    w0 ^= w4
    w4 |= w1
    w1 ^= w3
    w2 |= w0
    w2 &= w4
    w0 ^= w1
    w1 &= w2
    w1 ^= w0
    w0 &= w2
    w0 ^= w4
    return w2, w0, w3, w1

def s_box_2(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w0
    w0 &= w2
    w0 ^= w3
    w2 ^= w1
    w2 ^= w0
    w3 |= w4
    w3 ^= w1
    w4 ^= w2
    w1 = w3
    w3 |= w4
    w3 ^= w0
    w0 &= w1
    w4 ^= w0
    w1 ^= w3
    w1 ^= w4
    w4 ^= 0xffffffff
    return w2, w3, w1, w4

def s_box_3(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w0
    w0 |= w3
    w3 ^= w1
    w1 &= w4
    w4 ^= w2
    w2 ^= w3
    w3 &= w0
    w4 |= w1
    w3 ^= w4
    w0 ^= w1
    w4 &= w0
    w1 ^= w3
    w4 ^= w2
    w1 |= w0
    w1 ^= w2
    w0 ^= w3
    w2 = w1
    w1 |= w3
    w1 ^= w0
    return w1, w2, w3, w4

def s_box_4(block_words):
    w0, w1, w2, w3 = block_words
    w1 ^= w3
    w3 ^= 0xffffffff
    w2 ^= w3
    w3 ^= w0
    w4 = w1
    w1 &= w3
    w1 ^= w2
    w4 ^= w3
    w0 ^= w4
    w2 &= w4
    w2 ^= w0
    w0 &= w1
    w3 ^= w0
    w4 |= w1
    w4 ^= w0
    w0 |= w3
    w0 ^= w2
    w2 &= w3
    w0 ^= 0xffffffff
    w4 ^= w2
    return w1, w4, w0, w3

def s_box_5(block_words):
    w0, w1, w2, w3 = block_words
    w0 ^= w1
    w1 ^= w3
    w3 ^= 0xffffffff
    w4 = w1
    w1 &= w0
    w2 ^= w3
    w1 ^= w2
    w2 |= w4
    w4 ^= w3
    w3 &= w1
    w3 ^= w0
    w4 ^= w1
    w4 ^= w2
    w2 ^= w0
    w0 &= w3
    w2 ^= 0xffffffff
    w0 ^= w4
    w4 |= w3
    w2 ^= w4
    return w1, w3, w0, w2

def s_box_6(block_words):
    w0, w1, w2, w3 = block_words
    w2 ^= 0xffffffff
    w4 = w3
    w3 &= w0
    w0 ^= w4
    w3 ^= w2
    w2 |= w4
    w1 ^= w3
    w2 ^= w0
    w0 |= w1
    w2 ^= w1
    w4 ^= w0
    w0 |= w3
    w0 ^= w2
    w4 ^= w3
    w4 ^= w0
    w3 ^= 0xffffffff
    w2 &= w4
    w2 ^= w3
    return w0, w1, w4, w2

def s_box_7(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w1
    w1 |= w2
    w1 ^= w3
    w4 ^= w2
    w2 ^= w1
    w3 |= w4
    w3 &= w0
    w4 ^= w2
    w3 ^= w1
    w1 |= w4
    w1 ^= w0
    w0 |= w4
    w0 ^= w2
    w1 ^= w4
    w2 ^= w1
    w1 &= w0
    w1 ^= w4
    w2 ^= 0xffffffff
    w2 |= w0
    w4 ^= w2
    return w4, w3, w1, w0

s_boxes = (s_box_0, s_box_1, s_box_2, s_box_3, s_box_4, s_box_5, s_box_6, s_box_7)

def rotate_left(word, count):
    return ((word << count) | (word >> (32 - count))) & 0xffffffff

def key_mixing(block_words, subkey_words):
    w0, w1, w2, w3 = block_words
    s0, s1, s2, s3 = subkey_words
    w0 ^= s0
    w1 ^= s1
    w2 ^= s2
    w3 ^= s3
    return w0, w1, w2, w3

def linear_transformation(block_words):
    w0, w1, w2, w3 = block_words
    w0 = rotate_left(w0, 13)
    w2 = rotate_left(w2, 3)
    w1 ^= w0 ^ w2
    w3 ^= w2 ^ ((w0 << 3) & 0xffffffff)
    w1 = rotate_left(w1, 1)
    w3 = rotate_left(w3, 7)
    w0 ^= w1 ^ w3
    w2 ^= w3 ^ ((w1 << 7) & 0xffffffff)
    w0 = rotate_left(w0, 5)
    w2 = rotate_left(w2, 22)
    return w0, w1, w2, w3

def key_schedule(key_words):
    for i in range(132):
        key_words.append(rotate_left(key_words[i] ^ key_words[i+3] ^ key_words[i+5] ^ key_words[i+7] ^ phi ^ i, 11))
    prekeys = key_words[8:]
    j = 3
    for i in range(0, 132, 4):
        prekeys[i:i+4] = s_boxes[j](prekeys[i:i+4])
        j = (j + 7) % 8
    subkeys_words = [prekeys[i:i+4] for i in range(0, 132, 4)]
    return subkeys_words

def encrypt_words(block_words, key_words):
    subkeys_words = key_schedule(key_words)
    for i in range(31):
        block_words = key_mixing(block_words, subkeys_words[i])
        block_words = s_boxes[i%8](block_words)
        block_words = linear_transformation(block_words)
    block_words = key_mixing(block_words, subkeys_words[31])
    block_words = s_box_7(block_words)
    block_words = key_mixing(block_words, subkeys_words[32])
    return block_words
