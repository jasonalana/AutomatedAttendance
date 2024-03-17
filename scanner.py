import cv2
import time
import data
import pyautogui
import pandas as pd
import notification as nt
from selenium.webdriver.common.by import By


def scan(driver, row, switch, imgPath):
    webSort(switch, img_path, driver)
    pts = None

    while True:
        # Check if class ended yet
        if dt.csvStop(row):
            nt.tmessage("No QR today.")
            time.sleep(1)
            return

        nt.qrCode(row)
        time.sleep(5)

        # Takes SS based on site
        webSort(switch, imgPath, driver)

        # Reads QR from SS
        img = cv2.imread(imgPath)
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img)

        # If qr is found
        if val.find('learningmall') != -1:
            # Opens attendance webpage
            driver.get(val)

            # Sends telegram message
            nt.tmessage("Attendance taken!")
            nt.tpic(imgPath)
            driver.save_screenshot(imgPath)
            nt.tpic(imgPath)

            # Waits until class ends
            cr.csvWait(row)
            return val


def webSort(switch, img_path, driver):
    if switch:
        # PrtSC
        pyautogui.screenshot(img_path)
    else:
        # SS from webdriver
        # Qr scan process
        try:
            driver.find_element(By.XPATH, "//span[normalize-space()='View shared screen']")
        except:
            pass

        driver.save_screenshot(img_path)


def wait(row):
    now = data.now()

    while now < row.iloc[0, 3]:
        nt.clearConsole()
        now = pd.Timestamp.now()
        print("QRCode found, class ends in " + deltatimeEnd(row) + " .")
        time.sleep(30)