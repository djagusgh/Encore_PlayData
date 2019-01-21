from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        if username == 'hong' and pwd == '1234':
            session['username'] = username
            print('로그인 성공')
        return redirect('/')
    else:
        return render_template('loginForm.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)