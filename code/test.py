from flask import Flask, request, url_for, render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
app = Flask(__name__)
app.config['SECRET_KEY']='WERJ9EGJFKGMSKM29R454TSDFSF'
class RegisterForm(FlaskForm):
	user_name = StringField(label='username', validators=[DataRequired('用户名密码不能为空')])
	password = PasswordField(label='password', validators=[DataRequired('密码不能为空')])
	password2 = PasswordField(label='password2', validators=[DataRequired('密码不能为空'), EqualTo('password', 'not equal')])
	submit = SubmitField(label='submit')

@app.route('/register', methods=['POST', 'GET'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user_name = form.user_name.data
		password = form.password.data
		print('some database work')
		session['user_name'] = user_name
		return redirect(url_for('index'))
	return render_template('register.html', form=form)

@app.route('/index')
def index():
	user_name = session.get('user_name', 'null')
	return 'index page hello {}'.format(user_name)

@app.route('/')
def main_page():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)