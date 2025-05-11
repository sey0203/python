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

try:
    login.login(ws, EC, By, driver)

    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[1]/a[2]").click()

    time.sleep(2)

    driver.find_element(By.ID, "title").send_keys("일정 제목 추가")

    description_input = driver.find_elements(By.NAME, "description")[1]
    # input("테스트 완료! 창을 닫으려면 Enter 키를 누르세요...")
    print("✅ tag_name:", description_input.tag_name)  # 요소 태그명 출력
    print("✅ class:", description_input.get_attribute("class"))  # class 속성 가져오기
    print("✅ id:", description_input.get_attribute("id"))  # id 속성 가져오기
    print("✅ class:", description_input.get_attribute("name"))  # class 속성 가져오기

    description_input.send_keys("일정 설명 추가")

    driver.find_element(By.ID, "location").send_keys("일정 장소 추가")


    today = datetime.today().strftime("%Y-%m-%d")
    print(f"오늘 날짜: {today}")


    date_input = driver.find_element(By.NAME, "date")

    # 날짜 입력 (오늘 날짜로 자동 설정)
    driver.execute_script("""
        const input = arguments[0];
        input.setAttribute('value', arguments[1]);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        """, date_input, today)
    print("날짜 값 확인: ", date_input.get_attribute("value"))
    
    start_time_input = driver.find_element(By.NAME, "startTime")

 # 시작 시간 입력
    driver.execute_script("""
        const input = arguments[0];
        input.setAttribute('value', '14:00');
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        """, start_time_input)
    
    print("시작 시간 값 확인: ", start_time_input.get_attribute("value"))


    end_time_input = driver.find_element(By.NAME, "endTime")

    # 종료 시간 입력
    driver.execute_script("""
        const input = arguments[0];
        input.setAttribute('value', '15:00');
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        """, end_time_input)
    
    print("종료 시간 값 확인: ", end_time_input.get_attribute("value"))


    
    creat_btn = driver.find_element(By.XPATH, "//button[text()='생성']")
    creat_btn.click()

    time.sleep(3)

    if "detail" in driver.current_url:
       print("✅ 일정 생성 테스트 성공!")

    else:
       print("❌ 일정 생성 실패 (400 Bad Request 가능)")

    input("Enter를 누르면 창이 닫힙니다...")
    driver.quit()

except TimeoutException as TIE:
  print("타임아웃: ", str(TIE))

except NoSuchElementException as NSE:
  print("검색 결과 없음: ", str(NSE))





# date_div = ws.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[text()='{today}']")))

# schedule_container = date_div.find_element(By.XPATH, "following-sibling::div")


# USER_NAME = "seytest3"

# user = driver.find_element(By.XPATH, "//input[@placeholder='사용자 검색']")
# user.send_keys(USER_NAME)

# time.sleep(2)

# search_user = driver.find_element(By.XPATH, f"//div[text()='{USER_NAME}']")
# search_user.click()