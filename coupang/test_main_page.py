import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from coupang.main_page import MainPage
from selenium.webdriver.common.by import By
from urllib import parse #url 라이브러리를 통해 한글이 깨지지않게

@pytest.mark.usefixtures("driver")
class TestMainPage:
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
        
        except NoSuchElementException as e:
            assert False

    
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
         

            main_page.click_by_LINK_TEXT('로그인')

            assert "login" in driver.current_url
            driver.save_screenshot("메인페이지-로그인-성공.png")

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)
            main_page.click_by_LINK_TEXT('회원가입')
            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot("메인페이지-회원가입-성공.png")

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)
            main_page.click_by_LINK_TEXT('장바구니')
            assert "cartView" in driver.current_url
            driver.save_screenshot("메인페이지-장바구니-성공.png")

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)
            main_page.click_by_LINK_TEXT('마이쿠팡')
            assert "login" in driver.current_url
            driver.save_screenshot("메인페이지-마이쿠팡-성공.png")

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url


        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-링크테스트-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("메인페이지-링크테스트-실패-타임에러.png")
            assert False


    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
        try:
            ITEM_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            main_page.search_items('노트북')

            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))

            items = driver.find_elements(By.XPATH, ITEM_XPATH)
            item_name = parse.quote('노트북')
        

            assert len(items) > 0
            assert item_name in driver.current_url

            driver.save_screenshot("메인페이지-검색-성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-검색-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.png")
            assert False
