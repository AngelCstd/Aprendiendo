#Tomando en cuenta que las personas dicen 2 palabras por segundos, pedirle al usuario que diga cualquier texto real 
#calcular cuando tardaria en decir esa frase
#cuantas palabras dijo

#si se tarda mas de un minuto decirle para flaco tampoco es testamento

#Si dalto habla un 30% mas rapido cuanto tardaria en decirlo?

texto = input("Che, pon un texto real y te calculo en cuanto tiempo lo dirias: ")
cantidad_de_palabras = len(texto.split(" "))
tiempo_en_decirlas = cantidad_de_palabras/2

if tiempo_en_decirlas < 60:
    print(f"Tardarias {tiempo_en_decirlas} en decir todas esas palabras")
    print(f"Dirias {cantidad_de_palabras} palabras")
else:
    print("Para flaco que tampoco es testamento")

print("------------------------")
print(f"Dalto tardaria {tiempo_en_decirlas*.7} en decir esas palabras")
