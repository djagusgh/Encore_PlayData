from selenium import webdriver
import time

driver = webdriver.Chrome("C:\driver\chromedriver.exe")# 드라이버를 통해 크롬 열기
driver.get("https://www.google.com/") # 열어진 크롬을 통해 사이트 접속
time.sleep(5) # 정해진 시간 후에 쉬는 시간
driver.close() # 열어진 크롬을 닫는다