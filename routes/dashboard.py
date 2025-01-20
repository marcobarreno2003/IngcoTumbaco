from flask import Blueprint, render_template, session, redirect, url_for, request, flash
import os
from werkzeug.utils import secure_filename
from upload_excel_handler import cargar_datos_excel  # Importar la función para procesar Excel


# Crear el blueprint para el dashboard
dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")

# Ruta principal del dashboard
@dashboard_blueprint.route("/")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login.login"))
    return render_template("dashboard.html", usuario=session["usuario"])

# Ruta para mostrar el formulario de subir Excel
@dashboard_blueprint.route("/upload_excel_form", methods=["GET"])
def upload_excel_form():
    if "usuario" not in session:
        return redirect(url_for("login.login"))
    return render_template("upload_excel.html")

# Ruta para procesar el archivo Excel
@dashboard_blueprint.route("/upload_excel", methods=["POST"])
def upload_excel():
    if "usuario" not in session:
        return redirect(url_for("login.login"))

    if "excelFile" not in request.files:
        flash("No se seleccionó ningún archivo.", "danger")
        return redirect(url_for("dashboard.upload_excel_form"))

    excel_file = request.files["excelFile"]
    if excel_file.filename == "":
        flash("El archivo no tiene nombre.", "danger")
        return redirect(url_for("dashboard.upload_excel_form"))

    try:
        # Guardar el archivo de forma segura
        filename = secure_filename(excel_file.filename)
        filepath = os.path.join("uploads", filename)
        os.makedirs("uploads", exist_ok=True)  # Crear carpeta si no existe
        excel_file.save(filepath)

        # Llamar a la función para cargar los datos en la base de datos
        cargar_datos_excel(filepath)

        flash("Archivo subido y procesado con éxito. Los datos han sido insertados en la base de datos.", "success")
    except Exception as e:
        flash(f"Hubo un error al procesar el archivo: {e}", "danger")

    return redirect(url_for("dashboard.upload_excel_form"))
