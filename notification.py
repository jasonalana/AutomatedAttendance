import os
import time
import telegram
import data as dt
import pandas as pd

"""
Collection of notification functions
    can be used to track progress.
"""


def tmessage(message):
    """
    Sends a message to Telegram channel

    Parameters:
        message (string): wanted message
    """
    token = '5202557812:AAHCUQSF2CKv7GPLx-4M3wX9I-TcKnkuf7Q'
    chat_id = '-1001274412957'
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)


def tpic(path):
    """
    Sends an image to Telegram channel

    Parameters:
        path (string): path to image file
    """
    token = '5202557812:AAHCUQSF2CKv7GPLx-4M3wX9I-TcKnkuf7Q'
    chat_id = '-1001274412957'
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))


def loading():
    """Creates a loading screen that continuously updates."""
    clearConsole()
    print(consoleUpdate())
    time.sleep(10)


def clearConsole():
    """Clears console"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def Start():
    """Console on startup, returns string containing schedule"""
    df = pd.read_csv('timings.csv')
    schedule = df.loc[df.Day == str(pd.Timestamp.day_name(dt.now()))]
    schedule = schedule.drop(['Link', 'Day'], axis=1)

    start = ("Hello, today is: " + str(pd.Timestamp.day_name(dt.now()))
             + ", " + str(dt.now().strftime("%D/%Y")) + "\n"
             + "\nToday's schedule:\n"
             + schedule.to_string(index=False) + "\n")

    if schedule.dropna().empty:
        start = "No class today, have fun!"

    print(start)
    tmessage(start)


def consoleUpdate():
    """Console update, returns updated information."""
    try:
        update = ("\nCurrent time: " + dt.now().strftime("%X")
                  + "\nNext class: " + dt.nextClass().Class
                  + " | " + str(dt.nextClass().Start.strftime("%X")) + " - "
                  + str(dt.nextClass().End.strftime("%X"))
                  + "\nClass starts in: " + dt.deltatimeStart()
                  )
    except:
        # Exception occurs when there is no "next class".
        update = "No more class today, YAY!"
    return update


def qrCode(end):
    """Notification that shows when program is looking for QR."""
    clearConsole()
    print("Currently looking for QR code...\n")
    try:
        print("Current time: " + dt.now().strftime("%X")
          + "\nNext class: " + dt.nextClass().Class
          + " | " + str(dt.nextClass().Start.strftime("%X")) + " - "
          + str(dt.nextClass().End.strftime("%X"))
          + "\nClass ends in: " + dt.deltatimeEnd(end)
          )
    except:
        print("Class ends in: " + dt.deltatimeEnd(end))


def classStarting(subject):
    print(subject + " starting!")
    tmessage(subject + " started.")