import sys
import os

# Añadir la ruta del proyecto al sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Establecer la variable de entorno para Flask
os.environ['FLASK_APP'] = 'app.py'

# Importar la aplicación Flask
from app import app as application