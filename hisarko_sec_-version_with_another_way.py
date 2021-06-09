import telebot
import time
import Responses as R

def find_at(msg):
    for text in msg:
        if "/" in text:
            return text

print("test bot is started")

bot_token = "1846318619:AAETjtObUuezdDFfMAoEjWI_yP9CG72Ytgo"

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Type something random to get started!")

@bot.message_handler(commands=['guide'])
def send_welcome(message):
    bot.reply_to(message, "https://docs.google.com/document/d/1Aq0JPmzL_krqtLoWfN8K6a_t-f4ecjtkEc6orMGX_A4/edit?usp=sharing")

@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message, "Ask Neki or type /guide")

@bot.message_handler(func=lambda msg: msg.text is not None and "/" in msg.text)
def at_answer(message):
    texts = R.sample_responses(message.text)
    bot.reply_to(message, texts)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)