from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('YOUR_TOKEN')

import requests
requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://xyz123.ngrok.io/webhook')


app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.json, bot_app.bot)
    bot_app.dispatcher.process_update(update)
    return 'OK', 200

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    app.run(port=5000)