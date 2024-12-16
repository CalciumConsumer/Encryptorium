from src.modern_ciphers.des import des_encrypt, des_decrypt
from src.modern_ciphers.xdes import pad_message, unpad_message


def tdes_encrypt(plaintext, keys):
    if len(keys) != 3:
        raise ValueError("keys size should be 3")
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    plaintext = pad_message(plaintext)
    stage1 = des_encrypt(plaintext, keys[0], 0)
    stage2 = des_decrypt(stage1, keys[1], 0)
    stage3 = des_encrypt(stage2, keys[2], 0)
    return stage3


def tdes_decrypt(ciphertext, keys):
    if len(keys) != 3:
        raise ValueError("keys size should be 3")
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode()
    stage1 = des_decrypt(ciphertext, keys[2], 0)
    stage2 = des_encrypt(stage1, keys[1], 0)
    stage3 = des_decrypt(stage2, keys[0], 0)
    return unpad_message(stage3)
