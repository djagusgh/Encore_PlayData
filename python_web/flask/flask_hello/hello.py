from flask import Flask, render_template

app = Flask(__name__)

## URL 요청이 들어왔을 때 처리해주는 코드

# http://localhost:5000/ 요청을 처리
@app.route("/") # route : 경로
def index():
    return "Hello Flask!"

# http://localhost:5000/abc 요청을 처리
@app.route("/abc")
def abc():
    return "abc를 요청하셨군요 선생님!!!"

# http://localhost:5000/ddd 요청을 처리
@app.route("/ddd")
def ddd():
    return 'ddd를 요청하셨군요.'

# http://localhost:5000/hello 요청을 처리
@app.route('/hello')
def hello():
    return render_template('hello.html') # hello.html : templates 폴더에 저장하는 것이 약속!

# ex) http://localhost:5000/hi/hong
@app.route('/hi/<name>')
def hi(name): # name : hong
    return render_template('hello2.html', name=name)


if __name__ == '__main__': # 직접 실행되냐, 다른 곳에서 import되서 실행되냐
    app.run(debug=True) # 자동 reload