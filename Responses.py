from datetime import datetime
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

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("/hello", "/hi", "/sup"):
        return "Hey How's it going?.If you want to know how to ask questions, please ask how to ask questions for duties?"
    if user_message in ("/who are you", "/who are you?"):
        return "I am Hisako."
    if user_message in ("/time",  "/time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)
    if user_message in ("/how to ask commands?" , "/guide"):
        return str(g)


########  for admit duty(ad)
    if user_message in ('/what:ad?', "/what is admit duty?"):
        return (admit_duty_list[0])
    if user_message in ("/how:ad?", '/how to do admit duty?'):
        return (admit_duty_list[1])
    if user_message in ("/ielts:ad?", "/how to do admit duty for ielts?"):
        return (admit_duty_list[2])
    if user_message in ("/resources:ad?", "/can i get the resources for admit duty?"):
        return (admit_duty_list[3])
    if user_message in ("/note:ad?", "/what are the notes for admit duty?"):
        return (admit_duty_list[4])

########  for mute duty(md)
    if user_message in ('/what:md?', "/what is mute duty?"):
        return (mute_duty_list[0])
    if user_message in ("/how:md?", '/how to do mute duty?'):
        return (mute_duty_list[1])
    if user_message in ("/ielts:md?", "/how to do mute duty for ielts?"):
        return (mute_duty_list[2])
    if user_message in ("/resources:md?", "/can i get the resources for mute duty?"):
        return (mute_duty_list[3])
    if user_message in ("/note:md?", "/what are the notes for mute duty?"):
        return (mute_duty_list[4])

########  for spotlight duty(sd)
    if user_message in ('/what:sd?', "what is spotlight duty?"):
        return (spotlight_duty_list[0])
    if user_message in ("/how:sd?", 'how to do spotlight duty?'):
        return (spotlight_duty_list[1])
    if user_message in ("/ielts:sd?", "how to do spotlight duty for ielts?"):
        return (spotlight_duty_list[2])
    if user_message in ("/resources:sd?", "can i get the resources for spotlight duty?"):
        return (spotlight_duty_list[3])
    if user_message in ("/note:sd?", "what are the notes for spotlight duty?"):
        return (spotlight_duty_list[4])

########  for upload duty(ud)
    if user_message in ('/what:ud?', "/what is upload duty?"):
        return (upload_duty_list[0])
    if user_message in ("/how:ud?", '/how to do upload duty?'):
        return (upload_duty_list[1])
    if user_message in ("/ielts:ud?", "/how to do upload duty for ielts?"):
        return (upload_duty_list[2])
    if user_message in ("/resources:ud?", "/can i get the resources for upload duty?"):
        return (upload_duty_list[3])
    if user_message in ("/note:ud?", "/what are the notes for upload duty?"):
        return (upload_duty_list[4])

########  for attendance duty(aed)
    if user_message in ('/what:aed?', "/what is attendance duty?"):
        return (attendance_duty_list[0])
    if user_message in ("/how:aed?", '/how to do attendance duty?'):
        return (attendance_duty_list[1])
    if user_message in ("/ielts:aed?", "/how to do attendance duty for ielts?"):
        return (attendance_duty_list[2])
    if user_message in ("/resources:aed?", "/can i get the resources for attendance duty?"):
        return (attendance_duty_list[3])
    if user_message in ("/note:aed?", "/what are the notes for attendance duty?"):
        return (attendance_duty_list[4])

########  for phone duty(pd)
    if user_message in ('/what:pd?', "/what is phone duty?"):
        return (phone_duty_list[0])
    if user_message in ("/how:pd?", '/how to do phone duty?'):
        return (phone_duty_list[1])
    if user_message in ("/ielts:pd?", "/how to do phone duty for ielts?"):
        return (phone_duty_list[2])
    if user_message in ("/resources:pd?", "/can i get the resources for phone duty?"):
        return (phone_duty_list[3])
    if user_message in ("/note:pd?", "/what are the notes for phone duty?"):
        return (phone_duty_list[4])

########  for game duty(gd)
    if user_message in ('/what:gd?', "/what is game duty?"):
        return (game_duty_list[0])
    if user_message in ("/how:gd?", '/how to do game duty?'):
        return (game_duty_list[1])
    if user_message in ("/ielts:gd?", "/how to do game duty for ielts?"):
        return (game_duty_list[2])
    if user_message in ("/resources:gd?", "/can i get the resources for game duty?"):
        return (game_duty_list[3])
    if user_message in ("/note:gd?", "/what are the notes for game duty?"):
        return (game_duty_list[4])

########  for daily report duty(drd)
    if user_message in ('/what:drd?', "/what is daily report duty?"):
        return (daily_report_duty_list[0])
    if user_message in ("/how:drd?", '/how to do daily report duty?'):
        return (daily_report_duty_list[1])
    if user_message in ("/ielts:drd?", "/how to do daily report duty for ielts?"):
        return (daily_report_duty_list[2])
    if user_message in ("/resources:drd?", "/can i get the resources for daily report duty?"):
        return (daily_report_duty_list[3])
    if user_message in ("note:drd?", "what are the notes for daily report duty?"):
        return (daily_report_duty_list[4])

########  for daily attendance duty(daed)
    if user_message in ('/what:daed?', "/what is daily attendance duty?"):
        return (daily_attendance_duty_list[0])
    if user_message in ("/how:daed?", '/how to do daily attendance duty?'):
        return (daily_attendance_duty_list[1])
    if user_message in ("/ielts:daed?", "/how to do daily attendance duty for ielts?"):
        return (daily_attendance_duty_list[2])
    if user_message in ("/resources:daed?", "/can i get the resources for daily attendance duty?"):
        return (daily_attendance_duty_list[3])
    if user_message in ("/note:daed?", "/what are the notes for daily attendance duty?"):
        return (daily_attendance_duty_list[4])

    return "Hisako don't understand. Tell Neki."