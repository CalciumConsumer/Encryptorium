# DES - Data Encryption Standard
# see https://en.wikipedia.org/wiki/Data_Encryption_Standard
#     https://en.wikipedia.org/wiki/DES_supplementary_material

# DES is a symmetric key cipher/algorithm, it has been highly influencial in modern cryptography,
# DES is the predecessor of AES and as of modern day has been superceded by AES.
# DES is insecure due to the relatively short 56-bit key size, the small keysize makes it vulnerable to brute-force attacks
#

import struct

# fmt: off
IP = [
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8,  0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
]

IP_INV = [
    39, 7,  47, 15, 55, 23, 63, 31,
    38, 6,  46, 14, 54, 22, 62, 30,
    37, 5,  45, 13, 53, 21, 61, 29,
    36, 4,  44, 12, 52, 20, 60, 28,
    35, 3,  43, 11, 51, 19, 59, 27,
    34, 2,  42, 10, 50, 18, 58, 26,
    33, 1,  41, 9,  49, 17, 57, 25,
    32, 0,  40, 8,  48, 16, 56, 24,
]

E = [
    31, 0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9,  10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0,
]

P = [
    15, 6,  19, 20, 28, 11, 27, 16,
    0,  14, 22, 25, 4,  17, 30, 9,
    1,  7,  23, 13, 31, 26, 2,  8,
    18, 12, 29, 5,  21, 10, 3,  24,
]

PC1 = [
    56, 48, 40, 32, 24, 16, 8,
    0,  57, 49, 41, 33, 25, 17,
    9,  1,  58, 50, 42, 34, 26,
    18, 10, 2,  59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6,  61, 53, 45, 37, 29, 21,
    13, 5,  60, 52, 44, 36, 28,
    20, 12, 4,  27, 19, 11, 3,
]

PC2 = [
    13, 16, 10, 23, 0,  4,
    2,  27, 14, 5,  20, 9,
    22, 18, 11, 3,  25, 7,
    15, 6,  26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31,
]

SBOX = [
    [
        14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7,
        0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8,
        4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0,
        15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13,
    ],
    [
        15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10,
        3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5,
        0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15,
        13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9,
    ],
    [
        10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8,
        13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1,
        13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7,
        1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12,
    ],
    [
        7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15,
        13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9,
        10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4,
        3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14,
    ],
    [
        2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9,
        14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6,
        4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14,
        11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3,
    ],
    [
        12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11,
        10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8,
        9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6,
        4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13,
    ],
    [
        4,  11,  2, 14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1,
        13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6,
        1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2,
        6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12,
    ],
    [
        13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7,
        1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2,
        7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8,
        2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11,
    ],
]

ROTATES = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
# fmt: on


def des_encrypt(plaintext, key, pad=1, iv=None):
    """
    has a pad option if plaintext cannot be divided to block of 8 bytes
    has initialization vector for cbc mode
    """

    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    if isinstance(key, str):
        key = key.encode()
    plaintext, key = ensure_type(plaintext, key)
    key = split_key(key)
    if pad and len(plaintext) % 8 != 0:
        plaintext = pad_message(plaintext)
    return encipher_all(plaintext, key, pad, iv, 1)


def des_decrypt(ciphertext, key, pad=1, iv=None):
    """
    has a pad option if ciphertext was padded
    has initialization vector for cbc mode
    """
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode()
    if isinstance(key, str):
        key = key.encode()
    ciphertext, key = ensure_type(ciphertext, key)
    key = split_key(key)
    return encipher_all(ciphertext, key, pad, iv, 0)


def ensure_type(text, key):
    """
    checks and or converts the type of text and key to bytes
    """
    if isinstance(key, bytearray):
        key = bytes(key)
    if isinstance(text, bytearray):
        text = bytes(text)

    if not isinstance(key, bytes):
        raise Exception("key should be of byte-like type")
    if len(key) != 8:
        raise Exception("key length must be 8 bytes")
    return text, key


def split_key(key):
    """splits key into the 16 subkeys"""
    key0, key1, key2 = key[:8], key[8:16], key[16:]
    if key1 == key2:
        return (tuple(make_keys(key0)),)

    key2 = key2 or key0
    if key1 == key0:
        return (tuple(make_keys(key2)),)

    return tuple(tuple(make_keys(key)) for key in (key0, key1, key2))


def pad_message(message):
    """pads message according to PKCS#5 padding(same as PKCS#7 padding)"""
    length = len(message)
    pad_length = 8 - len(message)
    padding = bytes([pad_length] * pad_length)
    return message + padding
    # return message.ljust(length + 8 >> 3 << 3, chr(8 - (length & 7)).encode())


def encipher_all(text, key, pad, iv, is_encrypting):
    """encrypt or decrypt a text based on key, pad, initial vector and a bool is_encrypting"""
    if isinstance(text, bytes) or isinstance(text, bytearray):
        # unpack text to 8 bytes blocks as unsigned long long
        blocks = (struct.unpack(">Q", text[i : i + 8])[0] for i in range(0, len(text), 8))
    else:
        raise ValueError("text must be byte like")
    if iv is None:
        encoded_blocks = ecb(blocks, key, is_encrypting)
    else:
        encoded_blocks = cbc(blocks, key, iv, is_encrypting)

    ret = b"".join(struct.pack(">Q", block) for block in encoded_blocks)
    return ret[: -ord(ret[-1:])] if not is_encrypting and pad else ret


def make_keys(key):
    """makes the 16 subkeys"""
    (key,) = struct.unpack(">Q", key)
    next_key = permute(key, 64, PC1)
    next_key = next_key >> 28, next_key & 0x0FFFFFFF
    for bits in ROTATES:
        next_key = left_shift(next_key[0], bits), left_shift(next_key[1], bits)
        yield permute(next_key[0] << 28 | next_key[1], 56, PC2)
    return


def left_shift(half_key, rot):
    """left shifts by rot with a warp around"""
    return half_key << rot & 0x0FFFFFFF | half_key >> 28 - rot


def permute(data, bits, table):
    """permute and expand data based on a table"""
    perm = 0
    for i, v in enumerate(table):
        if data & 1 << bits - 1 - v:
            perm |= 1 << len(table) - 1 - i
    return perm


def ecb(blocks, key, is_encrypting):
    """Electronic codebook mode"""
    for block in blocks:
        yield encipher(block, key, is_encrypting)


def cbc(blocks, key, iv, is_encrypting):
    """Cipher block chaining"""
    if is_encrypting:
        for block in blocks:
            iv = encipher(block ^ iv, key, is_encrypting)
            yield iv

    else:
        for block in blocks:
            iv, block = block, iv ^ encipher(block, key, is_encrypting)
            yield block


def encipher(block, key, is_encrypting):
    for k in key:
        block = encipher_block(block, k, is_encrypting)
    return block


def encipher_block(block, keys, is_encrypting):
    """encodes or decodes a block with subkeys"""
    block = permute(block, 64, IP)
    block = block >> 32, block & 0xFFFFFFFF

    if not is_encrypting:
        keys = reversed(keys)
    for key in keys:
        block = block[1], block[0] ^ feistel(block[1], key)

    return permute(block[1] << 32 | block[0], 64, IP_INV)


def feistel(block, key):
    """des feistel function"""
    block = permute(block, 32, E) ^ key
    data = 0
    for i, box in enumerate(SBOX):
        # six bytes to be converted in SBOX
        i6 = block >> 42 - i * 6 & 0x3F
        # weird voodoo indexing
        box_idx = i6 & 0x20 | (i6 & 0x01) << 4 | (i6 & 0x1E) >> 1
        data = data << 4 | box[box_idx]
    return permute(data, 32, P)
