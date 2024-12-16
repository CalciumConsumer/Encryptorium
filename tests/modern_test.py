import pytest
from src.modern_ciphers.xdes import xdes_encrypt, xdes_decrypt
from src.modern_ciphers.des import des_encrypt, des_decrypt


@pytest.mark.parametrize(
    "message, key, pad, iv",
    [(b"this is a sentence to test the program encryption and decryption", "abcdefק", 1, None)],
)
def test_des(message, key, pad, iv):
    pad = 1
    key = (key.replace(" ", ""))[:8]
    encrypted = des_encrypt(message, key, pad, iv)
    decrypted = des_decrypt(encrypted, key, pad, iv)
    assert decrypted == message
