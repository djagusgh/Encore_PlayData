# SELECT + WHERE
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8")
cur = conn.cursor(pymysql.cursors.DictCursor) # dictionary로 값 받음
sql = "SELECT * FROM member WHERE name=%s and age=%s"
cur.execute(sql, ('홍길동', 25) )
row = cur.fetchone()
print(row)
conn.close()
# {'no': 1, 'name': '홍길동', 'age': 25, 'email': 'hong@aaa.com'}