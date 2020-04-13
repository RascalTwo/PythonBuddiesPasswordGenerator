# I tried making a generator which would generate a comparatively easy to remember password
# This modifies the name and birth year and adds random numbers and variables to make it
# almost impossible to get the same output twice
# This is the best way I could come up with regarding the implementation
def passwordIncorporatesName(name, birth_year):
    import random

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = list(alphabet)  # Alphabets the program will choose from

    numbers = "1234567890"
    nums = list(numbers)    # Numbers the program will choose from

    special = "!@#$%^&*~"
    spec = list(special)   # Special characters the program will choose from

    while True:

        m = []  # Will store the users name
        n = []  # Will store the users birth year
        prefix = []
        suffix = []


    # If name is left blank below line will cause the program to restart

        if len(name) == 0:
            continue

        for letter in name:
            m.append(letter)



    # If birth year is left blank below line will cause the program to restart

        if len(birth_year) == 0:
            continue
        for digit in birth_year:
            n.append(digit)

    #modify certain letters to increase password strength

        if "0" in n:
            n[n.index("0")] = "O"
        if "9" in n:
            n[n.index("9")] = "P"
        if "8" in n:
            n[n.index("8")] = "B"
        if "3" in n:
            n[n.index("3")] = "E"

    # Modify certain characters to increase password strength

        if "a" in m:
            m[m.index("a")] = "@"
        if "S" in m:
            m[m.index("S")] = "$"
        if "i" in m:
            m[m.index("i")] = "!"
        if "c" in m:
            m[m.index("c")] = "("

    # Throughout this program I make use of several random variables to
    # decrease the possibility of getting same password twice

        rand2 = random.randrange(1,3,1) #random variable between 1 to 2
    # this random variable will decide how many characters will be case swapped


        for i in range(0,rand2):
            rand1 = random.randrange(0, len(name), 1) # random index number whose case will be swapped.

    # Below 4 line will result in swapping of cases

            if ord(m[rand1]) >= 97 and ord(m[rand1]) <= 122:
                m[rand1] = chr(ord(m[rand1]) - 32)
            elif ord(m[rand1]) >= 65 and ord(m[rand1]) <= 90:
                m[rand1] = chr(ord(m[rand1]) + 32)

        for i in range (0,random.randrange(4,6,1)): # 4-6 extra characters will be added
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

        password = "".join(prefix) + "".join(m) + "".join(n) + "".join(suffix)

    # If length of password is less than 6 , extra characters will be added to make it longer

        if len(password) < 6:
            for i in range(0,6-len(password)):
                flag_inc = random.randrange(0, 2,1) # Will decide if extra character is added to prefix or suffix

                if flag_inc == 1:
                    prefix.insert(random.randrange(0, len(prefix),1), random.choice(alpha))
                else:
                    suffix.insert(random.randrange(0, len(suffix),1), random.choice(alpha))

        flag_order = random.randrange(0,2) # Will decide the order of joining of different lists

        if flag_order == 0:
            password = "".join(prefix) + "".join(m) + "".join(n) + "".join(suffix)
        else:
            password = "".join(prefix) + "".join(n) + "".join(m) + "".join(suffix)

        return password