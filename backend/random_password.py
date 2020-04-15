def passwordFullyRandom(length, digits, special):
    letter_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_pool = '1234567890'
    special_pool = '!?-_@&%()[]{}'

    import random

    if length == "random":
        length = random.randint(6, 20)

    if digits == "random":
        digits = random.randint(0, length // 2)

    if special == "random":
        special = random.randint(0, length // 2)

    password = []

    for i in range(length - digits - special):
        password.append(random.choice(letter_pool))

    for i in range(digits):
        password.append(random.choice(digits_pool))

    for i in range(special):
        password.append(random.choice(special_pool))

    random.shuffle(password)

    return ''.join(password)
