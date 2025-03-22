from flask import Flask, render_template
import ee
ee.Initialize()

app = Flask(__name__)

# Global routes.
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

# Import and register country blueprints.
from country_dashboards.mali import mali_bp
from country_dashboards.niger import niger_bp
from country_dashboards.chad import chad_bp
from country_dashboards.burkinafaso import burkinafaso_bp
from country_dashboards.mauritania import mauritania_bp
from country_dashboards.senegal import senegal_bp
from country_dashboards.sudan import sudan_bp

app.register_blueprint(mali_bp, url_prefix='/dashboard/mali')
app.register_blueprint(niger_bp, url_prefix='/dashboard/niger')
app.register_blueprint(chad_bp, url_prefix='/dashboard/chad')
app.register_blueprint(burkinafaso_bp, url_prefix='/dashboard/burkinafaso')
app.register_blueprint(mauritania_bp, url_prefix='/dashboard/mauritania')
app.register_blueprint(senegal_bp, url_prefix='/dashboard/senegal')
app.register_blueprint(sudan_bp, url_prefix='/dashboard/sudan')

if __name__ == '__main__':
    app.run(debug=True)