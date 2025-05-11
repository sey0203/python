from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import login
import time
from datetime import datetime

# ✅ Chrome WebDriver 실행  
driver = webdriver.Chrome()

time.sleep(2)

driver.get("http://localhost:3000/login")

time.sleep(2)


driver.add_cookie({'domain': 'localhost', 'httpOnly': False, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2M4MDVlZGMzYWI3Y2MyNDkzNWYzNWQiLCJpYXQiOjE3NDEzMTM0NDN9.nd2F-srgGGUw-psyxgbXrZ4VgtdUsOepP6IksxkzVDU'})

time.sleep(2)

url = driver.current_url
print(url)