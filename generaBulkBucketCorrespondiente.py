#Programado para la versión python3
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Ruta de archivo a procesar")
#parser.add_argument("-n", "--name", help="Nombre de archivo de salida")
args = parser.parse_args()
 
#if args.name is None: or args.file is None :
if args.file is None :
    print ("faltan parametros; tecleé --help o -h para ver las opciones")
    exit()
if args.file:
    # Abre archivo en modo lectura
    archivoEntrada = open(args.file,'r')
    # inicia bucle infinito para leer línea a línea
    while True: 
        linea = archivoEntrada.readline()  # lee línea
        if not linea: 
            break  # Si no hay más se rompe bucle
        metadata = json.loads(linea)
        tp = str(metadata["tp"])
        create =  "{\"create\":{\"_index\":\"firdig_%s\",\"_type\":\"firdig\"}}" % (tp.lower())
        print (create)
        print(metadata)  # Muestra la línea leída
    archivoEntrada.close  # Cierra archivoEntrada

