import psycopg2

# Configuración de la base de datos
db_config = {
    'host': '34.174.129.109',
    'dbname': 'dbr6uzy0wodm0t',
    'user': 'ughay44kqfx5w',
    'password': '8&C%6(M^uib4',
}

# Función para realizar la consulta
def consultar_reparaciones():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # Consulta SQL para obtener los datos de la tabla
        query = "SELECT * FROM reparaciones;"
        cursor.execute(query)

        # Recuperar todas las filas
        rows = cursor.fetchall()

        # Imprimir los datos
        print("Datos en la tabla 'reparaciones':")
        for row in rows:
            print(row)

    except psycopg2.Error as e:
        print(f"Error al realizar la consulta: {e}")

    finally:
        # Cerrar conexión
        if connection:
            cursor.close()
            connection.close()

# Ejecutar la función
if __name__ == "__main__":
    consultar_reparaciones()
