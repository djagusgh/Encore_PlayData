# crawl_tour.py
# pip install BeautifulSoup4
# pip install selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.by

main_url = "http://tour.interpark.com/"
keyword = "파리"  # 키워드 직접 입력 -> 하드코딩, 변경이 힘들다


driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
time.sleep(3) # 절대적 : 무조건 정해진 시간(초)를 쉰다.

# 입력란 찾기 <input id="SearchGNBText" ...>
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword)
# elem.submit() ==> 작동이 안됨! 이유 : 자바스크립트 호출해야 검색이 됨

# 검색 버튼 찾기 <button class = "search-btn" ...>
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

# 특정 요소를 얻으면 바로 진행 (oTravelBox가 뜨면..!)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as e:
    print("대기중 에러")


# id, class로 되어있지 않을때 찾는 법
# 크롬에서 경로 찾고 싶은 tag 오른쪽 마우스 -> copy -> copy selector
# moreBtn 결과 : body > div.container > div > div > div.panelZone > div.oTravelBox > ul > li.moreBtnWrap > button
# body부터 다 복사할 필요없음

time.sleep(3)
driver.find_element_by_css_selector(".oTravelBox > ul > li.moreBtnWrap > button").click()

# 묵시적 : 페이지가 다 뜨면 진행
driver.implicitly_wait(10) # seconds
"""
http://search-tour.interpark.com/PC/Result?search=%ED%8C%8C%EB%A6%AC&code1=R&code2=

"""
# 현재 
for page in range(1, 2): # 웹페이지 맨 아래 1 ~ 10 써있는 거
    # javascript 실행
    driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
    driver.implicitly_wait(5)
    print("{} 페이지로 이동!!!".format(page))
    # 각 box 정보 긁어오기
    boxItems = driver.find_elements_by_css_selector("div.oTravelBox > ul > li")
    print("boxItems = ", boxItems)
    for li in boxItems:
        

      
time.sleep(30)
driver.close()

