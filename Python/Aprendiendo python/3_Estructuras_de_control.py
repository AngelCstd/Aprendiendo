#IF ELSE
#If condicionEsTrueEntonces:
    #acciones a realizar
#else(sino):
    #acciones a realizar
edad = 19
if edad >=18:
    print("Pasas porque eres mayor de edad")
else:
    print("No pasas mi hermano")
#Elif es para ver si se cumplen ciertas condiciones, digamos que tienes 5 condiciones distintas pero al realizarce la 3 igual se realiza la 4 y la 5, elif permite que si se realiza la 3 entonces la 4 y la 5 ya no se ejecutan porque corresponden al mismo bloque de elif
if edad == 18:
    print("Ya sacaste tu ine?")
elif edad >=18:
    print("Pasas porque eres mayor de edad")
else:
    print("No pasas mi hermano")
#Bucles
#Aqui en python para poder iterar listas/tuplas si usamos el bucle for in que sirve como un foreach pero se escribe de la siguiente manera:
#for [objeto de lista] in [lista]:
animales = ["perro", "gato", "cocodrilo", "loro"] 
for animal in animales:
    print(animal)
numeros = [4 ,5 , 6 , 9]
#Asi se pueden recorrer dos listas al mismo tiempo, pero ambas tienen que tener la misma cantidad de oobjetos dentro, pueden ser la cantidad de listas que quieras
for numero, animal in zip(numeros, animales):
    print(f"Este es el numero: {numero}")
    print(f"Este es el animal: {animal}")
#Esto igual funciona si queremos obtener numeros, por ejemplo si le damos un rango de numeros esos numeros se convertiran en nuestros nuevos objetos de llista y la lista seran los numeros
for numero in range(0, len((numeros))):
    print(numero)
#Esto funciona igual ya que solo le estamos diciendo hasta donde lo queremos
for numero in range(len((numeros))):
    print(animales[numero])
#Pero la forma correcta de recorrer una lista junto con su indice es con la funcion enumerate ya que la lista se convierte en una lista de tuplas indice : valor
for indice, valor in enumerate(animales):
    #Como dato es que la siguiente lista esta desempaquetando la tupla, pero igual se puede desempaquetar al inicio, es lo mimo que haciamos cuando recorriamos 2 listas a la vez, creamos una lista de las istas y solo las desempaquetamos
    #indice, valor = tupla
    print(f"El indice es: {indice} y el valor es: {valor}")
#Igual si ponemos un else a un bucle este lo va a ejecutar solo una vez y sera cuando el bucle termine
for numero in numeros:
    print("Se pintan los numeeros")
else:
    print("el bucle termino")
#-----------------------------------------------------
#Iterando diccionario
#Es lo mismo solo que debemos obtener la lista de items con un clave valor, para eso usamos la funcion de items
diccionario = dict(nombre="angel",edad=15)
for key, value in diccionario.items():
    print(f"la clave es: {key} el valor es: {value}")
#-----------------------------------------------------------
#Continue
#Cuando tenemos esta palabra reservada dentro de un ciclo lo que va a hacer es ue se va a saltar todo lo demas que viene en el ciclo y lo va a volver a repetir, si son 10 lineas y en la 3 dice continnue, se va a saltar las otras 7 y repetira el ciclo o lo terminara como segun vaya
frutas = ["naranja", "papaya", "manzana", "fresa"]
for fruta in frutas:
    if fruta == "manzana":
        continue #Aqui ya no imprime la manzana, pasa al siguiente objeto
    print(fruta)
#"Break"
#Este nos sirve para terminar de plano el bucle y que ya no se ejecute nadamas
for fruta in frutas:
    if fruta == "manzana":
        break #Aqui ya no sigue el bucle, lo termina aun si faltan objetos en la lista de pasar
    #TAMPOCO EJECUTA EL ELSE
    print(fruta)

#Los string tambien sirven como listas de letra por letra
texto = "hola"
for caracter in texto:
    print(caracter)
#tambien podemos hacer ciclos en una sola linea
numeros = [2,5,8,1]
numeros_duplicados = [x*2 for x in numeros]
#---------------------------------------------------------------------------------
#El bucle while
#Este funciona igual que en los demas, se va a ejecutar siempre que la condicion sea true, de no ser asi entonces el ciclo se rompe o no entra
contador = 0
while contador < 3:
    print(contador)
    contador+=1
