import psycopg2

# Configuración de la base de datos
db_config = {
    'host': '34.174.129.109',  # Cambia al host correcto
    'dbname': 'dbr6uzy0wodm0t',  # Nombre de tu base de datos
    'user': 'ughay44kqfx5w',  # Usuario de la base de datos
    'password': '8&C%6(M^uib4',  # Contraseña
}

# Función para obtener la conexión
def get_connection():
    try:
        connection = psycopg2.connect(**db_config)
        return connection
    except psycopg2.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
