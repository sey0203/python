from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import login
import time
from datetime import datetime

# ✅ Chrome WebDriver 실행  
# with webdriver.Chrome() as driver:
#    wait = ws(driver, 10)

driver = webdriver.Chrome()
wait = ws(driver, 10)  # ✅ driver 유지


time.sleep(2)

try:
    login.login(ws, EC, By, driver)
    # wait.until(lambda d: "login" not in driver.current_url)


    today = datetime.today().strftime("%Y-%m-%d")
    print("오늘 날짜는: ", today)
    
    time.sleep(3)
    date_div = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[text()='{today}']")))

    # date_div = driver.find_element(By.XPATH, f"//div[text()='{today}']")


    schedule_container = date_div.find_element(By.XPATH, "following-sibling::div")

    first_schedule = schedule_container.find_element(By.XPATH, "./div[1]")

    first_schedule_title = first_schedule.text.strip()
    print(f"선택한 첫 번째 일정: {first_schedule_title}")

    first_schedule.click()

    time.sleep(2)

    detail_url = driver.current_url
    print(f"상세 페이지: {detail_url}")

    schedule_id = detail_url.split("/")[-1]
    print(f"추출된 일정 ID: {schedule_id}")

    edit_url = f"http://localhost:3000/edit/{schedule_id}"
    driver.get(edit_url)

    #edit_url = detail_url.replace("/detail/", "/edit/")
    #driver.get(edit_url)

    time.sleep(2)

    title_input = driver.find_element(By.ID, "title")

    # React 상태 동기화를 위한 이벤트 발생
    driver.execute_script("""
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }))
    """, title_input)

    time.sleep(2)

    title_input.clear()
    title_input.send_keys("업데이트된 회의 제목")

    description_input = driver.find_element(By.CSS_SELECTOR, "input[name='description']")
    description_input.clear()
    description_input.send_keys("새로운 회의 내용입니다.")

    update_button = driver.find_element(By.XPATH, "//button[text()='수정 완료']")
    update_button.click()

    time.sleep(2)

    if "detail" in driver.current_url:
        print("✅ 일정 수정 자동화 테스트 성공!")

    else:
        print("❌ 일정 수정 실패")

except TimeoutException as TIE:
  print("타임아웃: ", str(TIE))

except NoSuchElementException as NSE:
  print("검색 결과 없음: ", str(NSE))
