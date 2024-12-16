# must be run from root
# (pytest) from root
import pytest

from src.classical_ciphers import *
from src.modern_ciphers.des import des_encrypt, des_decrypt

BOOK_STRINGS = [
    "Not all those who wander are lost.",
    "It was the best of times, it was the worst of times.",
    "Winter is coming.",
    "Fear is the mind-killer.",
    "So it goes.",
    "The answer to the ultimate question of life, the universe, and everything is 42.",
    "Call me Ishmael.",
    "Big Brother is watching you.",
    "All animals are equal, but some animals are more equal than others.",
    "We accept the love we think we deserve.",
]

SHOW_STRINGS = [
    "How you doin'?",
    "I am the one who knocks!",
    "Bazinga!",
    "The night is dark and full of terrors.",
    "Live long and prosper.",
    "D'oh!",
    "I am vengeance, I am the night, I am Batman!",
    "Clear eyes, full hearts, can't lose.",
    "I have a cunning plan.",
    "To infinity and beyond!",
]

ALL_STRINGS = SHOW_STRINGS + BOOK_STRINGS

KEYS = [
    "Albus Dumbledore",
    "The Force",
    "Winterfell",
    "Green Lantern",
    "Mandalorian Creed",
    "Hogwarts Legacy",
    "Sherlock Holmes",
    "Dark Knight",
    "Ring of Power",
    "The One Ring",
    "Invisible Man",
    "Stranger Things",
    "Iron Throne",
    "Redemption Song",
    "Sith Lord",
    "Middle Earth",
    "Elder Wand",
    "Secret Passage",
    "Dark Phoenix",
    "Narnia",
]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

STRNUM = [
    ("hello world", 5),
    ("scytale cipher", 7),
    ("railfence cipher", 5),
    ("sunset over the hills", 5),
    ("mysterious fog in the valley", 3),
    ("whale songs in the ocean", 7),
    ("crackling fire in the hearth", 2),
    ("morning dew on the grass", 4),
    ("ancient trees in the forest", 6),
    ("distant thunder in the sky", 1),
    ("quiet stream in the meadow", 8),
    ("frosty air on a winter morning", 9),
    ("whispers through the trees", 10),
    ("the scent of pine in the air", 3),
    ("clouds drifting across the sky", 6),
    ("stars twinkling in the night", 5),
    ("gentle breeze on a summer day", 2),
    ("mountain peaks under the moon", 7),
    ("footsteps in the snow", 4),
    ("light rain on the city streets", 8),
    ("a lone wolf in the wilderness", 9),
    ("soft hum of a quiet town", 1),
    ("dandelions floating in the wind", 10),
]


def only_alpha(message: str) -> str:
    return "".join(c for c in message if c in ALPHABET)


def rm_spaces(message: str) -> str:
    return message.replace(" ", "")


ALL_ZIP = [(message, key) for message, key in zip(ALL_STRINGS, KEYS)]


@pytest.mark.parametrize(
    "message, a, b",
    [
        ("hello world", 5, 8),
        ("affine cipher", 7, 3),
        ("sunrise over the mountains", 3, 7),
        ("ancient ruins in the desert", 5, 2),
        ("quiet night in the forest", 9, 4),
        ("running through the rain", 11, 5),
        ("dreams of distant places", 7, 3),
        ("deep blue ocean waves", 15, 6),
        ("stormy weather ahead", 15, 9),
        ("whispers in the dark", 17, 5),
        ("a walk on the beach", 19, 8),
        ("fading light of the sunset", 23, 6),
        ("city lights at midnight", 25, 2),
        ("across the endless fields", 3, 10),
        ("mystery in the old mansion", 7, 7),
        ("hidden paths through the woods", 9, 4),
        ("the sound of a distant train", 11, 6),
        ("lost in the vast desert", 17, 8),
        ("dancing under the stars", 5, 3),
        ("echoes of forgotten songs", 15, 7),
        ("cold winds of winter", 19, 4),
        ("a moment of silence", 23, 1),
    ],
)
def test_affine(message, a, b):
    encrypted = affine_encrypt(message, a, b)
    decrypted = affine_decrypt(encrypted, a, b)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message",
    ALL_STRINGS,
)
def test_atbash(message):
    encrypted = atbash_encrypt(message)
    decrypted = atbash_decrypt(encrypted)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, key",
    ALL_ZIP,
)
def test_autokey(message, key):
    message = only_alpha(message).lower()
    encrypted = autokey_encrypt(message, key)
    decrypted = autokey_decrypt(encrypted, key)
    assert rm_spaces(message).lower() == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, shift",
    STRNUM,
)
def test_caesar(message, shift):
    message = only_alpha(message.lower())
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, key",
    ALL_ZIP,
)
def test_columnar_transposition(message, key):
    encrypted = transposition_encrypt(message, key)
    decrypted = transposition_decrypt(encrypted, key)
    assert only_alpha(rm_spaces(message).lower()) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message",
    ALL_STRINGS,
)
def test_morse(message):
    message = only_alpha(message).lower()
    encrypted = morse_encrypt(message)
    decrypted = morse_decrypt(encrypted)
    assert rm_spaces(message).upper() == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, rails",
    STRNUM,
)
def test_railfence(message, rails):
    encrypted = railfence_encrypt(message, rails)
    decrypted = railfence_decrypt(encrypted, rails)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, key",
    STRNUM,
)
def test_scytale(message, key):
    encrypted = scytale_encrypt(message, key)
    decrypted = scytale_decrypt(encrypted, key)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, key",
    ALL_ZIP,
)
def test_vigenere(message, key):
    message = only_alpha(message.lower())
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message",
    ALL_STRINGS,
)
def test_xor(message):
    key = genkey(len(message))
    encrypted = xor_encrypt(message, key)
    decrypted = xor_decrypt(encrypted, key)
    assert rm_spaces(message) == rm_spaces(decrypted)


@pytest.mark.parametrize(
    "message, key",
    ALL_ZIP,
)
def test_beauford(message, key):
    message = only_alpha(message).lower()
    encrypted = beauford_encrypt(message, key)
    decrypted = beauford_decrypt(encrypted, key)
    assert rm_spaces(message) == rm_spaces(decrypted)
