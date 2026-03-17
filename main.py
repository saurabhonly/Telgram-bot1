import os
import telebot
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    bot.reply_to(message, f"👋 Hello {user}!\n🤖 Bot 24/7 Railway par chal raha hai.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commands:\n/start\n/help")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"📩 Tumne likha: {message.text}")

@app.route("/")
def home():
    return "Bot Running"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
    app.run(host="0.0.0.0", port=8080)
