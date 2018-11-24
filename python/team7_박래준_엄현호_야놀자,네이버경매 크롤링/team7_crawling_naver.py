import time
import math
import pymysql
from bs4 import BeautifulSoup

from selenium import webdriver


# https://selenium-python.readthedocs.io/waits.html#explicit-waits 코드를 복사
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


main_url = "https://land.naver.com/auction/"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
time.sleep(3) # 무조건 정해진 시간(초) 쉰다.

Auction_list = []
def insert_auction(auction):
    conn = pymysql.connect(host='192.168.113.157', user='root', password='1234', db='test', charset='utf8')
    cur = conn.cursor()
    sql = """INSERT INTO apart1_auction(str_link, str_land_num, str_land_type, str_land_area, str_land_surface, str_land_site, str_land_high_price, str_land_low_price, str_land_condition, str_land_date, str_land_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute( sql, auction )
    conn.commit()
    conn.close()
    print("저장 성공!")
sub_url = "https://goodauction.land.naver.com/auction/ca_view.php?product_id="
citys = ["서울", "경기", "인천", "부산", "대구", "대전", "광주", "울산", "세종", "강원", "경북", "경남", "충북", "충남", "전북", "전남", "제주"]
click1 = ["areaBtn11", "areaBtn41", "areaBtn28", "areaBtn26", "areaBtn27","areaBtn30", "areaBtn29", "areaBtn31", "areaBtn36", "areaBtn42", "areaBtn47", "areaBtn48", "areaBtn43", "areaBtn44", "areaBtn45", "areaBtn46", "areaBtn50"]
try:
    for i in click1:
        driver.get("https://land.naver.com/auction/")
        time.sleep(2)
        close_info = driver.find_element_by_id(i).click()
        print("{}번째까지는 잘됨".format(i))
        #for j in citys:
        # print(j)
            #time.sleep(2)
        time.sleep(2)
        span_obj = driver.find_element_by_id("total_record")
        str_numbers = span_obj.text
        print(str_numbers)
        #print("str_numbers=", "---" + str_numbers + "---") # 혹시 공백있나 확인
        str_numbers = str_numbers.replace("(총 ", "")
        str_numbers = str_numbers.replace("건)", "")
        print("str_numbers=", str_numbers)

        # end : 몇 페이지까지 있는지
        number = int(str_numbers)
        print(type(number))
        end = math.ceil(number / 30) # 올림!
        print(end)
    

        try:
            for page in range(0, end+1):
            #for page in range(1,2): #테스트용
                # 자바스크립트 실행
                try:
                    time.sleep(1)
                    if page == 0:
                        list_num = driver.find_element_by_xpath('//*[@id="page_navi"]/div/strong')
                        #driver.execute_script("#page_navi > div > a:nth-child({})".format(page))
                        #driver.implicitly_wait(5) # 반복문 안에서는 사용하지 말 것!!!
                        #이유 : 반복문 안에서 너무 빨리 작동되어 페이지 로드를 완료 못함!!!
                        # 에러
                    elif page >= 1:
                        list_num = driver.find_element_by_xpath('//*[@id="page_navi"]/div/a[{}]'.format(page)).click()
                        time.sleep(2)
                    print("{} 페이지".format(page))
                    box_item = driver.find_element_by_id("tb")
                    box_item2 = box_item.find_elements_by_tag_name("tr")
                    print(len(box_item2))
                    box_list = len(box_item2)
                    
                    for tr in box_item2:
                        a_obj = tr.find_element_by_tag_name("a")
                        #print(a_obj)
                        str_onclick = a_obj.get_attribute("onclick")
                        #print(str_onclick)
                        l_list = str_onclick.split(",")
                        #print(l_list)
                        str_link = l_list[1]
                        #print(str_link)
                        str_link = str_link.replace(");","")
                        print(str_link)
                        land_num = tr.find_element_by_css_selector(".num")
                        str_land_num = land_num.text
                        #print(str_land_num)
                        tds = tr.find_elements_by_tag_name("td")
                        # print(tds)
                        str_land_type = tds[2].text
                        #print(str_land_type) 
                        land_area = tr.find_element_by_css_selector(".area")
                        land_area1 = land_area.find_element_by_tag_name("a")
                        str_land_area = land_area1.text
                        #print(str_land_area)
                        land_surface = tr.find_element_by_xpath('//*[@id="tb"]/tr[16]/td[4]/p/span[1]/em')
                        str_land_surface = land_surface.text
                        print(str_land_surface)
                        land_site = tr.find_element_by_xpath('//*[@id="tb"]/tr[17]/td[4]/p/span[3]/em')
                        str_land_site = land_site.text
                        print(str_land_site)
                        land_high_price = tr.find_element_by_css_selector(".num_type1")
                        str_land_high_price = land_high_price.text
                        #print(str_land_high_price)
                        land_low_price = tr.find_element_by_css_selector(".num_type2")
                        str_land_low_price = land_low_price.text
                        #print(str_land_low_price)
                        tds1 = tr.find_elements_by_tag_name("td")
                        str_land_condition = tds1[5].text
                        #print(str_land_condition)
                        land_date = tr.find_element_by_css_selector(".date")
                        str_land_date = land_date.text
                        #print(str_land_date)
                        land_count = tr.find_element_by_css_selector(".count")
                        str_land_count = land_count.text
                        #print(str_land_count)
                        

                        auction = [str_link, str_land_num, str_land_type, str_land_area, str_land_surface, str_land_site, str_land_high_price, str_land_low_price, str_land_condition, str_land_date, str_land_count]
                        Auction_list.append(auction)
                        #print(Auction_list)
                        #print(Auction_list[0])
                        print("end-----------------------------------------------")
                        # 데이터베이스에 넣는다.
                        print(type(auction))
                        print(auction)
                        insert_auction(auction)
                        

                        # for i in range(1, box_list+1):
                        #     a_click = tr.find_element_by_css_selector("tr:nth-child({}) > td.area > a".format(i)).click()
                        #     time.sleep(2)
                        #     print("{} 클릭".format(i))
                        #     time.sleep(2)
                        #     #land_surface = driver.find_element_by_xpath("div/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]")
                        #     #str_land_surface = land_surface.text
                        #     #print(str_land_surface)
                        #     #time.sleep(2)
                    
                    
                    # for auction in Auction_list:
                        
                    #     link = sub_url + auction(str_link[t])
                    #     #print(link)
                    #     #link = auction[0]
                    #     print(link)
                    #     driver.get(link)
                    #     time.sleep(2)
                    #     str_land_surface = ""; str_land_site = ""; str_land_disposal_date = ""; 
                    #     str_land_floor = ""; str_land_room_structure = ""; str_land_feature = "";
                    # try:
                    #     land_surface = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)")
                    #     str_land_surface = land_surface.text
                    #     #print(str_land_surface)
                    #     land_site = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > em")
                    #     str_land_site = land_site.text
                    #     #print(str_land_site)
                    #     land_disposal_date = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2) > table > tbody > tr.last > td:nth-child(2)")
                    #     str_land_disposal_date = land_disposal_date.text
                    #     #print(str_land_disposal_date)
                    #     land_floor = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(2)")
                    #     str_land_floor = land_floor.text
                    #     #print(str_land_floor)
                    #     land_room_structure = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(5)")
                    #     str_land_room_structure = land_room_structure.text
                    #     #print(str_land_room_structure)
                    #     land_feature = driver.find_element_by_css_selector("#content2 > div > div.content_wrap > div.content > div:nth-child(4) > table > tbody > tr:nth-child(3) > td")
                    #     str_land_feature = land_feature.text
                    #     print(str_land_feature)
                    #     time.sleep(2)
                    #     #soup = BeautifulSoup( driver.page_source, "lxml")
                    #     # trs = soup.select("#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody > tr:nth-child(3)")
                    #     # print(trs)
                    #     print("sd")
                    #     auction.append(str_land_surface)
                    #     auction.append(str_land_site)
                    #     auction.append(str_land_disposal_date)
                    #     auction.append(str_land_floor)
                    #     auction.append(str_land_room_structure)
                    #     auction.append(str_land_feature)
                    #     print("td")
                    #     # 데이터베이스에 넣는다.
                    #     #print(type(auction))
                    #     #print(auction)
                    #     #insert_auction(auction)
                    #     #driver.back()
                    #     print(Auction_list)
                    #     Auction_list.remove(Auction_list[0])
                    #     print("end")
                    #     b = t+1
                        
                        
                    # except Exception as b1:
                    #     print("css 달라짐")
                except Exception as e3 :
                    print("페이지 파싱 에러 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^", e3)
                    
                # auction[0]
                # driver.get("https://land.naver.com/auction/")                    
                # time.sleep(1)
                # close_info = driver.find_element_by_id(i).click()
        #apart = driver.find_element_by_id("sale_type2").click()
        except Exception as e2 :
            print("e2--------------", e2)
        
except Exception as e1 :
    print("e1=============", e1)
finally:
    driver.close()