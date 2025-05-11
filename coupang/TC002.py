from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


# TC001 장바구니 담기 기능 테스트


class CartPage:
    ITEM_XPATH = "//a[contains(@class, 'search-product-link')"
    CART_BUTTON_XPATH = "//button[contains(text()='장바구니 담기')]"
    MOVE_CART_BUTTON_CLASSNAME = "cart more"

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def select_first_item(self):
        wait = ws(self.driver, 10)
        first_item = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEM_XPATH)))
        first_item[0].click()


    def add_to_cart(self):
        wait = ws(self.driver, 10)
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON_XPATH)))
        cart_button.click()


    def move_to_cart(self):
        wait = ws(self.driver, 10)
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.MOVE_CART_BUTTON_CLASSNAME)))
        cart_button.click()