#No es lo mismo importar un paquete que es una carpeta con multiples archivos a un solo archivo o funcion
#Esto se usa en caso de querer utilizar muchos modulos de una carpeta
#Esta la carpeta paquetespruebas para poder ver que pasa aqui, primero debemos colocar un archivo llamado __init__.py

#Una vez que logremos esto entonces python nos va a tomar ese archivo como un paquete al cual vamos a poder acceder a su path y mas
#Tambien esto nos va a permitir acceder a modulos que estan dentro de estos y a sus funciones
import PaquetePrueba.saludando_ando

PaquetePrueba.saludando_ando.saludando_ando()
#Tambien podemos importar subpaquetes que serian paquetes con el __init__ dentro de un paquete con el __init__
#------------------------------------------------------------
#Para poder instalar paquetes de terceras personas debemos colocar en la terminal
#py -m pip install {nombrePquete}
