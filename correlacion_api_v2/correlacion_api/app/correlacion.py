from fastapi import FastAPI, APIRouter, HTTPException, Request, Response
from db import get_db_connection
import jwt
import time
from fastapi.responses import RedirectResponse


# Clave privada RSA
private_key = """
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
"""

# Función para generar el JWT
def generate_jwt():
    payload = {
        "user": "foobar",
        "sub": "foobar@example.com",
        "iat": int(time.time()),
        "exp": int(time.time()) + 300
    }
    token = jwt.encode(payload, private_key, algorithm='RS256')
    return token

# Lista de dominios permitidos en el Referer
dominios_permitidos = ['*']

# Crear el router para los endpoints de la API
router = APIRouter(prefix="/correlacion/api")

@router.get("/datos")
async def obtener_datos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOMBRE,IP,ESTADO,REGIONAL  FROM equipos WHERE ESTADO = 0")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"nombre": row[0], "fecha_falla": row[1], "estado": row[2],"regional": row[3]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/r4")
async def obtener_regional(regional: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT NOMBRE, ID , CIUDADES, LATITUD, LONGITUD, ESTADO, WAN1,WAN2 "
            "FROM regionales WHERE TIPOGRAFIA = %s", 
            (regional,)
        )
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"nombre": row[0], "IP": row[1], "fechahora_falla": row[2],
                   "Latitud": row[3], "Longitud": row[4],"estado": row[5],"claro": row[6],"ufinet": row[7]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/topologia")
async def obtener_topologia(idEquipo: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query de nodos
        cursor.execute("SELECT CODIGO, NOMBRE, IP, TIPO, ESTADO, FECHA_FALLA FROM equipos WHERE REGIONAL = %s", (idEquipo,))
        nodos = cursor.fetchall()

        # Query de conexiones
        cursor.execute("SELECT Origen, Destino FROM neighbors2 WHERE Interfaz = %s", (idEquipo,))
        conexiones = cursor.fetchall()

        cursor.close()
        conn.close()

        nodos_result = [{"ID": row[0], "Nombre": row[1], "IP": row[2], "Tipo": row[3], "Estado": row[4], "fecha": row[5]} for row in nodos]
        conexiones_result = [{"Origen": row[0], "Destino": row[1]} for row in conexiones]

        return {"nodos": nodos_result, "conexiones": conexiones_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/regionales")
async def obtener_regionales():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOMBRE, CIUDADES, TIPOGRAFIA, LATITUD, LONGITUD, TIPOGRAFIA FROM regionales")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"nombre": row[0], "ciudades": row[1], "tipografia": row[2], "x": row[3], "y": row[4], "codigo": row[5]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get('/oficinas')
async def obtener_oficinas(regional: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "SELECT CODIGO,IP,MAC,TIPO,CLASE,NOMBRE,ESTADO,ALARMAS  FROM equipos  WHERE REGIONAL = %s"
        cursor.execute(sql, (regional,))
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"CODIGO": row[0], "IP": row[1], "MAC": row[2], "TIPO": row[3], 
                   "CLASE": row[4], "NOMBRE": row[5], "ESTADO": row[6], "ALARMAS": row[7]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/equipos")
async def obtener_datos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id ,nombre, mac_address, role, license_type, software_version, status, statusbk FROM Dispositivos")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"id": row[0], "nombre": row[1], "mac": row[2], "tipo": row[3], "licensia": row[4], "version": row[5], "estado": row[6], "ultimobk": row[7]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/total")
async def obtener_datos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Consulta para obtener el total de equipos registrados
        cursor.execute("SELECT COUNT(*) FROM Dispositivos")
        total_equipos = cursor.fetchone()[0]  # Extraer el resultado del conteo

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

        # Retornar el total de equipos como un diccionario
        return {"total_equipos": total_equipos}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   



@router.get("/ultima_fecha")
async def obtener_ultima_fecha():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Consulta para obtener la última fecha y hora del último registro
        cursor.execute("SELECT MAX(date) FROM backups")  # Asegúrate de que esta columna exista
        ultima_fecha = cursor.fetchone()[0]  # Extraer el resultado

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

        # Retornar la última fecha como un diccionario
        return {"ultima_fecha": ultima_fecha if ultima_fecha else None}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/detalle/{dispositivo_id}")
async def obtener_detalle(dispositivo_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Consulta que une ambas tablas usando el campo `id` de `backups` y `Dispositivos`
        cursor.execute("""
            SELECT d.nombre, d.mac_address, d.role, d.license_type, d.software_version, d.status, d.statusbk, d.imagen, b.date, b.backup
            FROM Dispositivos d
            LEFT JOIN backups b ON d.id = b.id
            WHERE d.id = %s
            ORDER BY b.date DESC
            LIMIT 1
        """, (dispositivo_id,))
        
        resultado = cursor.fetchone()

        # Cerrar conexión
        cursor.close()
        conn.close()

        if resultado:
            # Estructura del resultado
            detalle = {
                "nombre": resultado[0],
                "mac": resultado[1],
                "tipo": resultado[2],
                "licensia": resultado[3],
                "version": resultado[4],
                "estado": resultado[5],
                "statusbk": resultado[6],
                "imagen": resultado[7],
                "fecha_backup": resultado[8],
                "backup": resultado[9]
            }
            return detalle
        else:
            raise HTTPException(status_code=404, detail="Dispositivo o backup no encontrado")
           
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
@router.get("/get-token")
async def get_token(grafana_url: str = None):
    if not grafana_url:
        raise HTTPException(status_code=400, detail="No se proporcionó la URL de Grafana")
    token = generate_jwt()
    return {"token": token, "grafana_url": grafana_url}

@router.get("/render-grafana")
async def render_grafana(request: Request, auth_token: str = None, grafana_url: str = None):
    referer = request.headers.get('Referer')
    if not referer or not any(referer.startswith(dominio) for dominio in dominios_permitidos):
        raise HTTPException(status_code=403, detail="Acceso no autorizado")

    if not grafana_url:
        raise HTTPException(status_code=400, detail="No se proporcionó la URL de Grafana")

    return RedirectResponse(url=f"{grafana_url}&auth_token={auth_token}") 

@router.get("/troubleshooting")
async def obtener_datos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id,ip_wan,nombre_mostrar,pe,proyecto,vrf  FROM troubleshooting")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"id": row[0], "ip_wan": row[1], "nombre_mostrar": row[2],"pe": row[3],"proyecto": row[4],"vrf": row[5]} for row in datos]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
       