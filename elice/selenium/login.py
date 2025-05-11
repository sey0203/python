def login(ws, EC, By, driver):
  driver.get("http://localhost:3000/login")

  login_button = ws(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '로그인')]"))
  )

  # ✅ 이메일 & 비밀번호 입력
  driver.find_element(By.NAME, "email").send_keys("test1@naver.com")
  driver.find_element(By.NAME, "password").send_keys("pw1")

  login_button.click()