from flask import Blueprint

burkinafaso_bp = Blueprint('burkinafaso', __name__, template_folder='templates', static_folder='static')
from . import routes