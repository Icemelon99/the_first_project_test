from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(import_name=__name__,
			static_url_path='/static',
			static_folder='static',
			template_folder='templates')
# 自定义转换器使用正则表达式
class RegexConverter(BaseConverter):
	def __init__(self, url_map, regex):
		super(RegexConverter, self).__init__(url_map)
		self.regex = regex
	def to_python(self, value):
		return value
	def to_url(self, value):
		return value

app.url_map.converters['re'] = RegexConverter

@app.route('/index/<re(r"1[34578]{1}[0-9]{9}"):mobile_num>')
def mobile(mobile_num):
	return 'Send message to {}'.format(mobile_num)

@app.route('/post')
def post():
	url = url_for('mobile', mobile_num='15112345678')
	return redirect(url)

@app.route('/goods/<int:goods_id>')
def goods(goods_id):
	return 'The goods_id is {}'.format(goods_id)


# 使用配置文件
# app.config.from_pyfile('config.cfg')
class Config:
	DEBUG = True
app.config.from_object(Config)


if __name__ == '__main__':
	print(app.url_map)
	app.run(host='0.0.0.0', port=5000)