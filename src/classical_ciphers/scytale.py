def scytale_encrypt(plaintext: str, key: int) -> str:
    plaintext = plaintext.replace(" ", "").lower()  # Remove spaces and lowercase
    columns = [""] * key
    for i, char in enumerate(plaintext):
        columns[i % key] += char
    return "".join(columns)


def scytale_decrypt(ciphertext: str, key: int) -> str:
    n = len(ciphertext)
    rows = (n + key - 1) // key
    full_cols = n % key
    short_col_size = n // key
    plaintext = ""
    columns = []
    index = 0
    for col in range(key):
        col_size = short_col_size + (1 if col < full_cols else 0)
        columns.append(ciphertext[index : index + col_size])
        index += col_size
    for row in range(rows):
        for col in range(key):
            if row < len(columns[col]):
                plaintext += columns[col][row]

    return plaintext
