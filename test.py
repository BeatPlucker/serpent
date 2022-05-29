from utils import words_from_bytes, bytes_from_words
from serpent import encrypt_words


plain_text = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08'

# Serpent encrypts 32-bit words
plain_text_words = words_from_bytes(plain_text)
key_words = words_from_bytes(key)

cypher_text_words = encrypt_words(plain_text_words, key_words)
cypher_text = bytes_from_words(cypher_text_words)
print(cypher_text.hex())
