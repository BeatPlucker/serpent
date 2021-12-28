import utils
import serpent


def ctr_mode(plain_words, subkeys_words, nonce, counter):
    counter_block = counter ^ nonce
    counter_block = counter_block.to_bytes(16, 'big')
    counter_words = utils.words_from_bytes(counter_block)
    cipher_counter_words = serpent.encrypt_words(counter_words, subkeys_words)
    cipher_words = utils.xor_blocks(plain_words, cipher_counter_words)
    return cipher_words
