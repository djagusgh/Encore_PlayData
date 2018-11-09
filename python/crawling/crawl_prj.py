import time
import math
from bs4 import BeautifulSoup

from selenium import webdriver
# https://selenium-python.readthedocs.io/waits.html#explicit-waits 코드를 복사
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


main_url = "https://www.skyscanner.co.kr/"
keyword = "후쿠오카"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
time.sleep(3) # 무조건 정해진 시간(초) 쉰다.

one_way = driver.find_element_by_id("fsc-trip-type-selector-one-way") #.send_keys(keyword)
one_way.click()
# elem.send_keys(keyword)
time.sleep(2)
destination = driver.find_element_by_id("destination-fsc-search") #.send_keys(keyword)
destination.clear()
destination.send_keys(keyword)
time.sleep(2)
start_day = driver.find_element_by_id("button.bpk-calendar-date-1Mg7I bpk-calendar-date--focused-1KUc- bpk-calendar-date--selected-3V6m1") #.send_keys(keyword)
start_day.click("2018년 11월 10일 토요일")
#time.sleep(2)
#return_day = driver.find_element_by_id("return-fsc-datepicker-button") #.send_keys(keyword)
#return_day.clear()
#return_day.send_keys("2018. 11. 11.")
#time.sleep(2)
#btn_search = driver.find_element_by_css_selector("button.bpk-button-2YQI1 bpk-button--large-1Z1P5 SubmitButton-WxCV2")
#btn_search.click()

time.sleep(5)
driver.close()