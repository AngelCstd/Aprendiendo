#Un archivo es un contenedor de informacion y tienen su propia extension, un archivo exe son hojas de calculo y txt es texto
#Primero debemos abrir el archivo con la funcion open, pero esta funcion nos retorna algo, entonces lo guardamos en una variable

#El encoding es solo para marcar la codificacion en la que esta, no es obligatorio pero te ahorra problemas
archivo = open("Aprendiendo python\\archivos\\texto.txt", encoding="UTF-8")
print(type(archivo)) #<class '_io.TextIOWrapper'>
print(dir(archivo)) #['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
#-----------------------------------------------------------------------------
#Ahora para poder leer el archivo usaremos el metodo read que es el que podemos ver que se encuentra cuando le mandamos al dir

#archivo = archivo.read()
#print(archivo)

#Cuando se lee un archivoo una vez ya no se puede volver a leer, tienes que volver a abrirlo, por eso comentamos el codigo anterior
#De esta forma podemos obtener una lista de cada una de las lineas del archivo
lineas = archivo.readlines()
#Igual se puede leer una sola linea con el metodo readLine(1)
print(lineas)

#Una vez que leimos el archivo se debe cerrar y ya no va a permitir leerlo, si lo quieres leer nuevamente debes volverlo a abrir
#Es importante cerrarlo o se puede perder informacion
archivo.close()
#-------------------------------------------------------------------
#Pero es pesado estar abriendo y cerrando un archivo, para esto python nos trae el with open que funciona como un if else, en caso de que el archivo se abra correctamente entonces podremos ejecutar una accion
with open("Aprendiendo python\\archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())
#Gracias a esto no es necesaro cerrarlo
#-------------------------------------------------
#Ahora vamos a escribir en un archivo, para esto necesitamos poner la bandera de 'w' al abrir el archivo para abrirlo con un permiso de escritura
        #Con el permiso de 'w' si no encuentra el archivo lo crea
        #la funcion write reescribe todo el archivo
        #La funcion writelines igual reescribe todo pero podemos mandarle un iterable con varias lineas y las va a escribir
with open("Aprendiendo python\\archivos\\texto.txt",'w', encoding="UTF-8") as archivo:
    archivo.write("Jaja escribiendo con el codigo")
    archivo.writelines(["jajaja", "\nJajajaja en segunda linea"])
