import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from database.db_connection import get_connection

# Función para insertar un usuario en la tabla
def insertar_usuario(usuario, contrasena):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = sql.SQL("INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)")
        cursor.execute(query, (usuario, contrasena))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"Error al insertar usuario: {e}")
        return False

# Función para autenticar un usuario
def autenticar_usuario(usuario, contrasena):
    try:
        connection = get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        query = sql.SQL("SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s")
        cursor.execute(query, (usuario, contrasena))
        resultado = cursor.fetchone()
        cursor.close()
        connection.close()
        return resultado is not None
    except Exception as e:
        print(f"Error al autenticar usuario: {e}")
        return False
