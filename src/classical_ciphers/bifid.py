def generate_polybius_square(key: str) -> str:
    square = [["/"] * 5 for _ in range(0, 5)]
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    alphabet = "".join([c for c in alphabet if c not in key])
    alphabet = key + alphabet
    for i in range(0, 5):
        for j in range(0, 5):
            square[i][j] = alphabet[i * 5 + j]

    return square


def bifid_encrypt(plaintext: str, polybius_key: str) -> str:
    plaintext = plaintext.lower().replace(" ", "")
    polybius_key = polybius_key.lower().replace(" ", "")

    square = generate_polybius_square(polybius_key)
    pairs = []
    placeof = {}
    for i in range(5):
        for j in range(5):
            placeof[square[i][j]] = (i + 1, j + 1)

    for c in plaintext:
        pairs.append(placeof[c])

    row1 = "".join(str(pair[0]) for pair in pairs)
    row2 = "".join(str(pair[1]) for pair in pairs)
    cipher_numbers = row1 + row2
    ciphertext = ""
    for i in range(0, len(cipher_numbers), 2):
        idx = int(cipher_numbers[i]) - 1
        jdx = int(cipher_numbers[i + 1]) - 1
        ciphertext += square[idx][jdx]
    return ciphertext


def bifid_decrypt(ciphertext: str, polybius_key: str) -> str:
    ciphertext = ciphertext.lower().replace(" ", "")
    polybius_key = polybius_key.lower().replace(" ", "")
    square = generate_polybius_square(polybius_key)
    placeof = {}
    for i in range(5):
        for j in range(5):
            placeof[square[i][j]] = (i + 1, j + 1)
    cipher_numbers = ""
    for c in ciphertext:
        cipher_numbers += str(placeof[c][0]) + str(placeof[c][1])
    pairs = []
    mid = len(cipher_numbers) // 2
    for i in range(0, mid):
        pair = (int(cipher_numbers[i]), int(cipher_numbers[i + mid]))
        pairs.append(pair)
    plaintext = ""
    for pair in pairs:
        idx = pair[0] - 1
        jdx = pair[1] - 1
        plaintext += square[idx][jdx]
    return plaintext
