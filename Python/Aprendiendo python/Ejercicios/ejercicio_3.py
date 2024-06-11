def es_primo(num):
    for i in range(2, num):
        if(num%i==0): return False
    return True
primos = []
for num in range(100):
    if(es_primo(num)):
        primos.append(num)
print(primos)
