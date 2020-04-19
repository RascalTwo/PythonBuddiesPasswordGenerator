"""Generator of fully random passwords"""
import random

# pylint: disable=invalid-name
def passwordFullyRandom(length, digits, special):
    """Generate fully-random password"""
    letter_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_pool = '1234567890'
    special_pool = '!?-_@&%()[]{}'

    if length == "random":
        length = random.randint(6, 20)

    if digits == "random":
        digits = random.randint(0, length // 2)

    if special == "random":
        special = random.randint(0, length // 2)

    password = []

    for _ in range(length - digits - special):
        password.append(random.choice(letter_pool))

    for _ in range(digits):
        password.append(random.choice(digits_pool))

    for _ in range(special):
        password.append(random.choice(special_pool))

    random.shuffle(password)

    return ''.join(password)
