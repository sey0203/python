from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import password
import time

class LoginPage():
    URL = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
    EMAIL_INPUT_ID = "login-email-input"
    PASSWORD_INPUT_ID = "login-password-input"
    LOGIN_EMAIL = password.email
    LOGIN_PASSWORD = password.password

    #객체 > 인스턴스화/ 원하는 설정으로 셋업하는 함수
    def __init__(self, driver: WebDriver):
        self.driver = driver

    #로그인페이지 열기
    def open(self):
        self.driver.get(self.URL)

    def login_success(self):
        login_email_input = self.driver.find_element(By.ID, self.EMAIL_INPUT_ID)
        login_email_input.send_keys(self.LOGIN_EMAIL)

        time.sleep(3)

        login_password_input = self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID)
        login_password_input.send_keys(self.LOGIN_PASSWORD)

        time.sleep(3)

        login_password_input.send_keys(Keys.ENTER)





    # def search_items(self, item_name: str):
    #     search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
    #     search_input_box.send_keys(item_name)
    #     search_input_box.send_keys(Keys.ENTER)

    # def click_by_LINK_TEXT(self, link_text: str):
    #     login_button = self.driver.find_element(By.LINK_TEXT, link_text)
    #     login_button.click()

    # def click_login(self):
    #     login_button = self.driver.find_element(By.LINK_TEXT, "로그인")
    #     login_button.click()