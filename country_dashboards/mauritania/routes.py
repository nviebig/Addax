from flask import render_template
from . import mauritania_bp

@mauritania_bp.route("/")
def detail():
    return render_template("detail.html", country="Mauritania")
