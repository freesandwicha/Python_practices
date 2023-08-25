# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 15/8/2023 10:08 am

import random
import sys

class RPS:
    def __init__(self):
        self.moves: dict = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        #Convert the key to list ['Rock', 'Paper', 'Scissor' ]
        self.user_win: int = 0   #instance variable to track user wins
        self.ai_win: int = 0   # instance variable to track ai wins
        #self.user_win and self.ai_win are instance attributes of the RPS class.
        #Each instance of RPS will have its own separate user_win and ai_win attributes.

    def play_game(self):
        user_move: str = input('Rock, Paper or Scissors : ').lower()

        if user_move == 'exit':
            print('Thanks for playing')
            sys.exit()
            #Exit the program.

        if user_move not in self.valid_moves:
            print('Invalid moves...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_game(user_move, ai_move)
        self.check_move(user_move, ai_move)


    def display_game(self, user_move, ai_move):
        print('---')
        print(f'You : {self.moves[user_move]}')
        print(f'AI : {self.moves[ai_move]}')
        print('---')

    def check_move(self, user_move, ai_move):

        if user_move == ai_move:
            print('It\'s a tie')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.user_win += 1
        # Just list all possible to win, the else situation will lose.
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.user_win += 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.user_win += 1
        else:
            print('AI wins...')
            self.ai_win += 1

        print(f'You have won {self.user_win} times, and AI have won {self.ai_win} times')

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
