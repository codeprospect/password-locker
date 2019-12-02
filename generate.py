import string
import random

class Generator:

    passwords = []

    def __init__(self, media, account, g_password):
        self.media = media
        self.account = account
        self.password = g_password

    def save_passwords(self):
        Generator.passwords.append(self)

    @classmethod
    def password(cls, number):
        #arrays from which the password is picked from
        small = list(string.ascii_lowercase)
        capital = list(string.ascii_uppercase)
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        symbols = ["!", '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '/', '?', '~']
        combined = small + capital + numbers + symbols

        #first four combinations for the password
        first = random.choice(small) + random.choice(capital) + random.choice(numbers) + random.choice(symbols)
        first = list(first)
        # print(first)

        #rest of the password
        # print("Enter password length:")
        length = int(number)
        length = length - 4

        password = []

        for i in range(length):
            current = random.choice(combined)
            password.append(current)

        password = password + first
        random.shuffle(password)
        password = "".join(password)

        return password

    @classmethod
    def display_passwords(cls):
        return cls.passwords
