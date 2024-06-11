#TIPOS DE DATOS
#   #STRING TEXTO
'texto'
'''texto
de varias lineas''' 
#   #ENTERO INT
4 
#   #FLOAT DECIMAL
4.4 
#   #BOOLEAN
True, False 
#   #CONCATENAR CONN F STRING COMO BACKTIPS EN JAVASCRIPT
nombre = "wen"
saludo = f"hola {nombre}"
#   #PARA ELIMINAR VARIABLES
del nombre
#DATOS COMPUESTOS
#   #LISTA
    #Es un array
lista = ["hola", 4, True] 
lista[0] = "carnal" 

#   #TUPLAS
tupla = ("hoola", 5, False)
    #Esto no se puede ya que las tuplas no pueden modificarse
#tupla[0] = "carnal" 

##CONJUNTO
    #Este tipo de dato no lleva un orden y tampoco se puede moodificar un elemento directo ya que no lleva un orden o un indice al cual acceder, estos datos estan desordenados
    #Este dato es como un objeto en javascript pero sin las llaves (keys)
    #Tambien este tipo de dato no permite elementos duplicados
conjunto = {"holabro", 5, True}
    #sin embargo si puedes sobreescribir el conjunto aun si no puedes modificar sus valores
conjunto = {"hola brother", 10, False}
    #Aqui podemos ver que no se puede acceder al valor con el indice
########print(conjunto[0])

#DICCIONARIO
    #Es un objeto de javascript
diccionario = {
    'nombre': "angelon",
    'edad': 23
}
    #Asi accedes a el
print(diccionario['nombre'])

#------------------------------------------------------------------------------
#Desempaquetado
#De esta manera podemos obtener los valores de un dato complejo (lista o tupla o conjunto), algo parecido a como hacemos la destructuracion en javascript
datos = ("angel", "lucas", 15)
nombre, amigo, partidos_jugados = datos
print(nombre) #angel
print(amigo) #lucas
print(partidos_jugados) #15
#-----------------------------------------------------------------------------
#CONJUNTOS
#Teoria de conjuntos
conjunto1={1,3,5,7}
conjunto2 = {1,3,7}
#Aqui podemos ver que si tomamos a 2 como conjunto entonces 1 es un superconjunto de 2, en caso de que tomemos 1 como conjunto entonces 2 es un subconjunto de 1
#Este metodo nos permite saber si el conjunto 2 es un subconjunto de 1 con booleano
resultado = conjunto2.issubset(conjunto1)
#Igual podemos ponerlo como <= o >= si es un superconjunto
resultado = conjunto2 <= conjunto1 #Sub conjunto
resultado = conjunto2 >= conjunto1 #Super conjunto
#Para saber si hay un resultado que NO concuerde entre dos conjuntos (o sets) entonces usamos 
resultado = conjunto2.isdisjoint(conjunto1)
#-------------------------------------------------------------------------------
#DICCIONARIOS
#Podemos crearlos como un json de javascript o con la funcion dict
diccionario = dict(nombre = "angel", edad = 15)
diccionario = {
    "nombre":"angel",
    "edad":15
}
#Esto nos permite crear un diccionario con todos los valores none
diccionario = dict.fromkeys(["nombre", "apellido","suscriptores"])
#---------------------------------------------------------------------
#Slicing
#Esta es una tecnica para cortar partes de un array o tupla, etc, se usa mandando a llamar un indice pero definido con :, asi podemos ver desde que numero inicia y hasta que numero termina (Sin tomar en cuenta ese numero)
print(lista) #['carnal', 4, True]
print(lista[:2]) #['carnal', 4]
print(lista[1:]) #[4, True]
print(lista[1:2]) #[4]
print(lista[1:-1]) #[4]