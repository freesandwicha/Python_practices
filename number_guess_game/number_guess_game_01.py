# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 11/8/2023 3:51 pm

#The main funciton: users need to guese a number from lower  to higher. But they just have three times.
from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)


def guess_number():
    print(f"Guess the name in the range from {lower_num} to {higher_num}")
    count = 0
    value = 3
    while value > 0:
        try:
            user_number = int(input("Guess : "))

        except ValueError as e :
            print("Please enter an integer.")
            continue
            #Continue won't execute the data after continue. Go back to the start of while:
        value -= 1  # 2 1 0
        count += 1  # 1 2 3
        if user_number < random_number:
            print("Your number is lower...")
        elif user_number > random_number:
            print("Your number is higher...")
        else:
            print("You got it.")
            break
            #Break will jump from this loop.
    else:
        print("Sorry, you just has three chances.")



if __name__ == "__main__":
    guess_number()
