import psycopg2
from psycopg2 import sql

# Configuración de la base de datos
db_config = {
    'host': '34.174.129.109',
    'dbname': 'dbr6uzy0wodm0t',
    'user': 'ughay44kqfx5w',
    'password': '8&C%6(M^uib4',
}

def recrear_tabla_reparaciones():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # SQL para eliminar la tabla si existe
        cursor.execute("DROP TABLE IF EXISTS reparaciones CASCADE;")

        # SQL para crear la tabla con todas las columnas como VARCHAR
        crear_tabla_query = """
        CREATE TABLE reparaciones (
            id SERIAL PRIMARY KEY,
            razon_social VARCHAR(255),
            ruc VARCHAR(50),
            telefono VARCHAR(50),
            factura VARCHAR(50),
            codigo_producto VARCHAR(100),
            descripcion_producto VARCHAR(255),
            fecha_emision_factura VARCHAR(50),
            fin_garantia VARCHAR(50),
            dias_vencimiento VARCHAR(50),
            notas VARCHAR(255)
        );
        """
        cursor.execute(crear_tabla_query)
        connection.commit()
        print("La tabla 'reparaciones' ha sido recreada exitosamente con todas las columnas como VARCHAR.")
    
    except Exception as e:
        print(f"Error al recrear la tabla 'reparaciones': {e}")
    
    finally:
        if connection:
            cursor.close()
            connection.close()

# Ejecutar la función
if __name__ == "__main__":
    recrear_tabla_reparaciones()
