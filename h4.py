import math
import sys
import time


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
    for i in range(1, numero):
        potencia = pow(i, i, mod)
        suma = suma + potencia
    return suma % mod


def simple_sum1(numero, mod):
    suma = 0
    for i in range(1, numero):
        arr_cifras = cifras(i)[::-1]
        potencia = 1
        for k in arr_cifras:
            potencia = (potencia*pow(i, pow(2,k), mod)) % mod
        suma += potencia
    return suma % mod


start = time.time()
resultado2 = simple_sum(654321, 5465)
end = time.time()
tiempo2 = end-start
print('Lento: ', resultado2, ' con tiempo de: ', tiempo2)
start = time.time()
resultado2 = simple_sum1(654321, 5465)
end = time.time()
tiempo2 = end-start
print('Rápido: ', resultado2, ' con tiempo de: ', tiempo2)
