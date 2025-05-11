import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:3000/login")

time.sleep(1)

print("현재 페이지 제목: ", driver.title)
print("현재 URL: ", driver.current_url)

input("Enter를 누르면 창이 닫힙니다...")
driver.quit()