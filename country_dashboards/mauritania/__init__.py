from flask import Blueprint

mauritania_bp = Blueprint('mauritania', __name__, template_folder='templates', static_folder='static')

# Import routes so they register with the blueprint.
from . import routes