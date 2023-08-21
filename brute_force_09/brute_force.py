# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 21/8/2023 11:33 am

import itertools
import string
import time

def common_guess(word: str) -> str | None:
    #This function checks if the given word (password) is present in the words.txt file.
    with open('words.txt','r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            #If the word is found, it returns a formatted string indicating the word and its position in the list.
            return f'Common match: {match} (#{i}) '


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    # This function tries to brute-force crack the given word (password) using the specified character set.
    chars: str = string.ascii_lowercase

    if digits:
        #We can use bool to control if we need to put digits.
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        #Using itertools.product(), all possible combinations of the specified length are tried.
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'

        # print(guess, attempts)

def main():
    print('Searching...')
    password: str = 'bbbb'
    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        #It first tries to find the password in words.txt using the common_guess function.
        print(common_match)
    else:
        for i in range(3, 5):
            if cracked := brute_force(password, i, digits=True, symbols=True):
                #If not found, it then uses the brute_force function for password lengths from 3 to 4 ).
                print(cracked)
            else:
                print('There was no match...')

    end_time: float =time.perf_counter()
    print(round(end_time - start_time, 2), 's')

if __name__ == '__main__':
    main()
