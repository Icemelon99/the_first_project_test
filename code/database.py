from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask'
# 每次请求结束后自动提交，不建议开启
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# 跟踪数据库的修改，自动修改模型类数据
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 显示对应的SQL语句，一般用于调试和跟踪
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)
# 定义模型类，默认以类名作为表名
class User(db.Model):
    __tablename__ = 'tbl_users'
    id = db.Column(db.Integer, primary_key=True) # 整型的主键会设置为自增加
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))
class Role(db.Model):
    __tablename__ = 'tbl_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship('User', backref='role') # 关联模型类名，可以直接 使用Role().users获取到对应实例集，并给关联的模型类(User)中添加了role属性，可以直接使用User().role获取对应模型类实例，即封装了使用外键查询Role实例的这个步骤
    

if __name__ == '__main__':
    db.drop_all() # 清除当前数据库中所有表
    db.create_all() # 创建所有表
    role1 = Role(name='admin') # 创建对象，并给表中添加数据，自增的主键无须操作
    role2 = Role(name='stuff')
    db.session.add(role1) # 会话记录对象任务
    db.session.add(role2)
    db.session.commit() # 提交到数据库中
    us1 = User(name='wang',email='wang@163.com',password='123456',role_id=role1.id)
    us2 = User(name='zhang',email='zhang@189.com',password='201512',role_id=role2.id)
    us3 = User(name='chen',email='chen@126.com',password='987654',role_id=role2.id)
    us4 = User(name='zhou',email='zhou@163.com',password='456789',role_id=role1.id)
    db.session.add_all([us1, us2, us3, us4]) # 会话记录对象任务列表
    db.session.commit() # 提交到数据库中