from flask_script import Manager
from  demo_multi import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import comment_tag,Comment,Tag

manager = Manager(app)

#绑定app,db
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


# @manager.command
# def runserver():
#     print('服务器跑起来了')


if __name__ == '__main__':
    manager.run()