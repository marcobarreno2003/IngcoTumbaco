from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from database.db_connection import get_connection

# Crear un Blueprint para login
login_blueprint = Blueprint("login", __name__, template_folder="templates")

# Ruta para mostrar el formulario de login
@login_blueprint.route("", methods=["GET", "POST"])  # Ruta raíz del blueprint
def login():
    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["contrasena"]

        connection = None
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para buscar el usuario
            query = "SELECT contrasena FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result and check_password_hash(result[0], password):
                # Si las credenciales son válidas, iniciar sesión
                session["usuario"] = username
                flash("Inicio de sesión exitoso.", "success")
                return redirect(url_for("dashboard.dashboard"))
            else:
                flash("Usuario o contraseña incorrectos.", "danger")

        except Exception as e:
            flash(f"Error al procesar el inicio de sesión: {e}", "danger")
        finally:
            if connection:
                cursor.close()
                connection.close()

    return render_template("login.html")


