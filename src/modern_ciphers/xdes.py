from src.modern_ciphers.des import des_encrypt, des_decrypt
import struct


# xdes is des encryption with XES (Xor-Encrypt-Xor) mode of operation
# see:
# https://en.wikipedia.org/wiki/DES-X
# https://en.wikipedia.org/wiki/Xor-encrypt-xor
def pad_message(message):
    """pads message according to PKCS#5 padding(same as PKCS#7 padding)"""
    if isinstance(message, str):
        message = message.encode()
    length = len(message)
    return message.ljust(length + 8 >> 3 << 3, chr(8 - (length & 7)).encode())


def unpad_message(message):
    """Remove PKCS#5 padding."""
    padding_length = message[-1]
    return message[:-padding_length]


def xor_blocks(message: str, key: str):
    if isinstance(key, str):
        key = int(key)
    if isinstance(message, str):
        message = message.encode()
    blocks = [struct.unpack(">Q", message[i : i + 8])[0] ^ key for i in range(0, len(message), 8)]
    return b"".join(struct.pack(">Q", b) for b in blocks)


def xdes_encrypt(plaintext, des_key, xorkey1, xorkey2):
    plaintext = pad_message(plaintext)
    ciphertext = xor_blocks(plaintext, xorkey1)
    ciphertext = des_encrypt(ciphertext, des_key, 0)
    ciphertext = xor_blocks(ciphertext, xorkey2)
    return ciphertext


def xdes_decrypt(ciphertext, des_key, xorkey1, xorkey2):
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode()
    plaintext = xor_blocks(ciphertext, xorkey2)
    plaintext = des_decrypt(plaintext, des_key, 0)
    plaintext = xor_blocks(plaintext, xorkey1)
    return unpad_message(plaintext)
