import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:3000/login")


login_button = ws.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), '로그인')]")))

driver.find_element(By.NAME, "email").send_keys("test1@naver.com")
driver.find_element(By.NAME, "password").send_keys("pw1")

login_button.click()

time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='사용자 검색']").send_keys("seytest2")


ws.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='사용자 검색']/following-sibling::div")))

# avatars = driver.find_elements(By.CLASS_NAME, "sc-ghWlax thuNm")

# print(avatars)

# print(f"검색된 사용자 수: {len(avatars)}명")


# searched_user = driver.find_element(By.XPATH, "//div[text()='seytest2']")

# assert searched_user.is_displayed(), "검색된 사용자가 보이지 않습니다!"
# print("'seytest2'가 검색 결과에 정상적으로 표시되었습니다!")

# assert searched_user.text == "seytest2", "'seytest2' 확인 안됨."
# print("'seytest2' 검색 결과 확인 완료!")

# searched_user.click()

# assert "browse/67c80e7bc3ab7cc24935f3bb" in driver.current_url, "페이지 이동 실패"
# print("'seytest2' 페이지로 이동 성공")

# time.sleep(1)

# user_name_display = driver.find_element(By.XPATH, "//div[contains(text(), '님의 일정')]")

# assert user_name_display.is_displayed(), "사용자 상세페이지에서 이름이 표시되지 않았습니다!"
# print("상세 페이지에서 사용자 이름이 정상적으로 표시됨: ", user_name_display.text)


