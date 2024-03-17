import qr
import data as dt
import tasks as task
import notification as nt

"""
This program takes in a schedule found in a CSV file, uses pandas to sort data, 
logs attendance from a QR code using OpenCV, and notifies user using telegram.
Author: Jason Alana
"""

username = "jason.alana21"
password = "Kentut20"
chromePt = "C:\\chromedriver.exe"
img_path = "C:\\Users\\alana\\Documents\\Scripts\\attendance\\screenshots\\screenshot.png"
fly_path = "C:\\Program Files (x86)\\iflyrecClient\\iflyrecClient.exe"


# Infinite while loop detects current time and
# crosschecks with 'timings.csv'
try:
    while True:
        # Notifies start of program
        nt.Start()

        # Defines class details
        row = dt.findRow()                                              # Waits until class starts
        if row.empty:
            break
        subject = row.iloc[0, 0]
        day = row.iloc[0, 1]
        start = row.iloc[0, 2]
        end = row.iloc[0, 3]
        link = row.iloc[0, 4]

        # Notifies that class is starting
        nt.classStarting(subject)

        # Defines driver and joins class
        driver = task.startClass(link, chromePt, fly_path,              # Joins class based on platform
                                 password, img_path)

        # Finds and logs attendance
        qrLink = qr.findQR(end, driver, link, img_path)                 # Looks for QR until class ends
        task.logAttendance(qrLink, driver, password, img_path, end)     # Logs attendance on LMO
        task.quitAll(driver, link)                                      # Quits everything

except Exception as error:
    nt.tmessage(str(error))

finally:
    nt.tmessage("No more classes, program stopped.")
    print("No more classes.")
