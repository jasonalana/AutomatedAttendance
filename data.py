import os
import time
import pandas as pd
import notification as nt


"""
Collection of data manipulation modules.
"""


def csvConvert():
    """Converts dataframe type to
    datetime type."""
    df = pd.read_csv('timings.csv')
    df["Start"] = pd.to_datetime(df["Start"])
    df["End"] = pd.to_datetime(df["End"])
    return df


def findRow():
    """Loops through dataframe until a row
    containing the current time is found.

    Returns:
        row (index): row location of matched time
    """
    row = []
    df = csvConvert()

    # Loops through dataframe until
    # current time matches a value
    while len(row) == 0:
        # Reading current time
        ts_now = pd.Timestamp.now()
        ts_day = str(pd.Timestamp.day_name(ts_now))
        ts_start = ts_now + pd.Timedelta(minutes=3)

        # Finding row with the same day, and the current time
        # between the start and end of class.
        row = df.loc[(df.Day == ts_day) & (ts_start >= df.Start) & (ts_now < df.End)]

        if row.empty:
            return row

        # Loading screen
        nt.loading()
    return row


def now():
    """Returns current time as a
    timestamp."""
    currentTime = pd.Timestamp.now()
    return currentTime


def deltatimeStart():
    """Subtract next class and current time, returns time to next class as string."""
    next = nextClass()

    start = next.Start - now()
    start = round(start.seconds / 60)
    start = timeconv(start)

    return start

# Returns time class ends.
def deltatimeEnd(end):
    """Subtract end of class and current time, returns time to end of class as string."""
    timetoend = timeconv(round((end - now()).seconds / 60))
    return timetoend


def timeconv(timed):
    if timed >= 60:
        hour = str(int(timed / 60))
        minutes = str(timed % 60)
        if int(hour) > 1:
            timed = str(hour + " hrs " + minutes + " mins")
        else:
            timed = str(hour + " hr " + minutes + " mins")
    else:
        timed = str(str(timed) + " mins")
    return timed


def nextClass():
    """ Returns the next class in schedule."""
    df = csvConvert()
    today = str(pd.Timestamp.day_name(now()))

    # Outputs a data frame of all classes after current time
    next_class = df.loc[(df.Start > now()) & (df.Day == today)]

    # Sorts from earliest to latest class
    next_class = next_class.sort_values(by='Start', ascending=True)
    try:
        next_class = next_class.iloc[0]
    except:
        pass
    return next_class
