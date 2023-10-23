from random import randint

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'


def generate_abstract_username(length=12):
    username = ''
    while len(username) < length:
        if len(username) % 2 == 0:
            username += (letters[randint(0, len(letters) - 1)])
        else:
            username += (str(randint(0, 9)))

    return username


def generate_password(length=8):
    password = ''
    while len(password) < length:
        if len(password) % 2 == 0:
            password += (letters[randint(0, len(letters) - 1)])

        elif len(password) % 3 == 0:
            password += (symbols[(randint(0, len(symbols) - 1))])
        else:
            password += (str(randint(0, 9)))

    return password


if __name__ == "__main__":
    name = generate_abstract_username()
    print(name)
    password = generate_password()
    print(password)
