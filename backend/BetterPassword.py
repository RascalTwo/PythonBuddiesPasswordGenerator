# Generates easy to remember password
def passwordIncorporatesName(length, name, birth_year):
    import random

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = list(alphabet)  # Alphabets the program will choose from

    numbers = "1234567890"
    nums = list(numbers)    # Numbers the program will choose from

    special = "!@#$%^&*~"
    spec = list(special)   # Special characters the program will choose from


    user_name = []
    birth_year = []
    prefix = []
    suffix = []

    for letter in name:
        user_name.append(letter)

    for digit in birth_year:
        birth_year.append(digit)

    #modify certain letters to increase password strength

    if "0" in birth_year:
        birth_year[birth_year.index("0")] = "O"
    if "9" in birth_year:
        birth_year[birth_year.index("9")] = "P"
    if "8" in birth_year:
        birth_year[birth_year.index("8")] = "B"
    if "3" in birth_year:
        birth_year[birth_year.index("3")] = "E"

    # Modify certain characters to increase password strength

    if "a" in user_name:
        user_name[user_name.index("a")] = "@"
    if "S" in user_name:
        user_name[user_name.index("S")] = "$"
    if "i" in user_name:
        user_name[user_name.index("i")] = "!"
    if "c" in user_name:
        user_name[user_name.index("c")] = "("

    # decrease the possibility of getting same password twice
    # this random variable will decide how many characters will be case swapped

    rand2 = random.randrange(1,3,1) #random variable between 1 to 2

    for i in range(0,rand2):
        rand1 = random.randrange(0, len(name), 1) # random index number whose case will be swapped.

        # Below 4 line will result in swapping of cases

        if ord(user_name[rand1]) >= 97 and ord(user_name[rand1]) <= 122:
            user_name[rand1] = chr(ord(user_name[rand1]) - 32)
        elif ord(user_name[rand1]) >= 65 and ord(user_name[rand1]) <= 90:
            user_name[rand1] = chr(ord(user_name[rand1]) + 32)

    for i in range(length - len(user_name) - len(birth_year)): # 4-6 extra characters will be added
        flag_list = random.randrange(0,3,1) # Will decide whether extra character will be a prefix or suffix
        flag_char = random.randrange(0,2,1) # Will decide if extra character is a number or special character

        if flag_list == 0:
            if flag_char == 0:
                prefix.append(random.choice(nums))
            else:
                prefix.append(random.choice(spec))

        if flag_list == 1:
            if flag_char == 0:
                suffix.append(random.choice(nums))
            else:
                suffix.append(random.choice(spec))

    password = "".join(prefix) + "".join(user_name) + "".join(birth_year) + "".join(suffix)

    # If length of password is less than variable length , extra characters will be added to make it longer

    if len(password) < length:
        for i in range(0,length-len(password)):
            flag_inc = random.randrange(0, 2,1) # Will decide if extra character is added to prefix or suffix

            if flag_inc == 1:
                prefix.insert(random.randrange(0, len(prefix),1) if prefix else 0, random.choice(alpha))
            else:
                suffix.insert(random.randrange(0, len(suffix),1) if suffix else 0, random.choice(alpha))

    flag_order = random.randrange(0,2) # Will decide the order of joining of different lists

    if flag_order == 0:
        password = "".join(prefix) + "".join(user_name) + "".join(birth_year) + "".join(suffix)
    else:
        password = "".join(prefix) + "".join(birth_year) + "".join(user_name) + "".join(suffix)

    return password
