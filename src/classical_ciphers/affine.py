from math import gcd


def affine_value(plainchar: str, a: int, b: int) -> str:
    if not plainchar.isalpha():
        return plainchar
    plainchar = plainchar.lower()
    return chr(ord("a") + ((a * (ord(plainchar) - ord("a")) + b) % 26))


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26 for encryption.")
    return "".join(affine_value(c, a, b) for c in plaintext)


def anti_affine_value(cipherchar: str, a: int, b: int) -> str:
    if not cipherchar.isalpha():
        return cipherchar
    cipherchar = cipherchar.lower()
    a_inv = pow(a, -1, 26)
    return chr(ord("a") + (a_inv * ((ord(cipherchar) - ord("a")) - b) % 26))


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26 for decryption.")
    return "".join(anti_affine_value(c, a, b) for c in ciphertext)
