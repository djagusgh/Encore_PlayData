# -- coding: utf-8 --
# guest.py
from flask import Flask, render_template, request, redirect
from sqlite3 import dbapi2 as sqlite3

DATABASE = 'guest.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with connect_db() as db:
        with open('schema.sql', 'r', encoding="utf-8") as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_db')
def create_db():
    init_db()
    return 'Create TABLE success!!!'

# 방명록 쓰기 부분(INSERT)
@app.route('/write', methods=['GET','POST'])
def write():
    if request.method == 'POST':
        sql = "insert into guest(writer, title, content) values(?,?,?)"
        writer = request.form['writer'] # 글쓴이
        title = request.form['title'] # 제목
        content = request.form['content'] # 내용

        datas = [writer, title, content] 
        db = connect_db()
        db.execute(sql, datas)
        db.commit()

        # return '저장 성공!!!'
        return redirect('/list') # list로 돌아가기!
    else:
        return render_template('writeform.html') 

# 방명록 확인 부분(SELECT)
@app.route('/list')
def list():
    db = connect_db()
    sql = "select * from guest order by no desc"
    cur = db.execute(sql)
    db.execute(sql)
    # print(cur.fetchall())
    guests = [ dict(no=row[0], writer=row[1], title=row[2], content=row[3], regdate=row[4])
    for row in cur.fetchall()]
    print(guests)

    return render_template('list.html', guests=guests)
    
if __name__ == "__main__":
    app.run(debug=True)
