import Constants as keys
from telegram.ext import *
import Responses as R
import csv

############################################################

o = open("bot_responses _for_new_ats.csv")
reader = csv.reader(o)

admit_duty_list = []
mute_duty_list = []
spotlight_duty_list = []
upload_duty_list = []
attendance_duty_list = []
phone_duty_list = []
game_duty_list = []
daily_report_duty_list = []
daily_attendance_duty_list = []

for row in reader:
    admit_duty_list.append(row[0])
    mute_duty_list.append(row[1])
    spotlight_duty_list.append(row[2])
    upload_duty_list.append(row[3])
    attendance_duty_list.append(row[4])
    phone_duty_list.append(row[5])
    game_duty_list.append(row[6])
    daily_report_duty_list.append(row[7])
    daily_attendance_duty_list.append(row[8])

############################################################
print("Hisako is started")

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")

def help_command(update, context):
    update.message.reply_text("You can ask Neki")

def guide_command(update, context):
    update.message.reply_text("https://docs.google.com/document/d/1Aq0JPmzL_krqtLoWfN8K6a_t-f4ecjtkEc6orMGX_A4/edit?usp=sharing")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("guide", guide_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(0)
    updater.idle()


main()

