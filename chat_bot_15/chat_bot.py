# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 26/8/2023 1:29 pm

from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict ) -> str | None:
    questions: list[str] = [q for q in questions]
    matchers: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matchers:
        return matchers[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('''Bot: I don't understand ''')



if __name__ == '__main__':
    brain: dict = {'hello': 'Hey',
                   'How are you? ': 'Good.',
                   'What time is it ':'Don\'t know, don\'t care... ',
                   'bye':'See you!'
                  }
    #Here, we can use json to make the conversation richer.

    chat_bot(brain)
