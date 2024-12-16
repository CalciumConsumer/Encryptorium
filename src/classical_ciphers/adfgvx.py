table_dict = {
    "a": 0,
    "d": 1,
    "f": 2,
    "g": 3,
    "v": 4,
    "x": 5,
}
inv_table_dict = {k: v for v, k in table_dict.items()}

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def generate_polybius_square(key: str) -> list:
    key = "".join(dict.fromkeys(key))
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    alphabet = key + "".join([c for c in alphabet if c not in key])
    square = [["/"] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            square[i][j] = alphabet[i * 6 + j]
    return square


def adfgvx_encrypt(plaintext: str, polybius_key: str, transposition_key: str = "") -> str:
    plaintext = text_format(plaintext)
    polybius_key = text_format(polybius_key)
    transposition_key = text_format(transposition_key)
    square = generate_polybius_square(polybius_key)

    placeof = {}
    for i in range(6):
        for j in range(6):
            placeof[square[i][j]] = inv_table_dict[i] + inv_table_dict[j]

    try:
        ciphertext = "".join([placeof[c] for c in plaintext])
    except KeyError:
        raise ValueError("Plaintext contains characters not in the Polybius square.")

    if not transposition_key:
        return ciphertext

    col_order = sorted([(c, i) for i, c in enumerate(transposition_key)])
    sorted_indices = [idx for _, idx in col_order]

    columns_table = [
        ciphertext[i : i + len(transposition_key)] for i in range(0, len(ciphertext), len(transposition_key))
    ]
    if len(columns_table[-1]) < len(transposition_key):
        columns_table[-1] += "X" * (len(transposition_key) - len(columns_table[-1]))

    transposed_columns = ["".join(row[idx] for row in columns_table) for idx in sorted_indices]
    final_ciphertext = "".join(transposed_columns)
    return final_ciphertext.replace("X", "")


def adfgvx_decrypt(ciphertext: str, polybius_key: str, transposition_key: str) -> str:
    ciphertext = text_format(ciphertext)
    polybius_key = text_format(polybius_key)
    transposition_key = text_format(transposition_key)

    col_order = sorted([(c, i) for i, c in enumerate(transposition_key)])
    rev_col_order = [(c, i) for i, c in enumerate(transposition_key)]
    sorted_indices = [idx for _, idx in col_order]
    rev_sorted_indices = [idx for _, idx in rev_col_order]
    square = generate_polybius_square(polybius_key)

    n = len(transposition_key)
    columns_table = [["X"] * (len(ciphertext) // n + 1) for i in range(0, n)]
    idx = 0
    for col in range(0, n):
        for row in range(0, len(ciphertext) // n + (sorted_indices[col] < len(ciphertext) % n)):
            columns_table[col][row] = ciphertext[idx]
            idx += 1

    transposed_columns = ""
    for cols in range(0, len(ciphertext) // n + 1):
        for rows in col_order:
            transposed_columns += columns_table[rows[1]][cols]
    untranslated = transposed_columns.replace("X", "")
    plaintext = ""
    for i in range(0, len(untranslated), 2):
        plaintext += square[table_dict[untranslated[i]]][table_dict[untranslated[i + 1]]]
    return plaintext


def text_format(text: str) -> str:
    text = text.lower()
    text = "".join(char for char in text if char in ALPHABET)
    return text
