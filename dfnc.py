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


arreglo = input().split()
n = int(arreglo[3])
x = int(arreglo[0])
con = [int(s) for s in input().split()]
con = set(con)
sec = [int(s) for s in input().split()]
print(funcion_d(n, x, con, sec))
