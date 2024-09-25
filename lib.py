import os
import time
import datetime

def leer_archivos_en_directorio(direccion):
    archivos = os.listdir(direccion)
    
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(direccion, archivo))]
    
    return archivos
"""
def obtener_fecha_creacion(ruta_archivo):

    fecha_creacion = os.path.getctime(ruta_archivo)
    
    fecha_datetime = datetime.datetime.fromtimestamp(fecha_creacion)

    fecha_formateada = fecha_datetime.strftime("%H:%M:%S %d/%m/%Y")

    return fecha_formateada
"""

def obtener_fecha_modificacion(ruta_archivo,formato):

    fecha_modificacion = os.path.getmtime(ruta_archivo)
    
    fecha_datetime = datetime.datetime.fromtimestamp(fecha_modificacion)

    #fecha_formateada = fecha_datetime.strftime("%H:%M:%S %d/%m/%Y")
    if formato==0:
        fecha_formateada = fecha_datetime.strftime("%d/%m/%Y")
    elif formato==1:
        fecha_formateada = fecha_datetime.strftime("%d/%m/%Y %H:%M")
    elif formato==2:
        fecha_formateada = fecha_datetime.strftime("%d/%m/%Y %H:%M:%S")
    elif formato==3:
        fecha_formateada = fecha_datetime.strftime("%d/%m/%y")
    elif formato==4:
        fecha_formateada = ""

    return fecha_formateada

def DosEnUno(direccionIn,formato=0,):
    archivos = leer_archivos_en_directorio(direccionIn)

    ruta_archivo = direccionIn+archivos[0]

    return obtener_fecha_modificacion(ruta_archivo,formato)