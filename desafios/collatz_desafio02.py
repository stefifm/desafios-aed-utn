print("Secuencia Collatz")

def promedio(suma, total):
    if total > 0:
        prom = suma / total
    else:
        prom = 0
    return prom

secuencia = []
n = int(input("Ingrese un número: "))
secuencia.append(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    secuencia.append(n)


prom = round(promedio(sum(secuencia), len(secuencia)), 1)


print("Longitud de la secuencia es:",len(secuencia))
print("Mayor de la secuencia:",max(secuencia))
print("Promedio de la secuencia:",prom)