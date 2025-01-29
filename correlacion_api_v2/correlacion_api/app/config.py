import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

class Settings:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'nombre_de_la_base_de_datos')

    DEBUG = os.getenv('DEBUG', True)

settings = Settings()
