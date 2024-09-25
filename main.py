from PIL import Image, ImageDraw, ImageFont
import datetime

hora_actual = datetime.datetime.now().strftime("%H-%M-%S_%d-%m-%y")

from lib import DosEnUno,leer_archivos_en_directorio

inDir="in/"

inFile=inDir+leer_archivos_en_directorio(inDir)[0]
#inFile="in/in.jpg"


#outDir="out/out.png"

def agregar_texto_a_borde(texto,esq,color="white"):

    imagen_ruta=inFile

    imagen = Image.open(imagen_ruta)
    
    ancho, alto = imagen.size
    
    dibujo = ImageDraw.Draw(imagen)
    
    tamano_fuente = int(alto * 0.05)
    
    try:
        fuente = ImageFont.truetype("arial.ttf", tamano_fuente)
    except IOError:
        fuente = ImageFont.load_default()

    margen = tamano_fuente*2/3

    # Obtener el cuadro delimitador del texto en píxeles (x_min, y_min, x_max, y_max)
    bbox = dibujo.textbbox((0, 0), texto, font=fuente)
    ancho_texto = bbox[2] - bbox[0]  # Ancho del texto
    alto_texto = bbox[3] - bbox[1]   # Alto del texto

    if esq == 0:  #Esquina superior izquierda
        posicion_texto = (margen, margen)
    elif esq == 1:  #Esquina superior derecha
        posicion_texto = (ancho - ancho_texto - margen, margen)
    elif esq == 2:  #Esquina inferior izquierda
        posicion_texto = (margen, alto - tamano_fuente - margen)
    elif esq == 3:  #Esquina inferior derecha
        posicion_texto = (ancho - ancho_texto - margen, alto - tamano_fuente - margen)

    dibujo.text(posicion_texto, texto, font=fuente, fill=color)
    
    imagen.save("out/OUT_"+hora_actual+".png")

formato=0
horaDeCracion=DosEnUno(inDir,formato)
esquina=0
color="white"


eleccion=1
while eleccion!="0":
    if esquina==0:
        esq="Esquina superior izquierda"
    elif esquina==1:
        esq="Esquina superior derecha"
    if esquina==2:
        esq="Esquina inferior izquierda"
    elif esquina==3:
        esq="Esquina inferior derecha"

    print(f"Digite [1] para cambiar la config de esquina    | Config Actual: {esq}")
    print(f"Digite [2] para cambiar la config de color      | Config Actual: {color}")
    print(f"Digite [3] para cambiar el formato de fecha     | Config Actual: {horaDeCracion}")
    print("Digite [9] para exportar foto.")

    eleccion=input("Digite 0 para salir.")

    if eleccion=="1":
        esquina+=1
        if esquina>3:
            esquina=0

    elif eleccion=="2":
        if color=="white":
            color = "yellow"
        elif color== "yellow":
            color ="white"

    elif eleccion=="3":
        formato+=1
        if formato>4:
            formato = 0
        horaDeCracion=DosEnUno(formato)

    if eleccion=="9":
        agregar_texto_a_borde(horaDeCracion,esquina,color)