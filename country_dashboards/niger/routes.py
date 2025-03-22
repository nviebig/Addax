from flask import render_template
from . import niger_bp

@niger_bp.route("/")
def detail():
    return render_template("detail.html", country="Niger", country_code="NE")