def string2array(string: str):
    return [c for c in string]


STATIONARY_DISK = string2array("ABCDEFGILMNOPQRSTVXZ1234".lower())
MOVING_DISK = string2array("gklnprtuz&xysomqihfdbace")


def alberti_encrypt(
    plaintext: str,
    stationary_disk=STATIONARY_DISK,
    moving_disk=MOVING_DISK,
    period_increment: int = 1,
    period_length: int = 4,
    initial_shift: int = 0,
):
    if len(stationary_disk) != len(moving_disk):
        raise Exception("both disks must be the same size")
    if isinstance(stationary_disk, str):
        stationary_disk = string2array(stationary_disk)
    if isinstance(moving_disk, str):
        moving_disk = string2array(moving_disk)
    plaintext = plaintext.replace(" ", "")
    n = len(stationary_disk)
    idx = initial_shift
    placeof = {char: idx for idx, char in enumerate(stationary_disk)}
    print(placeof)
    ciphertext = ""
    for i, c in enumerate(plaintext):
        ciphertext += moving_disk[(placeof[c] + idx) % n]
        move = period_increment if i != 0 and (i + 1) % period_length == 0 else 0
        idx += move
        idx %= n

    return ciphertext


def alberti_decrypt(
    ciphertext: str,
    stationary_disk=STATIONARY_DISK,
    moving_disk=MOVING_DISK,
    period_increment: int = 1,
    period_length: int = 4,
    initial_shift: int = 0,
):
    if len(stationary_disk) != len(moving_disk):
        raise Exception("both disks must be the same size")
    if isinstance(stationary_disk, str):
        stationary_disk = string2array(stationary_disk)
    if isinstance(moving_disk, str):
        moving_disk = string2array(moving_disk)

    ciphertext = ciphertext.replace(" ", "")
    n = len(stationary_disk)
    idx = initial_shift % n
    plaintext = ""
    placeof = {char: idx for idx, char in enumerate(moving_disk)}
    for i, c in enumerate(ciphertext):
        plaintext += stationary_disk[(placeof[c] + idx) % n]
        move = period_increment if i != 0 and (i + 1) % period_length == 0 else 0
        idx -= move
        idx %= n

    return plaintext
