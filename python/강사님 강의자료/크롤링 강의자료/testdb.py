import pymysql
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


tour = ['title','link','img','comments','period', 'depart', 'price','score','reservation','feature']

insert_tour(tour)