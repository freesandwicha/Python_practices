# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 21/8/2023 10:51 am

def check_password(password: str):
    if not password.strip():
        #string means True. Blank means False.
        #if not password.strip(): means the password is empty.
        print("Password cannot be empty!")
        return

    with open('password.txt', 'r') as file:
         common_passwords: list[str] = file.read().splitlines()
         # print(common_passwords)
         #file.read().splitlines() reads the entire file and then splits it into lines, returning a list of lines from the file

    for i, common_password in enumerate(common_passwords, start=1):
        #enumerate is a built-in function that returns both the index (i) and the value (common_password) as we loop through a list.
        # The start=1 argument means the indexing starts from 1 instead of the default 0.
        if password == common_password:
            print(f'{password}: X (#{i})')
            # If the inputted password matches any password in the common_passwords list,
            # the function prints the password with an "X" next to it and its position in the list 
            # (indicating it's a commonly used password).
            return

    print(f'{password}：* unique.')


def main():
    while True:
        user_password = input('Please enter your password: ')
        check_password(f'{user_password}')


if __name__ == '__main__':
    main()
