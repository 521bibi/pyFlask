from flask import Flask,redirect,url_for,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    context = {
        'username':'bill',
        'gender':'男',
        'age':21
    }
    return render_template('index.html',**context)

@app.route('/login/')
def login():
    return '这是登录页面!'

@app.route('/ask/<is_login>')
def ask(is_login):
    if is_login=='1':
        return '这是提问页面！'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()