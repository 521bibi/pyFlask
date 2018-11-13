from flask import Flask,session
from exts import db
from models import comment_tag,Comment,Tag
import config
import os
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/')
def index():

    session['username'] = 'bill'
    session.permanent = True
    # comment1 = Comment(title='aaa')
    # comment2 = Comment(title='bbb')
    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')
    #
    # comment1.tags.append(tag1)
    # comment1.tags.append(tag2)
    #
    # comment2.tags.append(tag1)
    # comment2.tags.append(tag2)
    #
    # db.session.add(comment1)
    # db.session.add(comment2)
    #
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    # comment1 = Comment.query.filter(Comment.title == 'aaa').first()
    # tags = comment1.tags
    # for tag in tags:
    #     print(tag.name)

    return 'index'

@app.route('/get/')
def get():
    print(session.get('username'))
    return 'sucess'

if __name__ == '__main__':
    app.run()