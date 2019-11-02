import random
import math
import sys


def next_palin(numero):
    lista_numero = list(str(numero))
    medio = math.floor(len(lista_numero)/2)
    nueves = True
    for i in range(len(lista_numero)):
        if lista_numero[i] != '9':
            nueves = False
            break
    if nueves:
        lista_numero[0] = '1'
        for i in range(1, len(lista_numero)):
            lista_numero[i] = '0'
        lista_numero.append('1')
        print(''.join(lista_numero))
    else:
        if len(lista_numero) % 2 == 0:
            if palin(numero):
                for j in range(len(lista_numero)):
                    if lista_numero[medio + j] != '9':
                        lista_numero[medio+j] = str(int(lista_numero[medio+j])+1)
                        lista_numero[medio-1-j] = lista_numero[medio+j]
                        print(''.join(lista_numero))
                        break
                    else:
                        lista_numero[medio + j] = '0'
                        lista_numero[medio - 1 -j] = lista_numero[medio +j]
            else:
                j = 0
                while lista_numero[medio-1-j] == lista_numero[medio+j]:
                    j += 1
                if lista_numero[medio-1-j] > lista_numero[medio+j]:
                    for i in range(j, medio):
                        lista_numero[medio+i] = lista_numero[medio-1-i]
                    print(''.join(lista_numero))
                else:
                    for k in range(len(lista_numero)):
                        if lista_numero[medio-1-k] != '9':
                            lista_numero[medio-1-k] = str(int(lista_numero[medio-1-k])+1)
                            lista_numero[medio+k] = lista_numero[medio-1-k]
                            break
                        else:
                            lista_numero[medio + k] = '0'
                            lista_numero[medio - 1 - k] = lista_numero[medio + k]
                    for i in range(j, medio):
                        lista_numero[medio+i] = lista_numero[medio-1-i]
                    print(''.join(lista_numero))
        else:
            if palin(numero):
                for j in range(len(lista_numero)):
                    if lista_numero[medio-j] != '9':
                        lista_numero[medio-j] = str(int(lista_numero[medio-j])+1)
                        lista_numero[medio+j] = lista_numero[medio - j]
                        print(''.join(lista_numero))
                        break
                    else:
                        lista_numero[medio + j] = '0'
                        lista_numero[medio - j] = lista_numero[medio + j]
            else:
                j = 0
                while lista_numero[medio - j - 1] == lista_numero[medio + 1 + j]:
                    j += 1
                if lista_numero[medio - j - 1] > lista_numero[medio + 1 + j]:
                    for i in range(j, medio):
                        lista_numero[medio + i + 1] = lista_numero[medio - i -1]
                    print(''.join(lista_numero))
                else:
                    for k in range(len(lista_numero)):
                        if lista_numero[medio-k] != '9':
                            lista_numero[medio-k] = str(int(lista_numero[medio-k])+1)
                            lista_numero[medio+k] = lista_numero[medio - k]
                            break
                        else:
                            lista_numero[medio + k] = '0'
                            lista_numero[medio - k] = lista_numero[medio + k]
                    for i in range(j, medio):
                        lista_numero[medio + i + 1] = lista_numero[medio - 1 - i]
                    print(''.join(lista_numero))


def palin(numero):
        string = str(numero)
        if string == string[::-1]:
            return True
        else:
            return False


casos = input()
for i in range(int(casos)):
    num = input()
    next_palin(num)