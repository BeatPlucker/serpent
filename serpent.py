import ctr
import utils


phi = 0x9e3779b9


def s_box_0(w0, w1, w2, w3):
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


def s_box_1(w0, w1, w2, w3):
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


def s_box_2(w0, w1, w2, w3):
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


def s_box_3(w0, w1, w2, w3):
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


def s_box_4(w0, w1, w2, w3):
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


def s_box_5(w0, w1, w2, w3):
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


def s_box_6(w0, w1, w2, w3):
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


def s_box_7(w0, w1, w2, w3):
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


def key_mixing(w0, w1, w2, w3, subkey):
    w0 ^= subkey[0]
    w1 ^= subkey[1]
    w2 ^= subkey[2]
    w3 ^= subkey[3]
    return w0, w1, w2, w3


def linear_transformation(w0, w1, w2, w3):
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
        prekeys[i:i+4] = s_boxes[j](prekeys[i], prekeys[i+1], prekeys[i+2], prekeys[i+3])
        j = (j + 7) % 8
    subkeys = [prekeys[i:i+4] for i in range(0, 132, 4)]
    return subkeys


def encrypt_words(w0, w1, w2, w3, subkeys):
    for i in range(31):
        w0, w1, w2, w3 = key_mixing(w0, w1, w2, w3, subkeys[i])
        w0, w1, w2, w3 = s_boxes[i%8](w0, w1, w2, w3)
        w0, w1, w2, w3 = linear_transformation(w0, w1, w2, w3)
    w0, w1, w2, w3 = key_mixing(w0, w1, w2, w3, subkeys[31])
    w0, w1, w2, w3 = s_box_7(w0, w1, w2, w3)
    w0, w1, w2, w3 = key_mixing(w0, w1, w2, w3, subkeys[32])
    return w0, w1, w2, w3


def encrypt(plain_text, key, nonce):
    return ctr.encrypt(plain_text, key, nonce)


def decrypt(cipher_text, key, nonce):
    return encrypt(cipher_text, key, nonce)
