import os
import time
from .db import SessionLocal
from app.utils.export_csv import crear_csv
from .worker import celery

@celery.task
def generar_reporte_campania(id_campania, nombre, fecha):
    print(f"Iniciando reporte para campaña: {nombre} (ID: {id_campania})")

    session = SessionLocal()
    offset = 0
    limit = 10000
    pagina = 1
    headers = ["id", "id_maestro", "telefono", "mensaje"]
    datos_totales = []

    os.makedirs("reportes", exist_ok=True)
    nombre_archivo = f"reporte_{id_campania}_{int(time.time())}.csv"
    file_path = os.path.join("reportes", nombre_archivo)

    # 1. Consultar campaña en la base de datos
    print("Consultando campaña en la base de datos...")

    while True:
        # 2. Se genera la paginación
        print(f"Página {pagina} | Offset: {offset}")
        result = session.execute(
            f"CALL GetDetallesPorCampania({id_campania}, {offset}, {limit})"
        ).fetchall()

        if not result:
            print("Fin de la paginación. No hay más datos.")
            break

        datos_totales.extend(result)
        offset += limit
        pagina += 1

    # 3. Crear archivo de reporte con los datos
    print(f"Creando archivo CSV: {file_path}")

    # Escribir encabezados y datos en el archivo CSV
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        # Escribir los encabezados
        f.write(",".join(headers) + "\n")

        # Escribir los datos
        for row in datos_totales:
            f.write(f"{row['id']},{row['id_maestro']},{row['telefono']},{row['mensaje']}\n")

    # 4. Finalizar
    print(f"Reporte generado correctamente: {file_path}")
    session.close()

