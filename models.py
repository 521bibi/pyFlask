from exts import db

comment_tag = db.Table('comment_tag',
    db.Column('comment_id',db.Integer,db.ForeignKey('comment.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)

    tags = db.relationship('Tag',secondary=comment_tag,backref=db.backref('comments'))

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
