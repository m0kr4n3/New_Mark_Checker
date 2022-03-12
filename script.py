from selenium import webdriver
from dotenv import load_dotenv
import os
from datetime import datetime
from selenium.webdriver.chrome.service import Service

load_dotenv()

email = os.environ.get("email")
password = os.environ.get("password")


def get_last_note_date(browser):
    browser.get("https://talents.esi.dz/scolar/notifications")
    last_note = browser.find_element_by_xpath(
        '//*[@id="content"]/div/table/tbody/tr[1]/td[2]'
    )

    its_date = last_note.text[:-5]
    time_format = "%B %d, %Y, %H:%M"
    t0 = datetime.strptime(its_date, time_format)
    return t0


def if_today(t0):
    return t0.date() == datetime.today().date()


def main():
    s = Service("./chromedriver")
    browser = webdriver.Chrome(service=s)

    browser.get("https://talents.esi.dz/accounts/login/")
    username = browser.find_element_by_xpath('//*[@id="id_username"]')
    username.send_keys(email)
    password_inp = browser.find_element_by_xpath('//*[@id="id_password"]')
    password_inp.send_keys(password)
    submit = browser.find_element_by_xpath('//*[@type="submit"]')
    submit.click()

    t0 = get_last_note_date(browser)
    print(t0)
    if if_today(t0):
        print("There's a new note, go check it!")


if __name__ == "__main__":
    main()
