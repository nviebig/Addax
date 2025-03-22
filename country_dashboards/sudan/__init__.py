from flask import Blueprint

# Define the blueprint.
sudan_bp = Blueprint('sudan', __name__, template_folder='templates', static_folder='static')

# Import routes to register them with the blueprint.
from . import routes