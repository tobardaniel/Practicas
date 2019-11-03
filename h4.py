import math
import sys
import time
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443]


def cifras(numero):
    string = str(bin(numero))
    lista_str = list(string)[:1:-1]
    digitos = []
    for k in range(len(lista_str)):
        if lista_str[k] == '1':
            digitos.append(k)
    return digitos


def simple_sum(numero, mod):
    suma = 0
    for i in range(1, numero+1):
        potencia = pow(i, i, mod)
        suma = suma + potencia
    return suma % mod


def simple_sum1(numero, mod):
    suma = 0
    for i in range(1, numero + 1):
        arr_cifras = cifras(i)[::-1]
        potencia = 1
        for k in arr_cifras:
            potencia = (potencia*pow(i, pow(2,k), mod)) % mod
        suma += potencia
    return suma % mod












start = time.time()
resultado2 = simple_sum(1000000, 5465)
end = time.time()
tiempo2 = end-start
print('Lento: ', resultado2, ' con tiempo de: ', tiempo2)
start = time.time()
resultado2 = simple_sum1(1000000, 5465)
end = time.time()
tiempo2 = end-start
print('Rápido: ', resultado2, ' con tiempo de: ', tiempo2)