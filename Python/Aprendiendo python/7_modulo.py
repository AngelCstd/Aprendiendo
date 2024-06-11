#Los modulos son cualquier archivo que termina en la extension .py
#Esta nos sirve para poder acomodar y separar el programa en partes y python ya tiene algunos por defecto
#Tambien hay unos modulos que son de terceros donde lo descargamos de otras personas que crean sus librerias
#Tambien existen los modulos que creamos nosotros
#Para poder acceder a ese modulo desde otro archivo debemos importarlo de la siguiente manera:
#----------------------------------------------------------
#import prueba_modulo_saludar
#prueba_modulo_saludar.saludar_desde_modulo("Hola estoy desde el modulo mandando a llamar a esta funcion")
#--------------------------------------------------------
#Esto de una forma funcona, pero en caso de querer nombrar de una manera mas corta el modulo podemos usar as
#import prueba_modulo_saludar as saluda
#saluda.saludar_desde_modulo("Hola aqui en el modulo probando as")
#---------------------------------------------------------------
#Esto nos va a servir para poder importar solo una funcion
from prueba_modulo_saludar import saludar_desde_modulo as saludar, saludar_raro as saludar_raramente
saludar("Saludando mportando solo la funcion y cambiandole el nombre")
saludar_raramente("Este es otro tipo")
#------------------------------------------------------------------
#Igual podemos ver cuales son las funciones que tenemos dentro de un modulo usando el dir
import prueba_modulo_saludar as modulo
#Esto es para ver todas las propiedades y metodos del namespace
print(dir(modulo)) #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'saludar_desde_modulo', 'saludar_raro']
#------------------------------------------------------------------------
#Igual podemos acceder a modulos dentro de carpetas de la siguiente manera
from Ejercicios.ejercicio_4 import fibonacci as fibo
print(fibo(50))
#-----------------------------------------------------------------------
#Ahroa si necesitamos acceder a una que este en una carpeta fuera de la carpeta en la que estamos debemos coomenzar importando sys
import sys
#al importar sys podemos obtener el path de onde estan los modulos de python instalados y la primer ruta es nuestra ruta
#print(sys.path)
#Ahora solo deberiamos agregarle a los modulos instalados esa ruta
sys.path.append('c:\\Users\\luisa\\OneDrive\\Escritorio\\Proyectos\\Propios\\Organizacion de estudio\\Proyecto\\PruebaDeRutas')
import suma as  sumando
sumando.suma(4,7)
#Aun si nos dice que tiene error esto debe funcionar

