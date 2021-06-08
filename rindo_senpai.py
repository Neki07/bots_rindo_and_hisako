import csv
import discord
##############################################



##############################################

def adding_csv_into_list(row_number,csv_file,new_list):
    for row in csv_file:
        new_list.append(row[row_number])

##############################################

o = open("bot_responses _for_new_ats.csv")
reader = csv.reader(o)

##############################################

admit_duty_list = []
mute_duty_list = []
spotlight_duty_list = []
upload_duty_list = []
attendance_duty_list = []
phone_duty_list = []
game_duty_list = []
daily_report_duty_list = []
daily_attendance_duty_list = []

##############################################

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

##############################################

client = discord.Client()

@client.event

async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

######## for introduction
    if message.content.startswith('$hello') or message.content.startswith("$Hello"):
        await message.channel.send("Hey How's it going?.If you want to know how to ask questions, please ask how to ask questions for duties?")
    if message.content.startswith('$who are you') or message.content.startswith("$Who are you"):
        await message.channel.send("I am Rindo.")

########  for admit duty(AD)

    if message.content.startswith('$whatAD') or message.content.startswith("$What is admit duty?"):
        await message.channel.send(admit_duty_list[0])
    if message.content.startswith("$howAD?") or message.content.startswith("$How to do admit duty?"):
        await message.channel.send(admit_duty_list[1])
    if message.content.startswith("$ieltsAD?") or message.content.startswith("$How to do admit duty for ielts"):
        await message.channel.send(admit_duty_list[2])
    if message.content.startswith("$resourcesAD?") or message.content.startswith("$Can I get the resources for admit duty"):
        await message.channel.send(admit_duty_list[3])
    if message.content.startswith("$noteAD?") or message.content.startswith("$What are the notes for admit duty?"):
        await message.channel.send(admit_duty_list[4])

########  for mute duty(MD)

    if message.content.startswith('$whatMD') or message.content.startswith("$What is mute duty?"):
        await message.channel.send(mute_duty_list[0])
    if message.content.startswith("$howMD?") or message.content.startswith("$How to do mute duty?"):
        await message.channel.send(mute_duty_list[1])
    if message.content.startswith("$ieltsMD?") or message.content.startswith("$How to do mute duty for ielts?"):
        await message.channel.send(mute_duty_list[2])
    if message.content.startswith("$resourcesMD?") or message.content.startswith("$Can I get the resources for mute duty?"):
        await message.channel.send(mute_duty_list[3])
    if message.content.startswith("$noteMD?") or message.content.startswith("$What are the notes for mute duty?"):
        await message.channel.send(mute_duty_list[4])

########  for spotlight duty(SD)

    if message.content.startswith('$whatSD') or message.content.startswith("$What is spotlight duty?"):
        await message.channel.send(spotlight_duty_list[0])
    if message.content.startswith("$howSD?") or message.content.startswith("$How to do spotlight duty?"):
        await message.channel.send(spotlight_duty_list[1])
    if message.content.startswith("$ieltsSD?") or message.content.startswith("$How to do spotlight duty for ielts"):
        await message.channel.send(spotlight_duty_list[2])
    if message.content.startswith("$resourcesSD?") or message.content.startswith("$Can I get the resources for spotlight duty"):
        await message.channel.send(spotlight_duty_list[3])
    if message.content.startswith("$noteSD?") or message.content.startswith("$What are the notes for spotlight duty?"):
        await message.channel.send(spotlight_duty_list[4])


########  for upload duty(UD)

    if message.content.startswith('$whatUD') or message.content.startswith("$What is upload duty?"):
        await message.channel.send(upload_duty_list[0])
    if message.content.startswith("$howUD?") or message.content.startswith("$How to do upload duty?"):
        await message.channel.send(upload_duty_list[1])
    if message.content.startswith("$ieltsUD?") or message.content.startswith("$How to do upload duty for ielts"):
        await message.channel.send(upload_duty_list[2])
    if message.content.startswith("$resourcesUD?") or message.content.startswith("$Can I get the resources for upload duty"):
        await message.channel.send(upload_duty_list[3])
    if message.content.startswith("$noteUD?") or message.content.startswith("$What are the notes for upload duty?"):
        await message.channel.send(upload_duty_list[4])

########  for attendance duty(AeD)

    if message.content.startswith('$whatAeD') or message.content.startswith("$What is attendance duty?"):
        await message.channel.send(attendance_duty_list[0])
    if message.content.startswith("$howAeD?") or message.content.startswith("$How to do attendance duty?"):
        await message.channel.send(attendance_duty_list[1])
    if message.content.startswith("$ieltsAeD?") or message.content.startswith("$How to do attendance duty for ielts"):
        await message.channel.send(attendance_duty_list[2])
    if message.content.startswith("$resourcesAeD?") or message.content.startswith("$Can I get the resources for attendance duty"):
        await message.channel.send(attendance_duty_list[3])
    if message.content.startswith("$noteAeD?") or message.content.startswith("$What are the notes for attendance duty?"):
        await message.channel.send(attendance_duty_list[4])

########  for phone duty(PD)

    if message.content.startswith('$whatPD') or message.content.startswith("$What is phone duty?"):
        await message.channel.send(phone_duty_list[0])
    if message.content.startswith("$howPD?") or message.content.startswith("$How to do phone duty?"):
        await message.channel.send(phone_duty_list[1])
    if message.content.startswith("$ieltsPD?") or message.content.startswith("$How to do phone duty for ielts"):
        await message.channel.send(phone_duty_list[2])
    if message.content.startswith("$resourcesPD?") or message.content.startswith("$Can I get the resources for phone duty"):
        await message.channel.send(phone_duty_list[3])
    if message.content.startswith("$notePD?") or message.content.startswith("$What are the notes for phone duty?"):
        await message.channel.send(phone_duty_list[4])

########  for game duty(GD)

    if message.content.startswith('$whatGD') or message.content.startswith("$What is game duty?"):
        await message.channel.send(game_duty_list[0])
    if message.content.startswith("$howGD?") or message.content.startswith("$How to do game duty?"):
        await message.channel.send(game_duty_list[1])
    if message.content.startswith("$ieltsGD?") or message.content.startswith("$How to do game duty for ielts"):
        await message.channel.send(game_duty_list[2])
    if message.content.startswith("$resourcesGD?") or message.content.startswith("$Can I get the resources for game duty"):
        await message.channel.send(game_duty_list[3])
    if message.content.startswith("$noteGD?") or message.content.startswith("$What are the notes for game duty?"):
        await message.channel.send(game_duty_list[4])

########  for daily report duty(DrD)

    if message.content.startswith('$whatDrD') or message.content.startswith("$What is daily report duty?"):
        await message.channel.send(daily_report_duty_list[0])
    if message.content.startswith("$howDrD?") or message.content.startswith("$How to do daily report duty?"):
        await message.channel.send(daily_report_duty_list[1])
    if message.content.startswith("$ieltsDrD?") or message.content.startswith("$How to do daily report duty for ielts"):
        await message.channel.send(daily_report_duty_list[2])
    if message.content.startswith("$resourcesDrD?") or message.content.startswith("$Can I get the resources for daily_report duty"):
        await message.channel.send(daily_report_duty_list[3])
    if message.content.startswith("$noteDrD?") or message.content.startswith("$What are the notes for daily report duty?"):
        await message.channel.send(daily_report_duty_list[4])

########  for daily attendance duty(DaeD)

    if message.content.startswith('$whatDaeD') or message.content.startswith("$What is daily attendance duty?"):
        await message.channel.send(daily_attendance_duty_list[0])
    if message.content.startswith("$howDaeD?") or message.content.startswith("$How to do daily attendance duty?"):
        await message.channel.send(daily_attendance_duty_list[1])
    if message.content.startswith("$ieltsDaeD?") or message.content.startswith("$How to do daily attendance duty for ielts"):
        await message.channel.send(daily_attendance_duty_list[2])
    if message.content.startswith("$resourcesDaeD?") or message.content.startswith("$Can I get the resources for daily attendance duty"):
        await message.channel.send(daily_attendance_duty_list[3])
    if message.content.startswith("$noteDaeD?") or message.content.startswith("$What are the notes for daily attendance duty?"):
        await message.channel.send(daily_attendance_duty_list[4])

#########################################

client.run("ODQyNzgxMDU4NjA4NzkxNTYy.YJ6TBg.xF4FecgdhYv1dNI1KudGGdORAAo")
