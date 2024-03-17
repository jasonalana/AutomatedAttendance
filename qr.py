import cv2
import time
import pyautogui
import data as dt
import notification as nt
from selenium.webdriver.common.by import By


def findQR(end, driver, link, img_path):
    pts = None

    while True:
        # Check if class ended yet
        if dt.now() > end:
            nt.tmessage("No QR today.")
            time.sleep(1)
            return

        # Notifies searching for QR
        nt.qrCode(end)
        time.sleep(5)

        # Takes SS based on site
        if link.find('bigbluebuttonbn') != -1:
            try:
                driver.find_element(By.XPATH, "//span[normalize-space()='View shared screen']")
            except:
                pass
            driver.save_screenshot(img_path)
        else:
            pyautogui.screenshot(img_path)

        # Reads QR from SS
        img = cv2.imread(img_path)
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img)

        if val.find('attendance') != -1:
            print("QR code found!")
            return val


