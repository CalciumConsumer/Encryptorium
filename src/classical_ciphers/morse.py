morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}


def morse_encrypt(message: str) -> str:
    message = message.upper()
    encrypted = []
    for c in message:
        if c in morse_dict:
            encrypted.append(morse_dict[c])
        else:
            encrypted.append("#")
    return " ".join(encrypted)


def morse_decrypt(encrypted: str) -> str:
    reverse_dict = {v: k for k, v in morse_dict.items()}
    encrypted = encrypted.split(" ")
    decrypted = []
    for c in encrypted:
        if c in reverse_dict:
            decrypted.append(reverse_dict[c])
        else:
            decrypted.append(c)
    return " ".join(decrypted)
