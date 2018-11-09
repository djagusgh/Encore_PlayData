from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

# 사이트 접속
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get("https://www.mangoplate.com/")
time.sleep(2)

# 광고삭제
#btn_search = driver.find_element_by_css_selector("button.ad_btn ad_block_btn")
#btn_search.click()

market_count = 2
subject_count = 2
tag = 1

#맛집리스트 클릭
list_button = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
list_button.click()
time.sleep(2)

#태그 클릭
while (True ):
    tag += 1
    if (tag >=11):
        break
    subject_count = 1
    tag_subject2 =  WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/main/article/section/div/div/p/button[%d]"%(tag))))
    tag_button = driver.find_element_by_xpath("/html/body/main/article/section/div/div/p/button[%d]"%(tag)) 
    tag_button.click()
    time.sleep(1)
    # 태그 > 주제 들어가기
    while(True):
        market_count = 0
        subject_count += 1
        subject_button2 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/main/article/section/div/ul/li[%d]/a/figure/figcaption/div/span"%(subject_count))))
        subject_button = driver.find_element_by_xpath("/html/body/main/article/section/div/ul/li[%d]/a/figure/figcaption/div/span"%(subject_count))
        subject_button.click()
        time.sleep(1)
        # 태그 > 주제 > 가게 들어가기 
        while(True):
            try:
                market_count += 1
                market_button2 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="contents_list"]/ul/li[%d]/div/a'%(market_count))))
                market_button = driver.find_element_by_xpath('//*[@id="contents_list"]/ul/li[%d]/div/a'%(market_count))
                market_button.click()
                time.sleep(1)
                
                # 태그 > 주제 > 가게 > 가게정보 DB저장
                while(True):
                    print("%d 태그 ,%d 주제 , %d 가게 DB저장성공"%(tag,subject_count,market_count))
                    time.sleep(1)
                    break
                driver.back()
                time.sleep(1)
            except:
                try:
                    market_more_button2 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="contents_list"]/div/button')))
                    market_more_button = driver.find_element_by_xpath('//*[@id="contents_list"]/div/button')
                    if market_count >=11:
                        for i in range(market_count//10):
                            market_more_button.click()
                            time.sleep(1)
                    market_count -= 1 
                    
                except:
                    #더보기가 없는 에러처리 
                    driver.back()
                    tag2 = tag
                    tag_subject2 =  WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/main/article/section/div/div/p/button[%d]"%(tag2))))
                    tag_button = driver.find_element_by_xpath("/html/body/main/article/section/div/div/p/button[%d]"%(tag2))
                    tag_button.click()
                    time.sleep(2)   
                    try:
                        subject_count += 1
                        subject_button2 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/main/article/section/div/ul/li[%d]/a/figure/figcaption/div/span"%(subject_count))))
                        subject_button = driver.find_element_by_xpath("/html/body/main/article/section/div/ul/li[%d]/a/figure/figcaption/div/span"%(subject_count))
                        subject_button.click()
                        time.sleep(1)
                        market_count = 0
                        continue
                    except:
                        try:
                            subject_more_button2 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/article/section/div/a')))
                            subject_more_button2 = driver.find_element_by_xpath('/html/body/main/article/section/div/a')
                            subject_more_button2.click()
                            time.sleep(1)
                            subject_count -= 1
                            break
                        except:
                            break
        break
print("크롤링끝!")