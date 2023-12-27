from selenium import webdriver
from dotenv import load_dotenv
import os
from datetime import datetime
from selenium.webdriver.firefox.options import Options

load_dotenv()

email = os.environ.get("email")
password = os.environ.get("password")

def create_driver(headless=False):
    options = Options()

    if headless:
        options.add_argument('-headless')

    driver = webdriver.Firefox(options=options)
    return driver


def login():
    browser.get("https://talents.esi.dz/accounts/login/")
    username = browser.find_element("xpath",'//*[@id="username"]')
    username.send_keys(email)
    password_inp = browser.find_element("xpath",'//*[@id="password"]')
    password_inp.send_keys(password)
    submit = browser.find_element("xpath",'/html/body/div/div[2]/section/div[2]/div/div/form/button')
    submit.click()


def get_last_note_date():
    browser.get("https://talents.esi.dz/scolar/notifications")

    last_note = browser.find_element("xpath",'/html/body/div/div[2]/section/div[2]/div/table/tbody/tr[1]/td[1]/p')

    last_note_date = browser.find_element("xpath",
        '//*[@id="content"]/div/table/tbody/tr[1]/td[2]'
    )

    last_note_date = last_note_date.text[:-5].strip()
    last_note_date = last_note_date[:3] + last_note_date[4:]
    time_format = "%b. %d, %Y, %H:%M"
    t0 = datetime.strptime(last_note_date, time_format)
    if t0.date() == datetime.today().date():
        print("New note!")
        print(last_note.text)
    else:
        print("No new note.")


if __name__ == "__main__":
    browser = create_driver(headless=True)
    login()
    get_last_note_date()
    
