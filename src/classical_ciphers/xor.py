from os import urandom


def genkey(length: int) -> bytes:
    """Generate encryption key."""
    if isinstance(length, str):
        length = len(length)
    return urandom(length)


def xor_encrypt(plaintext: str | bytes, key: bytes) -> str:
    """Concatenate xor two strings together."""
    if isinstance(plaintext, str):
        return "".join(chr(ord(a) ^ b) for a, b in zip(plaintext, key))
    else:
        return "".join([a ^ b for a, b in zip(plaintext, key)])


def xor_decrypt(ciphertext: str, key: bytes) -> str:
    return xor_encrypt(ciphertext, key)
