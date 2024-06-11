#Estas funciones nos permten a dejar mas legible el codigo, no tener que estar repitiendo el codigo y poder modularlo
#las funciones se escriben de la siguiente manera:

#def [nombre_de_la_funcion]([parametros_de_la_funcion]):
#   [acciones de la función]
#   return [valor a retornar]
def sumatoria(num, num2):
    return num+num2
print(sumatoria(5,9))
#Podemos enviar una tupla en el return ya si queremos enviar varios valores 
def obteniendoExponentes(base, exponente):
    resultado = base**exponente
    return(resultado, exponente)
resultado, exponente = obteniendoExponentes(5,2)
print(f"Tu resultado es {resultado} y fue porque se elevo a {exponente}")

#Para usar el parametro args que es como el rest operator en javascript es usando el de multiplicacion antes del valor
def sumatoria(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
print(sumatoria(5,9,10,7,5,9))
#podemos definir algunos valores por default en la uncion a menos que lo reciba directamente y seria de la siguiente manera
def saludar(nombre, adjetivo = "tonto"):
    print(f"Hola {nombre} sos un {adjetivo}")
saludar("angel") #Aqui va a tomar el valor por defecto que tiene la funcion
saludar("dalto", "capo") #Aqui va a tomar el valor que le mandamos

#En caso de querer forzar lo que le mandamos debemos definir como se llaman los argumentos que le estamos mandando
saludar(adjetivo="capo", nombre="angel") #Aqui podemos ver que aun que les enviamos los argumentos en el orden invertido lo tomo bien, ya que le forzamos el nombre de estos argumentos
#----------------------------------------------------------------------------
#Funciones LAMBDA
#Esta es como las funciones flecha en javascript
#Se escribe de la siguiente manera
#
#lambda [parametro] : [Accion y retorno]
multipicar_por_dos = lambda x : x*2
resultado = multipicar_por_dos(5)
print(resultado) #10

#La puedes guardar en una variable o la puedes mandar como parametro
numeros = [2, 3, 4, 5, 6, 7, 8, 9]
numeros_pares = filter(lambda numero : numero%2==0, numeros)
#Aqui se convierte a lista porque retorna un objeto filter
list(numeros_pares)
print(numeros_pares)
