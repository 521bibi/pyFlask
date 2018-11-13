from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# # article表：
# CREATE TABLE article(
#     id INT PRIMARY KEY auto_increment,
#     title VARCHAR(100) NOT null,
#     content TEXT NOT NULL
# )character set utf8;

# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer,primary_key = True,autoincrement = True)
#     title = db.Column(db.String(100),nullable = False)
#     content = db.Column(db.Text,nullable = False)

class User(db.Model):
     __tablename__ = 'user'
     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
     username = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.Text,nullable = False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('articles'))

db.create_all()

@app.route('/')
def index():
    # #增加：
    # user1 = User(username = 'bill')
    # db.session.add(user1)
    # #事务
    # db.session.commit()
    #
    # article1 = Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article1)
    # db.session.commit()

    # #增加：
    # article1 = Article(title='aaa',content='bbb')
    # db.session.add(article1)
    # #事务
    # db.session.commit()

    # #查
    # #select * from article where article.title= 'aaa';
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # print ('title:%s' % article1.title)
    # print ('content:%s' % article1.content)

    # #改
    # #1.先查出数据
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # #2.修改
    # article1.title = 'new title'
    # #3.事务提交
    # db.session.commit()

    # #删
    # #1.先查出数据
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # #2.删除
    # db.session.delete(article1)
    # #3.事务提交
    # db.session.commit()

    # article = Article(title='aaa',content='bbb')
    # article.author = User.query.filter(User.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    article = Article.query.filter(Article.title == 'aaa').first()
    print ('username:%s'%article.author.username)

    return 'index'

if __name__ == '__main__':
    app.run()









# import pymysql  # 导入 pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host="localhost", user="root",
#                      password="", db="test", port=3306)
#
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
#
# # 1.查询操作
# # 编写sql 查询语句  login 对应我的表名
# sql = "select * from login"

# cur.execute(sql)
#
# for i in cur.fetchall():
#     print(i)
# print('查询到：',cur.rowcount,'条数据')

#查
# try:
#     cur.execute(sql)  # 执行sql语句
#
#     results = cur.fetchall()  # 获取查询的所有记录
#     print("id", "name", "password")
#     # 遍历结果
#     for row in results:
#         id = row[0]
#         name = row[1]
#         password = row[2]
#         print(id, name, password)
# except Exception as e:
#     raise e
# finally:
#     db.close()  # 关闭连接

#增
# sql_insert = """insert into login(id,username,password) values(4,'liu','1234')"""
#
# try:
#     cur.execute(sql_insert)
#     # 提交
#     db.commit()
# except Exception as e:
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()

#删
# sql_delete = "delete from login where id = %d"
#
# try:
#     cur.execute(sql_delete % (4))  # 像sql语句传递参数
#     # 提交
#     db.commit()
# except Exception as e:
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()

#改
# sql_update = "update login set username = '%s' where id = %d"
#
# try:
#     cur.execute(sql_update % ("xiongda", 3))  # 像sql语句传递参数
#     # 提交
#     db.commit()
# except Exception as e:
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()
