# there are many autokey ciphers, but the one implemented here is the first one
# made by Blaise de Vigenere
def autokey_encrypt(plaintext: str, key: str) -> str:
    plaintext = plaintext.lower()
    key = key.lower()
    ks = len(key)
    ciphertext = ""
    for i in range(0, min(ks, len(plaintext))):
        if plaintext[i] == " ":
            ciphertext += " "
            continue
        ciphertext += chr(ord("a") + (ord(plaintext[i]) + ord(key[i]) - 2 * ord("a")) % 26)
    for i in range(ks, len(plaintext)):
        if plaintext[i] == " ":
            ciphertext += " "
            continue
        ciphertext += chr(ord("a") + (ord(plaintext[i]) + ord(plaintext[i - ks]) - 2 * ord("a")) % 26)
    return ciphertext


def autokey_decrypt(ciphertext: str, key: str):
    ciphertext = ciphertext.lower()
    key = key.lower()
    plaintext = ""
    ks = len(key)
    for i in range(0, min(ks, len(ciphertext))):
        if ciphertext[i] == " ":
            plaintext += " "
            continue
        plaintext += chr(ord("a") + ((ord(ciphertext[i]) - ord(key[i])) % 26))
    for i in range(ks, len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
            continue
        plaintext += chr(ord("a") + ((ord(ciphertext[i]) - ord(plaintext[i - ks])) % 26))
    return plaintext
