from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://naver.com/"

driver.get(url)

time.sleep(3)

"""
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
"""

# driver.find_element(By.CLASS_NAME, "search_input").send_keys("빅뱅")
# time.sleep(1)

# driver.find_element(By.ID, "query").send_keys("권지용")
# time.sleep(1)

# driver.find_element(By.NAME, "query").send_keys("동영배")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "[title='검색어를 입력해 주세요.']").send_keys("강대성")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "[placeholder='검색어를 입력해 주세요.']").send_keys("빅뱅짱")
# time.sleep(1)


driver.find_element(By.XPATH, '//*[@id="query"]').send_keys("컴백축하")
time.sleep(1)