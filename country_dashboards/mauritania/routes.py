from flask import render_template
from . import mauritania_bp

@mauritania_bp.route("/")
def detail():
    print("Mauritania detail route accessed")  # Debug print in server log
    return render_template("detail.html", country="Mauritania")