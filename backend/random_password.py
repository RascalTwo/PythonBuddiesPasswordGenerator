class RandomGenerator:
    def __init__(self):
        pass


    def generate(self, length, digits, special):
        self.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '1234567890'
        self.special = '!?-_@&%()[]{}'

        import random

        if length == "random":
            length = random.randint(6, 20)
        
        if digits == "random":
            digits = random.randint(0, length // 2)

        if special == "random":
            special = random.randint(0, length // 2)

        password = []
        
        for i in range(length - digits - special):
            password.append(random.choice(self.letters))

        for i in range(digits):
            password.append(random.choice(self.digits))

        for i in range(special):
            password.append(random.choice(self.special))

        random.shuffle(password)

        return ''.join(password)

        