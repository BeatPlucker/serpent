import utils
import serpent


def encrypt(plain_text, key, nonce):
    key_words = utils.words_from_bytes(key)
    subkeys = serpent.key_schedule(key_words)
    nonce = int.from_bytes(nonce, 'big')
    cipher_text = b''
    counter = 0
    for i in range(0, len(plain_text), 16):
        plain_block = plain_text[i:i+16]
        plain_words = utils.words_from_bytes(plain_block)
        counter_block = counter ^ nonce
        counter_block = counter_block.to_bytes(16, 'big')
        w0, w1, w2, w3 = utils.words_from_bytes(counter_block)
        cipher_counter_words = serpent.encrypt_words(w0, w1, w2, w3, subkeys)
        cipher_words = utils.xor_blocks(plain_words, cipher_counter_words)
        cipher_block = utils.bytes_from_words(cipher_words)
        cipher_text += cipher_block
        counter += 1
    return cipher_text


def decrypt(cipher_text, key, nonce):
    return encrypt(cipher_text, key, nonce)
