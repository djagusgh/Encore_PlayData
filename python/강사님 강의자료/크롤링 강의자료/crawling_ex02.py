from selenium import webdriver
import time

driver = webdriver.Chrome("C:\driver\chromedriver.exe")# 드라이버를 통해 크롬 열기
driver.get("https://www.google.com/") # 열어진 크롬을 통해 사이트 접속
time.sleep(5) # 정해진 시간 후에 쉬는 시간

assert "Google" in driver.title # 테스트
# <input name="q" ... >
elem = driver.find_element_by_name("q")
elem.clear() # 혹시 내용이 있으면 지운다.
elem.send_keys("미세먼지") # 키보드로 문자를 입력한다.
elem.submit()

time.sleep(30)
driver.close() # 열어진 크롬을 닫는다