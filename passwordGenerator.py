from random import randint, choice, shuffle
import string

def passgen(password_lenght):
    number = int(password_lenght)
    if number < 12:
        return 'The minimum password length is 12 characters'
    password = ''
    i = 0
    while i < number:
        symbol = randint(0, 9)
        password += str(symbol)
        i += 1
        symbol = choice('!@#$%^&*()-+')
        password += str(symbol)
        i += 1
        symbol = choice(string.ascii_lowercase)
        password += str(symbol)
        i += 1
        symbol = choice(string.ascii_uppercase)
        password += str(symbol)
        i += 1
    password = list(password)
    shuffle(password)
    password = ''.join(password)
    return password[:number]

#password_lenght = input("Enter the password length: ")
#password = passgen(password_lenght)
#print(password)