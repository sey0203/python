import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:3000/login")


time.sleep(1)


button = driver.find_element(By.XPATH, "//button[text()='테마 변경']")
before_color = button.value_of_css_property("background-color")
print("변경 전 배경색: ", before_color)


button.click()

WebDriverWait(driver, 5)

after_color = button.value_of_css_property("background-color")
print("변경 후 배경색: ", after_color)

assert before_color != after_color, "버튼 클릭 후 색상이 변하지 않았습니다!"
print("테마 변경 테스트 성공!")


input("Enter를 누르면 창이 닫힙니다...")
driver.quit()