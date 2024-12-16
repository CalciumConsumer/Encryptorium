# atbash is a special case of the affine cipher
# where a = -1
def atbash_value(char: str) -> str:
    start_value = ord("A") if char.isupper() else ord("a")
    return chr(start_value + 25 - (ord(char) - start_value))


# Non-English letters+space logic added. It will just ingore them and add as they are
def atbash_encrypt(plaintext: str):
    ciphertext = ""
    for c in plaintext:
        if not ("a" <= c <= "z" or "A" <= c <= "Z"):
            ciphertext += c
            continue
        ciphertext += atbash_value(c)
    return ciphertext


def atbash_decrypt(ciphertext: str):
    return atbash_encrypt(ciphertext)
