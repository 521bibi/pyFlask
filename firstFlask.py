from flask import Flask,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

db.create_all()

@app.route('/')
def index():
    class Person(object):
        name = 'Lily'
        age = 18

    p = Person()

    context = {
        'username':'bill',
        'gender':'男',
        'age':21,
        'person': p,
        'website':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('index.html',**context)

@app.route('/login/')
def login():
    return render_template('login.html')


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