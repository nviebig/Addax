from flask import render_template
from . import mali_bp

@mali_bp.route("/")
def detail():
    return render_template("templates/detail.html", country="Mali", country_code="ML")
