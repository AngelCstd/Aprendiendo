#Esto nos permite ver todos los metodos que existen dependiendo del tpo de dato que le mandemos igual como las listas
#print(dir(5))
#print(dir("hola"))

############################################### METODOS DE CADENAS
texto = "hola bros"
texto.upper() #Convierte a mayusculas
texto.lower() #Convierte a minusculas
texto.capitalize() #Convierte solo la primera a mayuscula

indice = texto.find("b") #Nos devuelve la pocision de las letras donde se encuentra el valor que le mandamos. Si no enceuntra un valor devuelve -1 y se toman en cuenta las mayusculas
indice = texto.index("b") #Esto funciona igual pero en este caso si no encuentra el valor nos manda una excepcion

es_numerico = texto.isnumeric() #Esto nos devuelve un booleano dependiendo si el valor del texto son numeros o no
texto = "567534"
es_numerico = texto.isnumeric() #Esto ya nos devolveria true
es_numerico = texto.isalpha() #Esto es lo mismo pero solo caracteres de la a a la z, espacios no cuentan

texto = "hola mi carnaval"
contarCuantasVecesSeRepite = texto.count("a") #Devuelve cuantas veces se encuentra lo que le mandes, en este caso la letra a
contarCaracteres = len(texto) #Esto nos devuelve el numero de caracteres que contiene

#Remplaza el primer parametros por el segundo en la cadena
cadena_nueva=texto.replace("hola", "adios")
#Nos separa la cadena por el valor que le mandamos como parametro y convertido en una lista
texto = "hola, soy angel, como te llamas?"
cadena_separada = texto.split(",")

############################################### METODOS DE LISTAS
#Aqui se repite el metodo len ya que tiene la misma funcionalidad

lista=["hola, 5, True"]

#Agregando elementos al final de la lista
lista.append("agregando elemento")
#Agregando elementos en un indice especifico de la lista y los demas solamente los empuja un indice
lista.insert(2, "Ahora estoy en el 2")
#Agregando varios valores a una lista, debes agregarlos como una lista y no se agregara como una lista sera como un flat de javascript
lista.extend(["hola", "me agregarn"])
#Eliminando un elemento de la lista segun su indice
lista.pop(0)
#Removiendo un elemento de la lista por su valor
lista.remove('Ahora estoy en el 2')
#Eliminando todos los valores de la lista
#lista.clear()
#Ordenando los valores de una lista (No sirve con las cadenas, solo con numeros y booleanos porque son como 1 y 0 al final, el false es 0 y true es 1)
lista.sort()
#Esto los ordena al reves
lista.sort(reverse=True)
#Esto nos invierte los valores, pueden estar ordenados o no, pero los invierte a como estarian al inicio
lista.reverse()

############################################################################### METODOS DE TUPLAS
#En las tupls solo se pueden buscar elementos y contarlos
tuppla = ("hola", 5, 90)
indice = tuppla.index(5)
contador_de_coincidencias = tuppla.count(5)

############################################################################### METODOS DE DICCIONARIOS
#Recordemos que los diccionarios son como los objetos en javascript
diccionario = {
    "nombre": "angel",
    "edad": 5
}
#Devuelve las llaves (claves o keys) de el elmeento diccionario, nos sirve para iterar ya que nos devuelve las llaves en una lista
llaves = diccionario.keys()
#Devuelve el valor de una clave
valor = diccionario.get("nombre")
#Elimiinando un elemento del diccionario
diccionario.pop("nombre")
#Igual puede eliminar varios
diccionario.pop("nombre", "edad")
#Devuleve un array clave valor de los valores del diccionario
valores_diccionario = diccionario.items()
#Elimina todos los elementos
diccionario.clear()
print(lista)

