from flask import Flask, current_app, redirect, url_for, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
	file = request.files.get('file')
	img = request.files.get('img')
	text = request.form.get('textarea')
	file.save('./2.jpg')
	with open('./1.jpg', 'wb') as i:
		img = img.read()
		i.write(img)
	print(text)
	return 'OK{}'.format(text)

@app.route('/index')
def index():
	a = request.form.get('a')
	b = request.args.get('a')
	return 'the {}'.format(b)


if __name__ == '__main__':
	app.run(debug=True)