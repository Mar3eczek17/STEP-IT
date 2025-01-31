from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv

async def start(update: Update, context):
    await update.message.reply_text('Hello! I\'m your bot on Telegram!')

async def echo(update: Update, context):
    await update.message.reply_text(f"Powiedziałeś: {update.message.text}")

load_dotenv()
TOKEN = os.getenv('YOUR_TOKEN')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()