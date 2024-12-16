# caesar cipher is a special case of the affine cipher
# where a = 1, the caesar cipher is vulnerable to brute force attacks
# see more at: https://en.wikipedia.org/wiki/Caesar_cipher
def caesar_encrypt(plaintext: str, rot: int) -> str:
    plaintext = plaintext.lower()
    rot %= 26
    res = ""
    for c in plaintext:
        if "a" <= c <= "z":
            res += chr(ord("a") + (ord(c) + rot - ord("a")) % 26)
        else:
            res += c
    return res


def caesar_decrypt(ciphertext: str, rot: int) -> str:
    res = caesar_encrypt(ciphertext, -rot)
    return res


def rot13_encrypt(plaintext: str) -> str:
    return caesar_encrypt(plaintext, 13)


def rot13_decrypt(ciphertext: str) -> str:
    return rot13_encrypt(ciphertext)
