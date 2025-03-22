from flask import render_template
from . import niger_bp

@niger_bp.route("/")
def detail():
    return render_template("niger/detail.html", country="Niger", country_code="NE")