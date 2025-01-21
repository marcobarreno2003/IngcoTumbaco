from flask import Blueprint, render_template, request, flash
from database.db_connection import get_connection

# Crear el Blueprint para "Comprobar Garantía"
warranty_blueprint = Blueprint("warranty", __name__, template_folder="templates")

@warranty_blueprint.route("/warranty/check", methods=["GET", "POST"])
def check():
    results = None  # Variable para almacenar los resultados de la consulta

    if request.method == "POST":
        search_type = request.form.get("search_type")
        search_value = request.form.get("search_value")

        if not search_type or not search_value:
            flash("Por favor, completa todos los campos.", "danger")
            return render_template("warranty.html", results=results)

        try:
            # Conectar a la base de datos
            connection = get_connection()
            cursor = connection.cursor()

            # Definir la consulta SQL en base al tipo de búsqueda
            query = ""
            if search_type == "ruc":
                query = """
                SELECT ruc, razon_social, codigo_producto, descripcion_producto, factura, 
                       fecha_emision_factura, fin_garantia, dias_vencimiento, notas 
                FROM reparaciones 
                WHERE ruc = %s
                """
            elif search_type == "codigo_producto":
                query = """
                SELECT ruc, razon_social, codigo_producto, descripcion_producto, factura, 
                       fecha_emision_factura, fin_garantia, dias_vencimiento, notas 
                FROM reparaciones 
                WHERE codigo_producto = %s
                """
            elif search_type == "numero_serie":
                query = """
                SELECT ruc, razon_social, codigo_producto, descripcion_producto, factura, 
                       fecha_emision_factura, fin_garantia, dias_vencimiento, notas 
                FROM reparaciones 
                WHERE notas LIKE %s
                """
                # Buscar de forma parcial
                search_value = f"%{search_value}%"
            elif search_type == "factura":
                query = """
                SELECT ruc, razon_social, codigo_producto, descripcion_producto, factura, 
                       fecha_emision_factura, fin_garantia, dias_vencimiento, notas 
                FROM reparaciones 
                WHERE factura = %s
                """

            # Ejecutar la consulta
            cursor.execute(query, (search_value,))
            results = cursor.fetchall()

            if not results:
                flash("No se encontraron resultados para la búsqueda.", "warning")

        except Exception as e:
            flash(f"Hubo un error al buscar: {e}", "danger")
        finally:
            if connection:
                cursor.close()
                connection.close()

    return render_template("warranty.html", results=results)

