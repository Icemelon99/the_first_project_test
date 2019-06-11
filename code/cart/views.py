from . import app_cart
from flask import render_template, make_response, redirect

@app_cart.route('/get_cart')
def get_cart():
	res = make_response(render_template('cart.html'))
	res.set_cookie('name', 'tom')
	return res
