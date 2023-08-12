# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 12/8/2023 11:20 am

from random import randint

def roll_dice(amount: int = 2 ) -> list[int]:
    # Hint the type of amount is int, and the default value 2 is assigned to amount.
    #If we call the function without an argument, the function will behave as we input "2" in it.
    #-> list[int] : Its still a hint. Not mandatory.
    if amount <= 0:
        raise ValueError
    #raise is commonly used for "judgement conditions" and requires an interrupt to handle.
    #In this case, user cannot type negative numbers.
    rolls: list[int] = []
    #Hint the type of rolls is list[int]
    for i in range(amount):
        random_roll: int = randint(1,6)
        rolls.append(random_roll)
    return rolls

def total_sum(all_roll_dice: list) -> int:
    total: int = sum(all_roll_dice)
    return total

def main():
    while True:
        try:
            user_input: str = input("How many dices would you like to roll?")

            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break
            rolls = roll_dice(int(user_input))
            #Every time, when we call roll_dice function, it will generate a new list of random dice rolls.
            #So if we want only one outcome, it's better to store the list into a variable.
            print(*rolls, sep=', ')
            # When we use *roll_dice(Its a list), it's equivalent to passing each element of the list as a separate argument to the function.
            # sep=', ' argument tells print to use a comma and a space to separate the items.
            print(f"The total sum is {total_sum(rolls)}.")
        except ValueError:
            #This will catch any non-integer inputs and the ValueError raised by the roll_dice function
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()