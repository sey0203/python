import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from coupang.login_page import LoginPage
from selenium.webdriver.common.by import By
from urllib import parse


@pytest.mark.usefixtures("driver")
class TestLoginPage:
    def test_open_login_page(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
        
        except NoSuchElementException as e:
            assert False, f"로그인 페이지 열기 실패: {e}"

    def test_login_success(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url

            login_page.login_success()
            time.sleep(5)

            ws(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "로그아웃")))

            logout_button = driver.find_element(By.LINK_TEXT, "로그아웃")
            assert logout_button.is_displayed(), "로그아웃 버튼이 보이지 않음, 로그인 실패"
            driver.save_screenshot("로그인페이지-로그인-성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot("로그인페이지-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("로그인페이지-실패-타임에러.png")
            assert False
        




# @pytest.mark.usefixtures("driver")
# def test_login_page_open(self, driver: WebDriver):
#         try:
#             main_page = MainPage(driver)
#             main_page.open()

#             time.sleep(2)

#             wait = ws(driver, 10)
#             wait.until(EC.url_contains("coupang.com"))
#             assert "coupang.com" in driver.current_url
         

#             main_page.click_by_LINK_TEXT('로그인')

#             assert "login" in driver.current_url

#         except NoSuchElementException as e:
#             print(f"메인페이지-링크테스트-실패 : {e}")
#             assert False

#         except TimeoutException as e:
#             print(f"메인페이지-링크테스트-실패 : {e}")
#             assert False




# class TestLoginPage():
#   def test_login_url():
#     LoginPage().open()
#     drivert.cureturl.
#     assert

