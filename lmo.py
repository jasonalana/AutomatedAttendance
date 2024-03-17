import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def loading(text):
    for i in range(4):
        print(text + "." * i, end="", flush=True)
        time.sleep(1)
        print(end="\r")
        clear_console()


def drInit(hl, chromePt):
    """
    Initializes driver, takes in headless argument
    and chromedriver path
    """
    options = webdriver.ChromeOptions()
    if hl:
        options.add_argument('--headless')
        options.add_argument("--window-size=1920x1080")
    options.add_argument('--user-data-dir=C:/Users/alana/AppData/Local/Google/Chrome/User Data/TEST')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chromePt, chrome_options=options)
    return driver


def login(driver, password):
    lmo = "https://core.xjtlu.edu.cn/auth/saml2/login.php?wants=https%3A%2F%2Fcore.xjtlu.edu.cn%2Fmy%2F&idp=bc393aa26e71200f0791c509f6592f01&passive=off"

    # Logs into lmo
    logged = False
    while not logged:
        try:
            driver.get(lmo)
            logged = True
        except:
            pass
        time.sleep(5)

    driver.find_element(By.ID, "password_show").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="btn_login"]/div/input').click()
    time.sleep(3)


def init(bbb_link, driver, password):
    # Logs into LMO
    login(driver, password)
    # Opens BBB
    driver.get(bbb_link)

    # Clicks join class
    while len(driver.window_handles) == 1:
        try:
            loading("Waiting for class to open")
            driver.find_element(By.ID, "join_button_input").click()
        except Exception:
            driver.get(bbb_link)
        finally:
            time.sleep(2)

    # Switches tabs
    driver.switch_to.window(driver.window_handles[1])
    while True:
        try:
            loading("Selecting listening mode")
            driver.find_element(By.XPATH, "//i[@class='icon--2q1XXw icon-bbb-listen']").click()
        except:
            continue
        else:
            break
