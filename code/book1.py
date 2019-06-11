from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='WERJ9EGJFKGMSKM29R454TSDFSF'

db = SQLAlchemy(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

class Author(db.Model):
    __tablename__ = 'tbl_authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(64))
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    __tablename__ = 'tbl_books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))

class AuthorBookForm(FlaskForm):
    author_name = StringField(label='author', validators=[DataRequired()])
    book_name = StringField(label='book', validators=[DataRequired()])
    submit = SubmitField(label='save')

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name=book_name, author=author) 通过反引用设置的属性
        db.session.add(book)
        db.session.commit()

    authors = Author.query.all()
    return render_template('index.html', authors=authors, form=form)

@app.route('/delete_book', methods=['POST', 'GET'])
def delete_book():
    book_id = request.get_json().get('book_id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    # 调用ajax
    return jsonify(code=0, message='OK')

if __name__ == '__main__':
    manager.run()