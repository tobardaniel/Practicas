import math
import time
import random
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443]


def f_cifras(numero):
    string = str(bin(numero))
    lista_str = list(string)[:1:-1]
    digitos = []
    for k in range(len(lista_str)):
        if lista_str[k] == '1':
            digitos.append(k)
    return digitos


def simple_sum_bin(numero, mod):
    suma = 0
    for i in range(1, numero + 1):
        arr_cifras = f_cifras(i)[::-1]
        potencia = 1
        for k in arr_cifras:
            potencia = (potencia*pow(i, pow(2, k), mod)) % mod
        suma += potencia
    return suma % mod


def simple_sum_mod(numero, mod):
    suma = 0
    for i in range(1, numero+1):
        potencia = pow(i, i, mod)
        suma = suma + potencia
    return suma % mod


def f_primo(numero):
    prim = True
    for k in primos:
        if numero % k == 0:
            prim = False
            break
    return prim


def f_phi(numero):
    pass


def simple_sum(numero, mod):
    sumas = 0
    modulo_primo = f_primo(mod)
    if modulo_primo:
        veces = mod * (mod - 1)
        repeticiones = numero // veces
        resto = numero % veces
        phi = mod - 1
        if numero <= veces or True:
            for j in range(1, numero + 1):
                sumas += pow(j, j % phi, mod)
        else:
            for j in range(1, veces + 1):
                sumas += repeticiones * pow(j, j % phi, mod)
            for j in range(1, resto + 1):
                sumas += pow(j, j % phi, mod)
    return sumas % mod


mod = 1013
num = random.randrange(10000000)
print(num)
start = time.time()
resultado2 = simple_sum(num, mod)
end = time.time()
tiempo2 = end-start
print('Función elaborada: ', resultado2, ' con tiempo de: ', tiempo2)
start = time.time()
resultado2 = simple_sum_mod(num, mod)
end = time.time()
tiempo2 = end-start
print('Potencia modular: ', resultado2, ' con tiempo de: ', tiempo2)
