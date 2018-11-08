# my01.py
# SELECT All
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8")
cur = conn.cursor()
sql  = "SELECT * FROM member"
# data fetch
cur.execute(sql)     # 1. sql 쿼리문 실행
rows= cur.fetchall() # 2. fetchall : 실행한 후에 그 결과를 가져온다!
print(rows)
conn.close()