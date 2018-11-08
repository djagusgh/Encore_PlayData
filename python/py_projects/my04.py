# my04.py
# UPDATE
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8")
cur = conn.cursor()
sql = """
    UPDATE member SET name=%s, age=%s, email=%s
    WHERE no=%s
"""

cur.execute( sql, ('임꺽순',41,'soon@ddd.com',3) )
conn.commit()
conn.close()
print("수정 성공")