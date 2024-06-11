#La forma que se escribe es 
#try:
#   [acciones a realizar]
#except:
#   [accion a realizar en caso de error]
#Esto nos sirve para manejar algunos tipos de errores, por ejemplo definamos una funcion
def sumar_dos():
    a = input("Ingresa el primer numero")
    b = input("Ingresa el segundo numero")
    resultado = int(a) + int(b)
    return resultado
#Aqui tenemos la funcion inicial, que no tienen ningun error a menos que en lugar de un numero le mandes un caracter
#Ahora deberemos hacer una funcion que maneje el error, en este caso solo vamos a darle aviso que no se pudo procesar lo que el quiso hacer
def sumar_dos_manejando_error():
    a = input("Ingresa el primer numero: ")
    b = input("Ingresa el segundo numero: ")
    try:
        resultado = int(a) + int(b)
        return resultado
    except:
        print("Hermano a que estamos jugando, te dije NUMERO")
        return "Error"

#print(sumar_dos_manejando_error())
#Ahora vamos a hacer un bucle para que no termine a menos que todo saliera bien con la funcion, si hay un error volvera a repetirse
def sumar_dos_manejando_error_bucle():
    #Iniciando bucle
    while True:
        a = input("Ingresa el primer numero: ")
        b = input("Ingresa el segundo numero: ")
        #Intentando convertirlo a entero y sumarlos
        try:
            resultado = int(a) + int(b)
            return resultado
        #Si lanzo una excepcion decirle que estamos esperando un numero
        except:
            print("Hermano a que estamos jugando, te dije NUMERO")
        #Si todo saliio bien terminar el bucle
        else:
            break
#Igual podemos acceder al objeto error para mostrarlo
def sumar_dos_manejando_error_bucle_objeto_excepcion():
    #Iniciando bucle
    while True:
        a = input("Ingresa el primer numero: ")
        b = input("Ingresa el segundo numero: ")
        #Intentando convertirlo a entero y sumarlos
        try:
            resultado = int(a) + int(b)
            return resultado
        #Si lanzo una excepcion decirle que estamos esperando un numero
        except Exception as e:
            print(f"Hermano a que estamos jugando, me sacaste el error \n{e}")
        #Si todo saliio bien terminar el bucle
        else:
            break
