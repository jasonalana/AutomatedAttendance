import lmo
import time
import flyrec
import pyautogui
import data as dt
import notification as nt
from selenium.webdriver.common.by import By


def startClass(link, chromePt, fly_path, password, img_path):
    """
    Starts class based on its platform
    """

    if link.find('bigbluebuttonbn') != -1:
        # Do not headless
        driver = lmo.drInit(False, chromePt)
    else:
        # Start headless
        driver = lmo.drInit(True, chromePt)

    # Starts Zhumu
    if link.find('zhumu') != -1:
        driver.get(link)
    # Starts VooV
    elif link.find('tencent') != -1:
        driver.get(link)
        time.sleep(5)
        driver.find_element(By.ID, 'mpJoinBtnCtrl').click()
    # Starts BBB
    elif link.find('bigbluebuttonbn') != -1:
        lmo.init(link, driver, password)
        time.sleep(30)
        driver.save_screenshot(img_path)
        nt.tpic(img_path)
    # Starts flyrec
    else:
        flyrec.sign_in(link, fly_path)
    return driver


def logAttendance(qr_link, driver, password, img_path, end):
    # Login
    try:
        lmo.login(driver, password)
    except:
        pass

    # Opens attendance webpage
    driver.get(qr_link)
    nt.tpic(img_path)
    driver.save_screenshot(img_path)
    nt.tpic(img_path)

    # Waits until class ends
    while dt.now() < end:
        nt.clearConsole()
        print("QRCode found, class ends in " + dt.deltatimeEnd(end) + " .")
        time.sleep(30)


def quitAll(driver, link):
    # Checks if flyrec is open
    if not link.isalpha():
        pyautogui.moveTo(500, 500)
        time.sleep(1)
        pyautogui.click()

        with pyautogui.hold('alt'):
            pyautogui.press('q')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        with pyautogui.hold('alt'):
            pyautogui.press('f4')

    # Closes driver
    driver.quit()













