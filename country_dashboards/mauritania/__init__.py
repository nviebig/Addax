from flask import Blueprint

mauritania_bp = Blueprint('mauritania', __name__, template_folder='templates')

from . import routes