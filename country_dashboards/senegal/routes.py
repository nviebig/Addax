from flask import render_template
from . import senegal_bp

@senegal_bp.route("/")
def detail():
    return render_template("senegal/detail.html", country="Senegal", country_code="SN")