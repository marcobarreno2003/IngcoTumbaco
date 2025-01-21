import psycopg2
from psycopg2 import sql

# Configuración de la base de datos
db_config = {
    'host': '34.174.129.109',
    'dbname': 'dbr6uzy0wodm0t',
    'user': 'ughay44kqfx5w',
    'password': '8&C%6(M^uib4',
}

def recrear_tabla_ordenes_reparacion():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # SQL para eliminar la tabla si existe
        cursor.execute("DROP TABLE IF EXISTS ordenes_reparacion CASCADE;")

        # SQL para crear la nueva tabla con todas las columnas como VARCHAR
        crear_tabla_query = """
        CREATE TABLE ordenes_reparacion (
            id SERIAL PRIMARY KEY,
            ruc_ci VARCHAR(50),
            nombre_cliente VARCHAR(255),
            telefono VARCHAR(50),
            codigo_maquina VARCHAR(100),
            nombre_maquina VARCHAR(255),
            numero_serie VARCHAR(50),
            accesorios TEXT,
            fecha_recepcion VARCHAR(50),
            abono VARCHAR(50)
        );
        """
        cursor.execute(crear_tabla_query)
        connection.commit()
        print("La tabla 'ordenes_reparacion' ha sido recreada exitosamente con todas las columnas como VARCHAR.")
    
    except Exception as e:
        print(f"Error al recrear la tabla 'ordenes_reparacion': {e}")
    
    finally:
        if connection:
            cursor.close()
            connection.close()

# Ejecutar la función
if __name__ == "__main__":
    recrear_tabla_ordenes_reparacion()

