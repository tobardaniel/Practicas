import math


def bases(n):
    if n == 0:
        return('0')
    elif n == 1:
        return('INFINITY')
    else:
        sumas = 1
        i = 2
        while i < n:
            potencia = int(math.log(n, i))
            primer = n // i**potencia
            resto = n - (i ** potencia)
            if primer == 1 and potencia == 1:
                sumas += resto
                i += resto
            elif primer == 1:
                sumas += 1
                i += 1
            else:
                i += 1
        return(sumas)


def bases1(n):
    if n == 0:
        return('0')
    elif n == 1:
        return('INFINITY')
    else:
        sumas = 1
        for j in range(2,n):
            if primer_digito(n, j) == 1:
                sumas += 1
        return(sumas)

def primer_digito(numero, base):
    digito = numero
    while digito >= base:
        digito = digito // base
    return digito


#casos = input()
#for i in range(int(casos)):
#    bases = bases1(int(input()))
#    print(bases)

for i in range(10000, 1000000):
    rapido = bases(i)
    lento = bases1(i)
    if rapido != lento:
        print(i, rapido, lento)

# fallos
# [3**5 = 243, 129, 130],
# [(2*5)**3 = 1000, 514, 515],
# [17**3, 4913, 2485, 2486],
# [31**3 = 29791, 14959, 14960],
# [39304 = (2*17)**3, 19723, 19724],
# [(3**5)**2 = 59049, 29610, 29612],
# [41**3 = 68921, 34554, 34555],
# [((2**4) * 3)**3 = 110592, 55411, 55412]
# [140608 = ((2**2) * 13)**3 , 70430, 70431]
# [175616 = ((2**3) * 7)**3, 87949, 87950]