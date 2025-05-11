from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import login
import time

# ✅ Chrome WebDriver 실행  
driver = webdriver.Chrome()

try:
  login.login(ws, EC, By, driver)
  TARGET_USER_NAME = "seytest3"

  time.sleep(3)

  search_box = driver.find_element(By.XPATH, "//input[@placeholder='사용자 검색']")
  search_box.send_keys(TARGET_USER_NAME)

  time.sleep(2)

  search_user = driver.find_element(By.XPATH, f"//div[text()='{TARGET_USER_NAME}']")
  search_user.click()

  searched_user = ws(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, f"//strong[text()='{TARGET_USER_NAME}']")))
  searched_username = searched_user[0].text.strip()
  print("검색된 유저: ", searched_username)
  print("검색한 유저: ", TARGET_USER_NAME)

  if not searched_user == TARGET_USER_NAME:
    print("❌ 검색 유저가 일치하지 않습니다!")
    driver.quit()
  
  input("Enter를 누르면 창이 닫힙니다...")
  driver.quit()

except TimeoutException as TIE:
  print("타임아웃: ", str(TIE))

except NoSuchElementException as NSE:
  print("검색 결과 없음: ", str(NSE))