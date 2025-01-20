from flask import Blueprint, render_template

# Crear el Blueprint para "Administrar Reparaciones"
repairs_blueprint = Blueprint("repairs", __name__, template_folder="templates")

@repairs_blueprint.route("/repairs/manage")
def manage():
    return render_template("repairs.html")
