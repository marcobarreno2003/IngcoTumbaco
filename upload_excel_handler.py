import pandas as pd
from database.db_connection import get_connection

def cargar_datos_excel(file_path):
    try:
        # Leer el archivo Excel, saltando filas no deseadas y seleccionando la hoja específica
        data = pd.read_excel(file_path, sheet_name="BASE DE GARANTIAS", skiprows=8)

        # Validar que las columnas esperadas estén presentes
        columnas_esperadas = [
            "RAZON_SOCIAL", "RUC", "TELEFONO", "FACTURA", "CODIGO_PRODUCTO",
            "DESCRIPCION_PRODUCTO", "FECHA EMISION DE FACTURA", "FIN DE GARANTIA",
            "DIAS EN QUE VENCE GARANTIA", "NOTAS"
        ]
        if not all(col in data.columns for col in columnas_esperadas):
            raise ValueError("El archivo Excel no tiene el formato esperado. Verifica los encabezados.")

        # Conexión a la base de datos
        connection = get_connection()
        cursor = connection.cursor()

        # Renombrar columnas para que coincidan con la base de datos
        data.rename(columns={
            "RAZON_SOCIAL": "razon_social",
            "RUC": "ruc",
            "TELEFONO": "telefono",
            "FACTURA": "factura",
            "CODIGO_PRODUCTO": "codigo_producto",
            "DESCRIPCION_PRODUCTO": "descripcion_producto",
            "FECHA EMISION DE FACTURA": "fecha_emision_factura",
            "FIN DE GARANTIA": "fin_garantia",
            "DIAS EN QUE VENCE GARANTIA": "dias_vencimiento",
            "NOTAS": "notas"
        }, inplace=True)

        # Insertar datos en la tabla
        for _, row in data.iterrows():
            cursor.execute("""
                INSERT INTO reparaciones (razon_social, ruc, telefono, factura, codigo_producto,
                descripcion_producto, fecha_emision_factura, fin_garantia, dias_vencimiento, notas)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['razon_social'],
                row['ruc'],
                row['telefono'],
                row['factura'],
                row['codigo_producto'],
                row['descripcion_producto'],
                row['fecha_emision_factura'],
                row['fin_garantia'],
                row['dias_vencimiento'],
                row['notas']
            ))

        # Confirmar cambios
        connection.commit()
        print("Datos cargados exitosamente a la base de datos.")

    except Exception as e:
        print(f"Error al cargar datos desde Excel: {e}")
        raise e
    finally:
        if connection:
            cursor.close()
            connection.close()
