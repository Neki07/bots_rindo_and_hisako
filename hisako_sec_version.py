import telebot
import Constants as k
import time

print("test bot is started")

bot_token = "1846318619:AAETjtObUuezdDFfMAoEjWI_yP9CG72Ytgo"

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Type something random to get started!")


@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message, "Ask Neki or type /guide")



while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)