# my05.py
# DELETE

import pymysql
conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8")
cur = conn.cursor()
sql = "DELETE FROM member WHERE no=%s"
cur.execute( sql, (3) ) # 1개만 있어도 () 묶어줘야 함!
conn.commit()
conn.close()
print("삭제 성공")
