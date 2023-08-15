# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 11/8/2023 1:48 pm

#（1） How to use hint.
# (2) How to use f-string
def get_input(word_type: str):
    #Python's type hinting 'word_type' should be of type str (string)
    user_input: str = input(f"Enter a {word_type}:")
    #Python's type hinting (No constraint)
    # (1) We still can define other types.
    # (2) We don't need to write the data type(str) here
    return user_input


nount1 = get_input("noun")
adjective1 = get_input("adjective")
adjective2 = get_input("adjective")
verb1 = get_input("verb")
nount2 = get_input("noun")
verb2 = get_input("verb")

story = f'''

A long time ago, there were a {adjective1} {nount1} who loved to {verb1} all day.

One day, {adjective2} {nount2} found {nount1} in the park.

{nount2}: "Happy to see you"
{nount1}: "Me, too"
{nount2}: "I heard you prefer to {verb1} , is it right?"
{nount1}: "Yes, it really makes me happy. What about you?"
{nount2}: "I like to {verb2}, it sounds weired?"
{nount1}: "No. Thank you told me. Maybe we can {verb2} tomorrow."
{nount2}: "Great. See you tomorrow"
{nount1}: "See you tomorrow. But its time to {verb1} now. Bye."
{nount2}: "Bye."

'''

if __name__ == "__main__":
    print(story)
