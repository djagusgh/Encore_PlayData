# my03.py
# INSERT
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8")
cur = conn.cursor()
sql = """ INSERT INTO member(name,age,email)
        VALUES(%s,%s,%s)"""
cur.execute(sql, ('임꺽정', 42, "im@ccc.com") )
conn.commit()
conn.close()

print("저장 성공!!!")