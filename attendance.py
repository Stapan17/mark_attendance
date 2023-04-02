
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

USERNAME = "username"
PASSWORD = "password"

def get_clock_in_out_button():
    clock = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/button')
    return clock

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.maximize_window()

now = datetime.now()

current_hour = now.hour
current_minutes = now.minute

driver.get("https://new.myhrm.in/")


# entering username
username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input')
username.send_keys(USERNAME)

# entering password
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input[1]')
password.send_keys(PASSWORD)

# login button click
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/form/div[4]/button').click()

time.sleep(2)

try:

    # clock in/out
    current_clock = get_clock_in_out_button()
    current_text = current_clock.text

    # by mistake if the script runs more than once in the morning
    if current_text == "Clock Out" and current_hour < 18:
        print("You are already Clocled In!")
        exit()

    # by mistake if the script runs more than once at the EOD
    if current_text == "Clock In" and current_hour > 18:
        print("You are already Clocled Out!")
        exit()

    # if it's valid time then clock in/out
    current_clock.click()

    time.sleep(3)

    updated_clock = get_clock_in_out_button()
    updated_text = updated_clock.text

    if updated_text != current_text:
        message = "Attendance Marked!"

    else:
        message = "There is some issue, please mark/check attendance manually"

    print(message)

except:
    print("Username or Password is incorrect!")

driver.close()
