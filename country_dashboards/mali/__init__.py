from flask import Blueprint
mali_bp = Blueprint('mali', __name__, template_folder='templates', static_folder='static')
from . import routes