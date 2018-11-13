from flask import Flask
from exts import db
from models import comment_tag,Comment,Tag
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():

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


if __name__ == '__main__':
    app.run()