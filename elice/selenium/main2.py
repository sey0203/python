import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:3000/signup")

time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("seytest3")
driver.find_element(By.NAME, "email").send_keys("seytest3@naver.com")
driver.find_element(By.NAME, "password").send_keys("pw3")
driver.find_element(By.NAME, "passwordConfirm").send_keys("pw3")

signup_btn = driver.find_element(By.XPATH, "//button[text()='회원가입']").click()

time.sleep(2)

alert = driver.switch_to.alert
print("메시지 : ", alert.text)
alert.accept()
print("Alert이 정상적으로 처리되었습니다.")

time.sleep(2)

print("현재 URL: ", driver.current_url)
assert "login" in driver.current_url, "로그인 페이지로 이동하지 못했습니다."
print("성공적으로 로그인 페이지 이동")


input("Enter를 누르면 창이 닫힙니다...")
driver.quit()