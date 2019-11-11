import random
import time


def funcion_d(n, x, conjunto, secuencia):
    if n == 0:
        return x
    elif n in conjunto:
        return 0
    else:
        suma = 0
        for i in range(1, n + 1):
            suma = (suma + secuencia[(i - 1) % len(secuencia)]*funcion_d(n-i, x, conjunto, secuencia)) % (10**9 + 7)
        return suma


#arreglo = input().split()
#n = int(arreglo[3])
#x = int(arreglo[0])
#con = [int(s) for s in input().split()]
#con = set(con)
#sec = [int(s) for s in input().split()]
#print(funcion_d(n, x, con, sec))


n = 35
x = random.randrange(10000)
con = set(random.sample(range(n), 12))
sec = [random.randrange(1000) for s in range(12)]
start = time.time()
print(funcion_d(n, x, con, sec))
print(time.time() - start)
