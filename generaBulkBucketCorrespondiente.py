#Programado para la versión python3
import argparse
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(
    ['localhost'],
    port=9200
)

print(es)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Ruta de archivo a procesar")
#parser.add_argument("-n", "--name", help="Nombre de archivo de salida")
args = parser.parse_args()
 
#if args.name is None: or args.file is None :
if args.file is None :
    print ("faltan parametros; --help o -h para ver las opciones")
    exit()
if args.file:
    
    def getDataBulk():
        # Abre archivo en modo lectura
        archivoEntrada = open(args.file,'r')
        # inicia bucle infinito para leer línea a línea
        while True: 
            linea = archivoEntrada.readline()  # lee línea
            if not linea: 
                break  # Si no hay más se rompe bucle
            metadata = json.loads(linea)
            tp = str(metadata["tp"])
            # create =  "{\"create\":{\"_index\":\"firdig_%s\",\"_type\":\"firdig\"}}" % (tp.lower())
            yield {
                    "_index"  : "firdig_%s" % (tp.lower()),
                    "_type"   : "firdig",
                    "_source" : metadata
            }
            archivoEntrada.close  # Cierra archivoEntrada   

    # mycont = getDataBulk()

    # for i in mycont:
    #     print(i)
    helpers.bulk(es, getDataBulk())
    
