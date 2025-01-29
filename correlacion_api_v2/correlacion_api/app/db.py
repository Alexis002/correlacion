import MySQLdb
from config import settings

# Función para obtener la conexión a la base de datos
def get_db_connection():
    return MySQLdb.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWORD,
        db=settings.MYSQL_DB
    )
