
# Serpent

[Serpent](https://www.cl.cam.ac.uk/~rja14/serpent.html) is a 128-bit block cipher designed by Ross Anderson, Eli Biham and Lars Knudsen as a proposal for the Advanced Encryption Standard.(1998)

This implementation takes as a reference the original [C](http://www.cl.cam.ac.uk/~rja14/Papers/serpent.tar.gz) and [Python](https://www.cl.cam.ac.uk/~fms27/serpent/serpent.py.html) code written by Frank Stajano based on the submission [paper](https://www.cl.cam.ac.uk/~rja14/Papers/serpent.pdf) and combines it with an optimized implementation of the [S-boxes](http://www.ii.uib.no/~osvik/pub/aes3.pdf) developed by Dag Arne Osvik.

>*Nothing better than a Python to write a Serpent.*(Frank Stajano, 1998)

Encrypt a 128 bits message using counter mode (CTR):

```python
>>> from secrets import token_bytes
>>> from serpent import encrypt, decrypt
>>> 
>>> plain_text = b'128 bits message'
>>> key = token_bytes(32)
>>> nonce = token_bytes(16)
>>> 
>>> cipher_text = encrypt(plain_text, key, nonce)
>>> cipher_text
b'\x8a\xa4\x0f\xdbW(\xe4\x12\xcah\x9f\x8e4\x921\x92'
>>> 
>>> decrypt(cipher_text, key, nonce)
b'128 bits message'
```
