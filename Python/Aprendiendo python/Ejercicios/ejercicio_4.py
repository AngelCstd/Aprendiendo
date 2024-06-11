def fibonacci(num):
    a, b = 0, 1
    lista = [a]
    for i in range(num):
        if b > num: return lista
        else:
            lista.append(b) 
            a,b = b, a+b