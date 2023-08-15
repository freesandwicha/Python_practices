# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 15/8/2023 11:28 am

import string
import secrets
#Get a secure number

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

#print(string.punctuation, string.ascii_lowercase)

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits
    #'abcdefghijklmnopqrstuvwxyz0123456789'
    #combination is a string that contains all possible characters that can be part of the password
    # (like lowercase alphabets, digits, punctuation symbols(If True), etc., based on the previous logic in the function).

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
        #The secrets.randbelow function generates a random integer from 0 (inclusive) to combination_length (exclusive)
        #combination[secrets.randbelow(combination_length)]: This line randomly selects a character from the combination string
        if uppercase and not any(char.isupper() for char in new_password):
            #The any() function will return True if at least one character in new_password is uppercase
            #not any means there is no uppercase in new_password.
            random_position = secrets.randbelow(length)
            #This line selects a random index position(Must below length) within the new_password string. It's where we'll insert an uppercase character.
            random_upper_char = secrets.choice(string.ascii_uppercase)
            #We're choosing a random uppercase character from the set of all uppercase ASCII characters.
            new_password = new_password[:random_position] + random_upper_char + new_password[random_position + 1:]
            # insert the random_upper_char at the random_position in the new_password.
    return new_password


if __name__ == '__main__':
     for i in range(1,6):
         new_pass: str = generate_password(2,True,True)
         specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}'
         print(f'{i} -> {new_pass}({specs})')

