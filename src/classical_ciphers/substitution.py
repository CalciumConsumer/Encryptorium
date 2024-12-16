sbox = {
    "a": "c",
    "b": "z",
    "c": "f",
    "d": "k",
    "e": "m",
    "f": "p",
    "g": "s",
    "h": "q",
    "i": "r",
    "j": "t",
    "k": "u",
    "l": "v",
    "m": "w",
    "n": "x",
    "o": "y",
    "p": "e",
    "q": "a",
    "r": "b",
    "s": "d",
    "t": "h",
    "u": "i",
    "v": "v",
    "w": "l",
    "x": "n",
    "y": "o",
    "z": "g",
}


def substitution_encrypt(text: str) -> str:
    encrypted_text = ""
    for c in text:
        if c.isalpha() and c.lower() in "abcdefghijklmnopqrstuvwxyz":
            if not c.islower():
                c = c.lower()
            encrypted_text += sbox[c]
        else:
            encrypted_text += c
    return encrypted_text


def substitution_decrypt(encrypted: str) -> str:
    reverse_substitution = {v: k for k, v in sbox.items()}
    original = ""
    for c in encrypted:
        if c.isalpha() and c.lower() in "abcdefghijklmnopqrstuvwxyz":
            if not c.islower():
                c = c.lower()
            original += reverse_substitution[c]
        else:
            original += c
    return original
