from flask import Blueprint, render_template

mali_bp = Blueprint('mali', __name__)

@mali_bp.route('/')
def index():
    return render_template('mali/index.html', country='Mali', country_code='ML')

@mali_bp.route('/data')
def data():
    # Add logic to fetch and return data for Mali
    return {"data": "Mali data goes here"}