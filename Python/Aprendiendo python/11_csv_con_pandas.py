import pandas as pd
print(type(pd))
#para leer un archivo usamos la funcion read
dfConNombres = pd.read_csv("Aprendiendo python\\archivos\\datos.csv", names=["nombresPaps", "ApellidoPapusiento", "viejo"])
print(dfConNombres)
#Ahora si vemos esto nos pinta de una forma que podemos leerlo mas sencillo

#    nombre   apellido  edad
#0    lucas      dalto    99
#1  roberto  demencial    42

#  nombresPaps ApellidoPapusiento viejo
#0      nombre           apellido  edad
#1       lucas              dalto    99
#2     roberto          demencial    42

#Al mandarle el argumento names nos va a cambiar los nombres de las coolumnas
#Le ponemos de nombre dfConNombres poraue es un dataFrame que son estructuras de datos bidimensionales similares a una hoja de calculo, de esta manera podemos acceder a una columna colocando como si fuera un diccinario
nombre = dfConNombres["nombresPaps"]

df = pd.read_csv("Aprendiendo python\\archivos\\datos.csv")
#Ahora con esto podemos ordenar los valores segun una columna, en este caso por la edad
df_ordenado = df.sort_values("edad")
print(df_ordenado)
#    nombre   apellido  edad
#1  roberto  demencial    42
#0    lucas      dalto    99

#Ahora asi lo ordenamos descendientemente
df_ordenado_reves = df_ordenado.sort_values("edad", ascending=False)
print(df_ordenado)
#    nombre   apellido  edad
#0    lucas      dalto    99
#1  roberto  demencial    42
#Para cncatenardos dataFrame se puede usar una funcion
df_concatenado = pd.concat([df_ordenado, df_ordenado_reves])
print(df_concatenado)
#    nombre   apellido  edad
#1  roberto  demencial    42
#0    lucas      dalto    99
#0    lucas      dalto    99
#1  roberto  demencial    42
print("-----------------------")

#Ahora podemos acceder a las primeras filas con head y a las ultimas con tail, dependiendo el numero que le mandes son las filas que te va a mostrar (sin pones 0 en head son los nombres de las columnas)
print(df_concatenado.head(2))
#    nombre   apellido  edad
#1  roberto  demencial    42
#0    lucas      dalto    99
print("-----------------------")
print(df_concatenado.tail(2))
#    nombre   apellido  edad
#0    lucas      dalto    99
#1  roberto  demencial    42

#describe nos da las cosas de probabilidad y estadistica basicas
print(df.describe())
#iloc nos ayuda a cierta fila y valor que queremos, se le manda una lista de la cual el primer dato son las filas, ya sea con slicing lo podemos manejar o con algun numero, en este ejemplo le decimos de todas las flas muestrame la columna 1 que seria apellido
print(df.iloc[:,1])
#0        dalto
#1    demencial

#Aqui le pediremos de la fila 1 todas las columnas
print(df.iloc[1,:])
#nombre        roberto
#apellido    demencial
#edad               42

#De esta manera podemos manejar o que buscamos, tambien existe loc, donde las columnas se las tenemos ue mandar como estan escritas, por ejemplo aqui la fila 1 de la columna nombre
print(df.loc[1,"nombre"]) #roberto

#Igual podemos acceder a una condicion, aqui le decimos que donde la edad sea menor a 50 nos muestre todas las columnas
print(df.loc[df["edad"]<50,:]) #1  roberto  demencial    42


