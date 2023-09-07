# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 7/9/2023 3:52 pm

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters, ContextTypes

TOKEN: Final[str] = 'YOUR TOKEN'
BOT_USERNAME: Final[str] = '@YOURBOT'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Nice to meet you. Let\'s chat!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something and I will respond to you.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command.')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good, thanks.'

    if 'I love python' in processed:
        return 'Python is cooooool.'

    return 'I don\'t understand...'

async def handel_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    #Log
    print(f'User ({update.message.chat.id}） in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str =handle_response(text)

    #reply
    print('Bots', response)
    await update.message.reply_text(response)

async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')


def main():
    print('Starting up bot...')
    app = Application.builder().token(TOKEN).build()

    #Command:
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Message:
    app.add_handler(MessageHandler(filters.TEXT, handel_message))

    #Error:
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)



if __name__ == '__main__':
    main()
