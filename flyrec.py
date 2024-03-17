import pyautogui
import subprocess
import time


def sign_in(link, fly_path):
    """Opens up the ifly app"""
    subprocess.Popen([fly_path])

    time.sleep(20)

    # clicks the join button
    fullscreen_path = "C:\\Users\\alana\\Documents\\Scripts\\dumbasspdpv3\\pypics\\fullscreen.PNG"
    fullscreen = pyautogui.locateCenterOnScreen(fullscreen_path)
    pyautogui.moveTo(fullscreen)
    pyautogui.click()

    time.sleep(2)

    # clicks the join button
    join_path = "C:\\Users\\alana\\Documents\\Scripts\\dumbasspdpv3\\pypics\\join_button.PNG"
    join_btn = pyautogui.locateCenterOnScreen(join_path)
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(2)

    # Types information
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(link)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("123456")
    time.sleep(2)

    # Clicks join meeting
    join_meeting_path = "C:\\Users\\alana\\Documents\\Scripts\\dumbasspdpv3\\pypics\\join_meeting.PNG"
    join_meeting = pyautogui.locateCenterOnScreen(join_meeting_path)
    pyautogui.moveTo(join_meeting)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

def sign_out():
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

