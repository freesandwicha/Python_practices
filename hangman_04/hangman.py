# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 14/8/2023 8:31 pm

#The simple welcome for any users. Users need to guess the word via typing letters. 
from random import choice

def run_game():

    word_list: list = ['apple', 'secret', 'sun']
    word: str = choice(word_list)
    # Get a word from the list
    name: str = input('Please enter your name')
    print('Welcome %s to this game.' % name)
    print(f'Welcome {name} to this game')
    count: int = 6
    guessed: str = ''
    # The guessed string will store letters that the player has guessed so far.

    while count > 0:
        blanks: int = 0
        print('Word: ', end='')
        for char in word:
        #Check if there were a letter in the word which user needs to guess.
        #In every loop, the char will represent a letter.
            if char in guessed:
            #This if statement checks if the current character (char) is present in the guessed string.
                print(char, end='')
            #If the user guesses the right letter, it will print it without blank
            else:
            #From the beginning, since the user has entered nothing, this judgement is entered.
                print('_', end='')
                blanks += 1
                #Every time it prints a '_' that means one char is not in the word.
        print()

        if blanks == 0:
            print("You got it")
            break

        user_guess: str = input('Please enter a letter')
        if user_guess in guessed:
            # This line checks if the letter the user has just guessed (user_guess) is already present in the string guessed
            print(f'You already use: {user_guess}. Please try with another letter!')
            continue
            #It skips the rest of the loop's current iteration and jumps to the beginning of the next iteration

        guessed += user_guess
        if user_guess not in word:
            count -= 1
            print(f"Your letter {user_guess} is not in the word. Please try another letter! But you only have {count} times.")

            if count == 0:
                print("You don't have enough time to try... You lose.")
                break


if __name__ == '__main__':
    run_game()
