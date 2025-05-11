import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:3000/login")


time.sleep(1)

driver.find_element(By.NAME, "email").send_keys("test1@naver.com")
driver.find_element(By.NAME, "password").send_keys("pw1")
driver.find_element(By.XPATH, "//button[text()='로그인']").click()

time.sleep(1)

print("현재 URL: ", driver.current_url)

assert "/browse" in driver.current_url, "페이지 이동 실패"
print("성공적으로 페이지 이동!")

cookies = driver.get_cookies()
print("로그인 후 저장된 쿠키: ", cookies)

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(2)

driver.refresh()
print("이제 로그인 상태가 유지됩니다!")

time.sleep(3)

try:
    logout_button = driver.find_element(By.XPATH, "//button[text()='로그아웃']")
    assert logout_button.is_displayed(), "로그인이 되지 않았습니다!"
    print("로그인 후 로그아웃 버튼이 정상적으로 표시되었습니다!")
except Exception as e:
    print("로그아웃 버튼을 찾을 수 없습니다.", str(e))


input("Enter를 누르면 창이 닫힙니다...")
driver.quit()