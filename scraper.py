from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import os

driver: Chrome = None


def open_browser():
    global driver
    driver = Chrome()

def go_to_login_page():
    login_url = "https://account.everytime.kr/login"
    driver.get(login_url)

def insert_account_info(id: str, password: str):
    id_form = driver.find_element(By.NAME, "id")
    password_form = driver.find_element(By.NAME, "password")
    id_form.send_keys(id)
    password_form.send_keys(password)

def click_login():
    click_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input")
    click_button.click()

def login_everytime():
    id = "cuteparrots"
    password = os.getenv("EVERYTIME_PASSWORD")

    go_to_login_page()
    insert_account_info(id, password)
    click_login()

def close_browser():
    driver.close()

def main():
    open_browser()
    login_everytime()

    while True:
        pass
    
    close_browser()

if __name__ == "__main__":
    main()