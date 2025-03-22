from flask import render_template
from . import mauritania_bp

@mauritania_bp.route("/")
def detail():
    print("Mauritania detail route accessed")
    return render_template("mauritania/detail.html")