#Estos inputs nos permiten pedirle al usuario que ingrese algunos valores
nombre = input("Che, maestro, ingresa tu nombre: ")
print(nombre)
#Este valor siempre va a ser un texto, si deseamos que se convierta en un numero debemos convertirlo con la funcion int
numero = input("Bro rolame tu edad: ")
print("sin convertir a entero: "+numero*2)
numero = int(numero)
print("convertido a entero: "+numero*2)
