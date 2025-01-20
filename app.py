from flask import Flask, render_template
from routes.login import login_blueprint
from routes.dashboard import dashboard_blueprint
from routes.warranty import warranty_blueprint
from routes.repairs import repairs_blueprint

app = Flask(__name__)
app.secret_key = "una_clave_segura"

# Registrar Blueprints
app.register_blueprint(login_blueprint, url_prefix="/login")
app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")  # Dashboard en /dashboard
app.register_blueprint(warranty_blueprint, url_prefix="/warranty")
app.register_blueprint(repairs_blueprint, url_prefix="/repairs")

@app.route("/")
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)
