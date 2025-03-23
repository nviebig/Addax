from flask import render_template
from . import chad_bp

@chad_bp.route("/")
def detail():
    return render_template("chad/detail.html", country="Chad", country_code="TD")
