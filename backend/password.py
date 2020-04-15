class PasswordGenerator:
    def __init__(self, appropriateCharacters, passwordLength):
        self.appropriateCharacters = appropriateCharacters
        self.passwordLength = passwordLength

    def generateDefaultPassword(self, userName, birth_year, length):

        if int(birth_year) < 1975:
            from backend.BetterPassword import passwordIncorporatesName
            password = passwordIncorporatesName(length, userName, birth_year)
            return password
        else:
            from backend.random_password import RandomGenerator
            generator = RandomGenerator
            password = RandomGenerator.generate(generator, length, "random", "random")
            return password