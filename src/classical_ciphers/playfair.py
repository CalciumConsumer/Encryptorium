def polybius_square(key: str, char_locations: dict):
    square = [["|"] * 5 for _ in range(5)]
    key = key.lower().replace(" ", "")
    key = "".join(dict.fromkeys(key))
    letters = "abcdefghiklmnopqrstuvwxyz"
    letters = "".join(c for c in letters if c not in key)
    k = 0

    for char in key:
        char_locations[char] = (k // 5, k % 5)
        square[k // 5][k % 5] = char
        k += 1

    for char in letters:
        char_locations[char] = (k // 5, k % 5)
        square[k // 5][k % 5] = char
        k += 1

    return square


def playfair_encrypt(plaintext: str, key: str) -> str:
    char_locations = {}
    square = polybius_square(key, char_locations)
    plaintext = plaintext.lower().replace(" ", "").replace("j", "i")
    ciphertext = ""
    i = 0

    while i < len(plaintext):
        first = plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i + 1] != first:
            second = plaintext[i + 1]
            i += 2
        else:
            second = "x"
            i += 1

        (x1, y1) = char_locations[first]
        (x2, y2) = char_locations[second]

        if x1 == x2:
            ciphertext += square[x1][(y1 + 1) % 5] + square[x2][(y2 + 1) % 5]
        elif y1 == y2:
            ciphertext += square[(x1 + 1) % 5][y1] + square[(x2 + 1) % 5][y2]
        else:
            ciphertext += square[x1][y2] + square[x2][y1]

    return ciphertext


def playfair_decrypt(ciphertext: str, key: str) -> str:
    char_locations = {}
    square = polybius_square(key, char_locations)
    i = 0
    plaintext = ""
    while i < len(ciphertext) - 1:
        first = ciphertext[i]
        second = ciphertext[i + 1]
        i += 2
        (x1, y1) = char_locations[first]
        (x2, y2) = char_locations[second]

        if x1 == x2:
            plaintext += square[x1][(y1 - 1) % 5] + square[x2][(y2 - 1) % 5]
        elif y1 == y2:
            plaintext += square[(x1 - 1) % 5][y1] + square[(x2 - 1) % 5][y2]
        else:
            plaintext += square[x1][y2] + square[x2][y1]
    return plaintext
