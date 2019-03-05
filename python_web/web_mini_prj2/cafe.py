# cafe.py
from flask import Flask, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL
import pymysql

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)
app.secret_key = 'any random string'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config.from_object(__name__)

mysql.init_app(app)

@app.route('/')
def index():

    print("세션 ", session)

    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        conn = mysql.connect()
        cur = conn.cursor()
        sql = "SELECT ID, PASSWORD FROM member_info"
        cur.execute(sql)
        members = cur.fetchall()

        print("멤버 =======", members)

        # 사용자 입력 id, 비번을 dictionary 형태로
        input_dict = {}
        input_dict['ID'] = username
        input_dict['PASSWORD'] = password

    
        if input_dict in members:
            session['username'] = username
                    
            sql2 = "SELECT NICK_NAME FROM member_info WHERE ID = %s"
            cur.execute(sql2, session['username'])
            nick_name = cur.fetchone()['NICK_NAME']
            session['nick_name'] = nick_name 
        
        return redirect('/')
            
        
    else:
        return render_template('main.html')
        
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

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
    if request.method == 'POST':
        
        id = '가가가가' # 로그인 정보를 입력
        nick = request.form['nick']
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

"""


/* 카페정보 */
CREATE TABLE CAFE_INFO (
   num INT PRIMARY KEY AUTO_INCREMENT,
   CAFE_NAME VARCHAR2(200) NOT NULL, /* 카페 이름 */
   ADDRESS VARCHAR2(200) NOT NULL, /* 주소 */
   MENU VARCHAR2(200) NOT NULL, /* 대표 메뉴 */
   STAR_RATING VARCHAR2(200) NOT NULL, /* 별점 */
   PHONE_NUMBER VARCHAR2(200) NOT NULL /* 전화번호 */
);


/* 회원정보 */
CREATE TABLE MEMBER_INFO (
   NICK_NAME VARCHAR2(200) NOT NULL, /* 닉네임 */
   ID VARCHAR2(200) NOT NULL, /* ID */
   PASSWORD VARCHAR2(200) NOT NULL, /* 비밀번호 */
   BIRTH_DATE VARCHAR2(200) NOT NULL /* 생년월일 */
);

/* 후기 */
CREATE TABLE REVIEW_DB (
   num INT(20) NOT NULL,
   id VARCHAR(200) NOT NULL, /* 후기번호 */
   NICK_NAME VARCHAR(200) NOT NULL, /* 닉네임 */
   CAFE_NAME VARCHAR(200) NOT NULL, /* 카페 이름 */
   REC_MENU VARCHAR(100) NOT NULL, /* 메뉴 추천 */
   SCORE VARCHAR(200) NOT NULL, /* 별점 */
   REVIEW VARCHAR(200) NOT NULL /* 후기 */
);
"""