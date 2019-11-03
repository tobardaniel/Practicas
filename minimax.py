import numpy as np


def leer_matriz(n):
    matriz = []
    for i in range(n):
        fila = [int(s) for s in input().split(' ')]
        matriz.append(fila)
    matriz = np.array(matriz)
    return matriz


def ordenar(matriz, arg='F'):
    if arg == 'F':
        matriz = np.array([sorted(s) for s in matriz])
        matriz = matriz.transpose()
        return matriz
    elif arg == 'C':
        matriz = matriz.transpose()
        matriz = np.array([sorted(s)[::-1] for s in matriz])
        matriz = matriz.transpose()
        return matriz


def minimax(matriz):
    cambios = len(matriz)
    n = 0
    matriz_filas = ordenar(matriz, 'F')
    matriz_columnas = ordenar(matriz, 'C')
    if min(matriz_columnas[0]) == max(matriz_filas[0]):
        return('0')
    elif min(matriz_columnas[0]) < max(matriz_filas[0]):
        fallo = True
        while fallo and n <= len(matriz):
            for k in range(n):
                if min(matriz_columnas[k]) >= max(matriz_filas[n-k]):
                    cambios = n
                    fallo = False
            n += 1
        return cambios
    elif min(matriz_columnas[0]) > max(matriz_filas[0]):
        fallo = True
        while fallo and n <= len(matriz):
            for k in range(n):
                if min(matriz_columnas[k]) <= max(matriz_filas[n - k]):
                    cambios = n
                    fallo = False
            n += 1
        return cambios


matriz = leer_matriz(int(input()))
print(minimax(matriz))