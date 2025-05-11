import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from coupang.main_page import MainPage
from coupang.login_page import LoginPage
from selenium.webdriver.common.by import By
from urllib import parse

# TC001 상품 검색 기능 테스트

# 비 로그인 상태
# @pytest.mark.skip(reason="잠깐 테스트 케이스 발동 안함")
def test_unlogin_search_items(driver: WebDriver):
        try:
            time.sleep(2)
            ITEM_XPATH = "//form//ul/li"

            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            
            time.sleep(2)

            # main_page.search_items('노트북')
            text_to_type = "노"
            text_to_type_two = "트"
            text_to_type_three = "북"

            text_list = [text_to_type, text_to_type_two, text_to_type_three]


            for i in text_list:
                for char in i:
                    main_page.search_text_input(char)
                    time.sleep(3)  # 0.2초(200ms) 정도 대기 (원하는 만큼 조절)
           
            main_page.search_text_enter()
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


# 와우 회원 로그인
@pytest.mark.skip(reason="잠깐 테스트 케이스 발동 안함")
def test_wowlogin_search_items(driver: WebDriver):
        try:
            ITEM_XPATH = "//form//ul/li"

            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url

            login_page.login_success()
            time.sleep(5)

            ws(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "로그아웃")))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            text_to_type = "노"
            text_to_type_two = "트"
            text_to_type_three = "북"

            text_list = [text_to_type, text_to_type_two, text_to_type_three]

            main_page = MainPage(driver)
            for i in text_list:
                for char in i:
                    main_page.search_text_input(char)
                    time.sleep(3)  # 0.2초(200ms) 정도 대기 (원하는 만큼 조절)
           
            main_page.search_text_enter()

            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))

            items = driver.find_elements(By.XPATH, ITEM_XPATH)
            item_name = parse.quote('노트북')
        

            assert len(items) > 0
            assert item_name in driver.current_url

            driver.save_screenshot("와우 회원 로그인-검색-성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot("와우 회원 로그인-검색-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("와우 회원 로그인-검색-실패-타임에러.png")
            assert False