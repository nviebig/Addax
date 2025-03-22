from flask import render_template
from . import sudan_bp

@sudan_bp.route("/")
def detail():
    return render_template("detail.html", country="Sudan", country_code="SD")