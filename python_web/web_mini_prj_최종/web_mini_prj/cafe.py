# cafe.py
from flask import Flask, render_template, request, redirect, session
from flaskext.mysql import MySQL
import pymysql
import os


mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config.from_object(__name__)

app.secret_key = os.urandom(24)

mysql.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')



@app.route('/login',methods=['post','get'])
def login():
    if request.method == 'POST':
        id = request.form['email']
        pw = request.form['password']

        print('id =====', id )
        print('pw =====', pw )
        data = (id, pw)
        conn = mysql.connect()
        cur = conn.cursor()
        sql = 'SELECT * FROM member_info WHERE ID=%s AND PASSWORD=%s'
        cur.execute(sql, data)
        test = cur.fetchall()
        print(test)
        for t in test:
            nick = t.get('NICK_NAME')
            print(nick)
            session['NICK_NAME'] = nick
        print('---어디감---')
        # nick = test['NICK_NAME']
        # session['NICK_NAME'] = nick
        # print(session['NICK_NAME'])

        try:
            if pw == test[0]['PASSWORD']:
                print('login success')
                sql2 = 'SELECT * FROM cafe_info'
                cur.execute(sql2)
                test2 = cur.fetchall()

                session['id'] = id
                print(session['id'])
                print(session)
                conn.close()
                return render_template('contents.html' , cafes=test2)
            else:
                return render_template('main.html')
        except:
            return render_template('main.html')
    else:
        return render_template('main.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        nick = request.form['nick']
        # birth = request.form['birth']
        birth = request.form['birth-year'] + request.form['birth-month'] + request.form['birth-day']
        sql = 'insert into member_info(NICK_NAME, ID, PASSWORD, BIRTH_DATE) values(%s,%s,%s,%s)'
        data = (nick, id, pw, birth)
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        conn.close()
        print("저장 성공!!!!!")
        return redirect('/')
    else:
        return render_template('join.html')


@app.route('/contents')
def contents():
    # SELECT 해와서 정보를 contents.html로 넘김
    
    conn = mysql.connect()
    cur = conn.cursor()
    sql = "SELECT * FROM cafe_info"
    cur.execute(sql)
    cafes = cur.fetchall()

    sql2 = "SELECT * FROM review_db"
    cur.execute(sql2)
    reviews = cur.fetchall()

    print('cafes=============', cafes)
    return render_template('contents.html', cafes=cafes, reviews = reviews)



@app.route('/contents/review_write/<int:num>/<cafe>', methods=['GET', 'POST'])

def write_review(num, cafe):
    print('왜 안나와')
    print(session['id'])
    
    if request.method == 'POST':
        id = session['id']# 로그인 정보를 입력
        nick = session['NICK_NAME']
        cafe_name = cafe # 들어 갔던 카페 이름으로!
        rec_menu = request.form['rec_menu']
        score = request.form['score']
        review = request.form['review']
        
        # num, cafe_name -> 이전 장에서 받아와야!
        sql = "INSERT INTO review_db(num, id, NICK_NAME, CAFE_NAME, REC_MENU, SCORE, REVIEW) values (%s, %s, %s, %s, %s, %s, %s)"
        data = (num, id, nick, cafe_name, rec_menu, score, review)
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        conn.close()
        return redirect('/contents')
    else:
        return render_template('review_write.html', cafe=cafe)


if __name__ == '__main__':
    app.run(debug=True)