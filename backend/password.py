from backend.BetterPassword import passwordIncorporatesName

class PasswordGenerator:
    def __init__(self, appropriateCharacters, passwordLength):
        self.appropriateCharacters = appropriateCharacters
        self.passwordLength = passwordLength

    def generateDefaultPassword(self, userName, birth_year):

        if int(birth_year) < 1975:
            password = passwordIncorporatesName(userName, birth_year)
            return password
        else:
            import random
            password = ''.join(random.choices(self.appropriateCharacters, k=self.passwordLength))
            return password