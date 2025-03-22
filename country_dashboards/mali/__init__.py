from flask import Blueprint

# Define the blueprint.
mali_bp = Blueprint('mali', __name__, template_folder='templates', static_folder='static')

# Import routes to register them with the blueprint.
from . import routes