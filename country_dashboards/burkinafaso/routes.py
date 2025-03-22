from flask import render_template
from . import burkinafaso_bp

@burkinafaso_bp.route("/")
def detail():
    return render_template("detail.html", country="Burkina Faso", country_code="BF")