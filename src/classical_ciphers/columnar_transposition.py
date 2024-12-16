from ..modern_ciphers.des import des_encrypt, des_decrypt

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def transposition_encrypt(plaintext: str, key: str = None) -> str:  # A
    if key is None:
        return plaintext

    plaintext = text_format(plaintext)
    ks = len(key)
    sorted_key = sorted((char, index) for index, char in enumerate(key))
    column_order = [original[1] for original in sorted_key]
    rows = [plaintext[i : i + len(key)] for i in range(0, len(plaintext), len(key))]
    if len(rows[-1]) < len(key):
        rows[-1] += "X" * (len(key) - len(rows[-1]))

    transposed = ["".join(row[i] for row in rows) for i in column_order]
    ciphertext = "".join(transposed)
    return ciphertext.replace("X", "")


def transposition_decrypt(ciphertext: str, key: str) -> str:
    if key is None:
        return ciphertext
    ciphertext = text_format(ciphertext)

    sorted_key = sorted((char, index) for index, char in enumerate(key))
    column_order = [original[1] for original in sorted_key]
    ks = len(key)

    col_size = len(ciphertext) // ks
    col_mod = len(ciphertext) % ks

    columns = [["X"] * (len(ciphertext) // ks + 1) for i in range(0, ks)]
    start = 0
    idx = 0
    for col in range(0, ks):
        for row in range(0, len(ciphertext) // ks + (column_order[col] < len(ciphertext) % ks)):
            columns[col][row] = ciphertext[idx]
            idx += 1

    rearranged_columns = [None] * ks
    for idx, col_idx in enumerate(column_order):
        rearranged_columns[col_idx] = columns[idx]

    plaintext = ""
    for i in range(col_size + (1 if col_mod > 0 else 0)):
        for column in rearranged_columns:
            if i < len(column):
                plaintext += column[i]

    return plaintext.replace("X", "")


def text_format(text: str) -> str:
    text = text.lower()
    text = "".join(char for char in text if char in ALPHABET)
    return text
