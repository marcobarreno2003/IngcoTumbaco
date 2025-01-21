from flask import Blueprint, render_template, request, flash, redirect, url_for
from database.db_connection import get_connection

# Crear el Blueprint para "Administrar Reparaciones"
repairs_blueprint = Blueprint("repairs", __name__, template_folder="templates")

# Ruta principal del menú de reparaciones
@repairs_blueprint.route("/repairs", methods=["GET"])
def menu():
    return render_template("repairs_menu.html")

# Ruta para añadir reparaciones
@repairs_blueprint.route("/repairs/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            ruc_ci = request.form.get("ruc_ci")
            nombre_cliente = request.form.get("nombre_cliente")
            telefono = request.form.get("telefono")
            codigo_maquina = request.form.get("codigo_maquina")
            nombre_maquina = request.form.get("nombre_maquina")
            numero_serie = request.form.get("numero_serie")
            accesorios = request.form.get("accesorios")
            fecha_recepcion = request.form.get("fecha_recepcion")
            abono = request.form.get("abono")

            # Validar que los campos obligatorios no estén vacíos
            if not all([ruc_ci, nombre_cliente, telefono, codigo_maquina, nombre_maquina, fecha_recepcion]):
                flash("Por favor, completa todos los campos obligatorios.", "danger")
                return redirect(url_for("repairs.add"))

            # Conexión a la base de datos
            connection = get_connection()
            cursor = connection.cursor()

            # Insertar los datos en la tabla
            query = """
            INSERT INTO ordenes_reparacion (ruc_ci, nombre_cliente, telefono, codigo_maquina, nombre_maquina, numero_serie, accesorios, fecha_recepcion, abono)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (ruc_ci, nombre_cliente, telefono, codigo_maquina, nombre_maquina, numero_serie, accesorios, fecha_recepcion, abono))
            connection.commit()

            flash("¡Orden de reparación registrada exitosamente!", "success")
        except Exception as e:
            flash(f"Hubo un error al registrar la orden de reparación: {e}", "danger")
        finally:
            if connection:
                cursor.close()
                connection.close()

    return render_template("add_repair.html")

# Ruta para consultar reparaciones
@repairs_blueprint.route("/repairs/consult", methods=["GET", "POST"])
def consult():
    results = None
    if request.method == "POST":
        try:
            search_query = request.form.get("search_query")
            if not search_query:
                flash("Por favor, ingresa un valor de búsqueda.", "danger")
                return redirect(url_for("repairs.consult"))

            # Conexión a la base de datos
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta SQL para buscar en cualquier campo
            query = """
            SELECT * FROM ordenes_reparacion
            WHERE ruc_ci ILIKE %s OR
                  nombre_cliente ILIKE %s OR
                  telefono ILIKE %s OR
                  codigo_maquina ILIKE %s OR
                  nombre_maquina ILIKE %s OR
                  numero_serie ILIKE %s;
            """
            cursor.execute(query, tuple(f"%{search_query}%" for _ in range(6)))
            results = cursor.fetchall()

            if not results:
                flash("No se encontraron resultados para la búsqueda.", "warning")
        except Exception as e:
            flash(f"Hubo un error al consultar las reparaciones: {e}", "danger")
        finally:
            if connection:
                cursor.close()
                connection.close()

    return render_template("consult_repair.html", results=results)
