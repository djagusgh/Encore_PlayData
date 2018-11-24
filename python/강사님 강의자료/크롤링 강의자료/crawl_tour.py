# crawl_tour.py
# pip install BeautifulSoup4
# pip install selenium
import math
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql

# from selenium.webdriver.common.by

main_url = "http://tour.interpark.com/"
keyword = "파리"  # 키워드 직접 입력 -> 하드코딩, 변경이 힘들다


driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
# time.sleep(3) # 1) 절대적 : 무조건 정해진 시간(초)를 쉰다.
driver.implicitly_wait(10) # 2) 묵시적으로...

# 입력란 찾기 <input id="SearchGNBText" ...>
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword) # 파리
# elem.submit() ==> 작동이 안됨! 이유 : 자바스크립트 호출해야 검색이 됨

# 검색 버튼 찾기 <button class = "search-btn" ...>
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

# 특정 요소를 얻으면 바로 진행 (oTravelBox가 뜨면..!)
# 3) 명시적 기다리기 : 특정한 자원을 얻으면 바로 진행!
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

driver.find_element_by_css_selector(".oTravelBox > ul > li.moreBtnWrap > button").click()
time.sleep(3)

# 묵시적 : 페이지가 다 뜨면 진행
# driver.implicitly_wait(10) # seconds
"""
http://search-tour.interpark.com/PC/Result?search=%ED%8C%8C%EB%A6%AC&code1=R&code2=
지금까지 페이지
"""
"""
자동 페이지 이동 -> selenium 이용
태그 parsing -> selenium도 가능하지만, Beautifulsoup로 파싱하는게 더 편하다
(아래 코드는 Selenium으로 파싱함)
"""

# span_obj 해외여행 114개 (obj : 객체 의미로 이름에 붙임)
span_obj = driver.find_element_by_css_selector("div.panelZone > div.oTravelBox > h4 > span")
str_numbers = span_obj.text
print(span_obj)
#print("str_numbers=", "---" + str_numbers + "---") # 혹시 공백있나 확인
str_numbers = str_numbers.replace("(", "")
str_numbers = str_numbers.replace(")", "")
#print("str_numbers=", str_numbers)

# end : 몇 페이지까지 있는지
number = int(str_numbers)
#print(type(number))
end = math.ceil(number / 10) # 올림!

tour_list = []

def insert_tour(tour):
    conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='pythondb', charset="utf8")
    cur = conn.cursor()
    sql = """ INSERT INTO tbl_tour(title,link,img,comments,period, depart, price,score,reservation,feature)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql, tour)
    conn.commit()
    conn.close()

    print("저장 성공!!!")

        
try:
    # for page in range(1, end + 1):
    for page in range(1, 2): # page : 웹페이지 맨 아래 1 ~ 10 써있는 거, test용
        try:# javascript 실행
            driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))

            # 에러
            # driver.implicitly_wait(5) # <== 반복문 안에서 사용 x
            # 이유 : 반복문 안에서 빨리 작동되어 페이지 로드를 완료 못함

            time.sleep(2)
            print("{} 페이지".format(page))
            boxItems = driver.find_elements_by_css_selector("div.panelZone > div.oTravelBox > ul > li")
            #print( len(boxItems) )
            #print( boxItems ) # 10개의 리스트 객체 출력됨!
            # 하나씩 처리 ㄱㄱ
            for li in boxItems:
                # print('li', li) # 객체 1개씩 출력, 내용물이 안보임-> 디버깅이 어렵다
                # <a onclick="???"">
                a_obj = li.find_element_by_css_selector("a")
                str_onclick = a_obj.get_attribute("onclick")
                l_list = str_onclick.split(",")
                str_link = l_list[0]
                str_link = str_link.replace("searchModule.OnClickDetail('", "")
                str_link = str_link.replace("'", "")
                # print(str_link)
            
                # <img src="???" >
                img = li.find_element_by_css_selector("img")
                str_img_src = img.get_attribute("src")

                proTit = li.find_element_by_css_selector(".proTit")
                str_title = proTit.text

                proSub = li.find_element_by_css_selector(".proSub")
                str_comment = proSub.text

                # .proInfo class가 2개있음
                proInfos = li.find_elements_by_css_selector(".proInfo")
                obj_period = proInfos[0]
                str_period = obj_period.text
                #print(str_period)
                
                obj_start = proInfos[1]
                str_start = obj_start.text
                #print(str_start)

                # 여행 가격
                proPrice = li.find_element_by_css_selector(".proPrice")
                str_price = proPrice.text
                #print(str_price)
                proInfo = li.find_element_by_css_selector("div.info-row > div:nth-child(2) > p:nth-child(2)")
                str_score = proInfo.text
                #print(str_score)
                # 튜플에 여행정보를 담는다.
                tour = [str_title, str_link, str_img_src, str_comment, str_period,
                str_start, str_price, str_score]
                # 여행리스트에 담는다.
                tour_list.append(tour)
        except Exception as e:
            print("페이지 파싱 에러", e)
    # for 1 end
    for tour in tour_list:
        # print(tour)
        link = tour[1]
        # print(link)
        driver.get(link)
        time.sleep(2)
        # 이번엔 Selenium말고 BeautifulSoup 를 사용해보자!
        soup = BeautifulSoup(driver.page_source, "lxml")
        trs = soup.select("table.ui-data-table > tbody > tr") # select는 결과 1개여도 리스트를 리턴
        tr2 = trs[2]
        td = tr2.find("td")
        # td는 [<strong>예약 0명</strong>, <br/>, '(총 예정인원 10명/ 최소 출발 2명)']
        # 로 정해진 상태!
        strong = td.contents[0] # <strong>예약 0명</strong>
        str_reservation = strong.string # 예약 0명
        aaa = td.contents[2]    # '(총 예정인원 10명 / 최소출발 2명)'
        str_reservation = str_reservation + aaa # 예약 0명 '(총 예정인원 10명 / 최소 출발 2명)'
        #print(str_reservation)
        tour.append(str_reservation)
        lis = soup.select(".goods-point > .ui-con-list > li")
        # print(lis)
        str_feature = ""
        for li in lis:
            str_feature = str_feature + li.string + " "
        tour.append(str_feature)
        insert_tour(tour)
    # for 2 end
    print( len(tour_list) )
    print( tour_list )
    
finally:
    driver.close()
#    (str_title, str_link, str_img_src, str_comment, str_period,
# str_start, str_price, str_score, str_reservation, str_feature)
# 마지막 2개는 상세페이지에...!

"""
create table tbl_tour(
	num int not null auto_increment,
	title varchar(100),
	link varchar(200),
	img varchar(100),
	comments varchar(100),
	period varchar(50),
	depart varchar(50),
	price varchar(50),
	score varchar(10),
	reservation varchar(50),
	feature varchar(200),
	primary key(num)
)
"""