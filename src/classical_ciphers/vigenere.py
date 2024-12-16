def get_tabula_value(plaintext_char: str, key_char: str) -> str:
    """returns the vigenere tabula recta value for 2 chars"""
    return chr(ord("a") + ((ord(plaintext_char) + ord(key_char) - 2 * ord("a")) % 26))


def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    keyidx = 0
    key = key.lower()
    plaintext = plaintext.lower()
    for i in range(0, len(plaintext)):
        if plaintext[i] == " ":
            ciphertext += " "
            continue
        keyidx %= len(key)
        ciphertext += get_tabula_value(plaintext[i], key[keyidx])
        keyidx += 1
    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = key.lower()
    ciphertext = ciphertext.lower()
    decrypt = lambda c, k: chr(ord("a") + ((ord(c) - ord(k)) % 26))
    plaintext = ""
    keyidx = 0
    for char in ciphertext:
        if char == " ":
            plaintext += " "
            continue
        keyidx %= len(key)
        plaintext += decrypt(char, key[keyidx])
        keyidx += 1
    return plaintext
