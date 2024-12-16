def generate_polybius_square(key: str) -> str:
    square = [["/"] * 5 for _ in range(0, 5)]
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    alphabet = "".join([c for c in alphabet if c not in key])
    alphabet = key + alphabet
    for i in range(0, 5):
        for j in range(0, 5):
            square[i][j] = alphabet[i * 5 + j]

    return square


def nihilist_encrypt(plaintext: str, polybius_key: str, key: str) -> str:
    plaintext = plaintext.lower().replace(" ", "")
    polybius_key = polybius_key.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    square = generate_polybius_square(polybius_key)
    placeof = {}
    for i in range(0, 5):
        for j in range(0, 5):
            placeof[square[i][j]] = (i + 1, j + 1)

    ciphertext = ""
    for i, c in enumerate(plaintext):
        grid_value = str(placeof[c][0]) + str(placeof[c][1])
        ki = i % len(key)
        key_grid_value = str(placeof[key[ki]][0]) + str(placeof[key[ki]][1])
        ciphertext += str(int(grid_value) + int(key_grid_value)) + " "
    return ciphertext.strip()


def nihilist_decrypt(ciphertext: str, polybius_key: str, key: str) -> str:
    numlist = ciphertext.split(" ")
    polybius_key = polybius_key.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    square = generate_polybius_square(polybius_key)
    placeof = {}
    for i in range(0, 5):
        for j in range(0, 5):
            placeof[square[i][j]] = (i + 1, j + 1)

    plaintext = ""
    for i, tup in enumerate(numlist):
        ki = i % len(key)
        key_grid_value = str(placeof[key[ki]][0]) + str(placeof[key[ki]][1])
        original_value = str(int(tup) - int(key_grid_value))
        (i, j) = int(original_value[0]) - 1, int(original_value[1]) - 1
        plaintext += square[i][j]
    return plaintext


# encry = nihilist_encrypt("DYNAMITE WINTER PALACE", "zebras", "russian")
# print(encry)
# print(nihilist_decrypt(encry, "zebras", "russian"))
