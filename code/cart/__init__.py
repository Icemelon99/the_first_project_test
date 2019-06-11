from flask import Blueprint
app_cart = Blueprint('app_cart', __name__, static_folder='static')
from .views import get_cart

