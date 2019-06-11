from flask import Flask
from cart import app_cart

app = Flask(__name__)
app.register_blueprint(app_cart,
 url_prefix='/cart')


if __name__ == '__main__':
	print(app.url_map)
	app.run(debug=True)
