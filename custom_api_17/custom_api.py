# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 29/8/2023 10:29 am

from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['You are good!', 'I am good!', 'We are good!']
    return {'phrases': choice(phrases),
            'datatime': datetime.now()}

@app.route('/api/random')
def random():
    number_input = request.args.get('number', type=int)
    text_input = request.args.get('text', type=str, default='default-text')

    if isinstance(number_input, int):
        return {
            'input': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'data': datetime.now()
        }
    else:
        return {'Error': 'Please only enter numbers'}

if __name__ == '__main__':
    app.run()


Then we can use www.pythonanywhere.com to publish our api. In the future, we can just use the api to communicate with others...
