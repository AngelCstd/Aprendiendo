#Para poder trabajar con estoss archivos debemos abrir el archivo de nuev pero utilizaremos la libreria csv
import csv
with open("Aprendiendo python\\archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo) #Esto nos devuelve un objeto csv reader, que en realidad es una lista, entonces podemos iterar
    for row in reader:
        print(row) #Esto nos va a pintar fila por fila
#Hay una libreria llamada pandas que nos ayuda a manejar esto de formas mas faciles, escribi un modulo de eso