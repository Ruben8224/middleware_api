from fastapi import APIRouter, Depends
from sqlalchemy.sql import text
from fastapi.responses import FileResponse
import os
from .db import SessionLocal
from .tasks import generar_reporte_campania
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

# Dependency para manejar la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener las campañas de acuerdo a la fecha y generar el reporte
@router.get("/reporte")
def reporte(fecha: str, db: SessionLocal = Depends(get_db)):
    try:
        result = db.execute(
            text("CALL GetCampaniasPorFecha(:fecha)"),
            {"fecha": fecha}
        ).mappings().all()

        for campania in result:
            generar_reporte_campania.delay(
                campania['id'],
                campania['nombre_campania'],
                fecha
            )

        return {"mensaje": f"{len(result)} campañas enviadas a la cola"}
    except SQLAlchemyError as e:
        return {"error": str(e)}

# Ruta para obtener las campañas disponibles
@router.get("/campanias")
def obtener_campanias(db: SessionLocal = Depends(get_db)):
    try:
        result = db.execute(
            text("SELECT * FROM TA_SMS_MAESTRO")
        ).mappings().all()
        return result
    except SQLAlchemyError as e:
        return {"error": str(e)}

# Ruta para obtener detalles de una campaña en particular
@router.get("/detalles/{id_maestro}")
def obtener_detalles(id_maestro: int, db: SessionLocal = Depends(get_db)):
    try:
        result = db.execute(
            text("""
                SELECT * FROM TA_SMS_DETALLE
                WHERE id_maestro = :id
                LIMIT 100
            """),
            {"id": id_maestro}
        ).mappings().all()
        return result
    except SQLAlchemyError as e:
        return {"error": str(e)}

# Ruta para consultar las campañas basadas en fecha
@router.get("/paso/consultar-campania")
def consultar_campania(fecha: str, db: SessionLocal = Depends(get_db)):
    try:
        result = db.execute(
            text("CALL GetCampaniasPorFecha(:fecha)"),
            {"fecha": fecha}
        ).mappings().all()
        return result
    except SQLAlchemyError as e:
        return {"error": str(e)}

# Ruta para generar la paginación de detalles
@router.get("/paso/generar-paginacion")
def generar_paginacion(id: int, db: SessionLocal = Depends(get_db)):
    try:
        offset = 0
        limit = 10000
        total = 0
        while True:
            result = db.execute(
                text("CALL GetDetallesPorCampania(:id, :offset, :limit)"),
                {"id": id, "offset": offset, "limit": limit}
            ).fetchall()
            if not result:
                break
            total += len(result)
            offset += limit
        return {"total_registros": total}
    except SQLAlchemyError as e:
        return {"error": str(e)}

# Ruta para crear un archivo vacío
@router.get("/paso/crear-archivo")
def crear_archivo(nombre: str, fecha: str):
    ruta = f"./reportes/{nombre}_{fecha}.csv"
    os.makedirs("./reportes", exist_ok=True)
    with open(ruta, "w") as f:
        f.write("Archivo creado sin datos aún\n")
    return {"archivo": ruta}

# Ruta para escribir las cabeceras en el archivo
@router.get("/paso/escribir-cabeceras")
def escribir_cabeceras(nombre: str, fecha: str):
    ruta = f"./reportes/{nombre}_{fecha}.csv"
    headers = ["id", "id_maestro", "telefono", "mensaje"]
    with open(ruta, "w") as f:
        f.write(",".join(headers) + "\n")
    return {"archivo": ruta}

# Ruta para descargar los archivos por fecha
@router.get("/descargar/por-fecha/{fecha}")
def descargar_por_fecha(fecha: str):
    carpeta = "reportes"

    archivos = [f for f in os.listdir(carpeta) if fecha in f]

    if not archivos:
        return {"error": "No hay archivos para esta fecha"}

    archivos.sort(reverse=True)
    archivo_mas_reciente = archivos[0]

    return FileResponse(
        path=os.path.join(carpeta, archivo_mas_reciente),
        filename=archivo_mas_reciente,
        media_type='text/csv'
    )
