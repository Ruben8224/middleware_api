import csv
import os

def crear_csv(nombre_archivo, headers, datos):
    ruta_directorio = "reportes_csv"
    os.makedirs(ruta_directorio, exist_ok=True)  # crea carpeta si no existe

    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)

    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(headers)  # escritura de cabeceras

        for fila in datos:
            writer.writerow(fila)

    print(f"Archivo generado en: {ruta_archivo}")
