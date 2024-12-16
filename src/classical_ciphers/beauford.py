# the beaufort cipher is the brother to vigenere cipher
# instead of adding the char and the key it subtracts the char from the key


def beauford_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    plaintext = plaintext.replace(" ", "")
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord("a")
        k = ord(key[i % len(key)]) - ord("a")
        c = (k - p) % 26
        ciphertext += chr(c + ord("a"))
    return ciphertext


def beauford_decrypt(ciphertext: str, key: str) -> str:
    return beauford_encrypt(ciphertext, key)
