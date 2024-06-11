#OPERADORES
saludo = "hola mi bro"
#   #DE PERTENENCIA
print("hol" in saludo) #True
print("hol" not in saludo) #False

#   #ARITMETICOS
    #SUMA Y RESTA
5+4
5-4
    #MULTIPLICACION
5*4
    #DIVISION FLOAT
divisionFloat = 5/4     #Esto nos devuelve un float aun si no tiene un valor decimal
    #EXPONNENTE
5**4    #el segundo numero es el exponente
    #DIVISION INT
divisionInt = 5//4    #Esta es la división baja que redondea el valor y este si devuelve un int
    #RESTO O MOD
5%4

#FUNCION PARA VER EL TIPO DE DATO
print(type(divisionFloat)) #FLOAT
print(type(divisionInt)) #"INT"

#LOGICOS
    #aqui solo se tiene que poner uno de & o |, no dos como en los otros, igual para decir que no se debe colocar not
resultado = True & False
resultado = True | False
resultado = not False
