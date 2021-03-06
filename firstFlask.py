from flask import Flask,redirect,url_for,render_template,request,g,session
from flask_sqlalchemy import SQLAlchemy
import config
import os
from datetime import timedelta
from utils import login_log

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')
    # class Person(object):
    #     name = 'Lily'
    #     age = 18
    #
    # p = Person()
    #
    # context = {
    #     'username':'bill',
    #     'gender':'男',
    #     'age':21,
    #     'person': p,
    #     'website':{
    #         'baidu':'www.baidu.com',
    #         'google':'www.google.com'
    #     }
    # }
    # return render_template('index.html',**context)

@app.route('/search')
def search():
    q = request.args.get('q')
    return '用户提交的查询参数是:%s'%q

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'bill' and password == '123456':
            session['username'] = 'bill'
            return '登录成功'
        else:
            return '您的用户名或密码错误'

@app.route('/edit/')
def edit():
    if session.get('username'):
        return '修改成功'
    else:
        return redirect(url_for('login'))

# @app.route('/questions/<is_login>')
# def questions(is_login):
#     if is_login=='1':
#         user = {
#             'username':'nike',
#             'age':18
#         }
#         websites = ['baidu','google']
#         return render_template('questions.html',user=user,websites=websites)
#     else:
#         return redirect(url_for('login'))

# @app.before_request
# # def my_before_request():
# #     username = session.get('username')
# #     if username:
# #         g.username = session.get('username',username='bill')

@app.context_processor
def my_context_processor():
    # username = session.get('username')
    # if username:
    #     return {'username',username='bill'}
    return {'username':'bill'}

@app.route('/questions/<is_login>')
def questions(is_login):
    if is_login=='1':
        books = [
            {
                'name':'西游记',
                'author':'吴承恩',
                'price':120
            },
            {
                'name':'红楼梦',
                'author':'曹雪芹',
                'price':130
            },
            {
                'name':'三国演义',
                'author':'罗贯中',
                'price':140
            },
            {
                'name':'水浒传',
                'author':'施耐庵',
                'price':110
            },

        ]
        return render_template('questions.html',books=books)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()