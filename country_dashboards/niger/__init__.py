from flask import Blueprint

# Define the blueprint.
niger_bp = Blueprint('niger', __name__, template_folder='templates', static_folder='static')

# Import routes to register them with the blueprint.
from . import routes