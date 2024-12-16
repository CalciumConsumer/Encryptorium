# TODO: debug and correct encrypt and decrypt
def railfence_encrypt(plaintext: str, rails: int) -> str:
    if rails < 1:
        raise ValueError("Number of rails must be greater than 0")
    if rails == 1:
        return plaintext

    plaintext = "".join(char for char in plaintext if char.isalnum())
    rail_pattern = [""] * rails
    rail = 0
    direction = 1

    for char in plaintext:
        rail_pattern[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(rail_pattern)


def railfence_decrypt(ciphertext: str, rails: int) -> str:
    if rails < 1:
        raise ValueError("Number of rails must be greater than 0")
    if rails == 1:
        return ciphertext

    n = len(ciphertext)
    rail_pattern = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(n):
        rail_pattern[rail].append(i)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    grid = [None] * n
    idx = 0
    for rail in rail_pattern:
        for pos in rail:
            grid[pos] = ciphertext[idx]
            idx += 1

    plaintext = []
    rail = 0
    direction = 1

    for i in range(n):
        plaintext.append(grid[i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(plaintext)
