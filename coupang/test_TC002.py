import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from coupang.main_page import MainPage
from coupang.login_page import LoginPage
from coupang.TC002 import CartPage
from selenium.webdriver.common.by import By
from urllib import parse



# TC002 장바구니 담기 기능 테스트


# 비 로그인 상태
# @pytest.mark.skip(reason="잠깐 테스트 케이스 발동 안함")
def test_unlogin_product_page(driver: WebDriver):
        try:
            ITEM_XPATH = "//a[contains(@class, 'search-product-link')"

            time.sleep(5)
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(5)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))

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

            items = driver.find_elements(By.XPATH, ITEM_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url

            time.sleep(3)
            cart_page = CartPage(driver)
            cart_page.select_first_item()

            time.sleep(3)

            assert "products" in driver.current_url
            driver.save_screenshot("비회원-검색-상세페이지-성공.png")
      
        except NoSuchElementException as e:
            driver.save_screenshot("비회원-상세페이지-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("비회원-상세페이지-실패-타임에러.png")
            assert False


@pytest.mark.skip(reason="잠깐 테스트 케이스 발동 안함")
def test_unlogin_add_cart(driver: WebDriver):
        try:
            ITEM_XPATH = "//a[contains(@class, 'search-product-link')"
            Cart_Count_ID = "headerCartCount"

            time.sleep(5)
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(10)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))

            main_page.search_items('노트북')
            time.sleep(5)

            items = driver.find_elements(By.XPATH, ITEM_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url

            time.sleep(3)
            
            cart_page = CartPage(driver)
            cart_page.select_first_item()

            time.sleep(3)

            assert "products" in driver.current_url

            cart_page.add_to_cart()
            time.sleep(3)

            cart_count = driver.find_element(By.ID, Cart_Count_ID)
            cart_count_num = cart_count.text
            assert 1 in cart_count_num
            driver.save_screenshot("비회원-장바구니 담기-성공.png")
      
        except NoSuchElementException as e:
            driver.save_screenshot("비회원-장바구니 담기-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("비회원-장바구니 담기-실패-타임에러.png")
            assert False