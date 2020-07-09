from flask import Blueprint

bp = Blueprint('bp', __name__, url_prefix='/store')

from . import (routes, user,cart, orders,
               categories, products)
