import numpy as np
numeros_primos =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def primos(maximo):
    for numero in range(maximo):
        if (numero in numeros_primos):
            yield numero
        if ( numero >100):
            break

maximo = 50

for numero in primos(maximo):
    print(numero)

# ----------------------------------------------------------------------------
# otro ejercicio
def pares(inicio,fin):

    if (inicio %2 == 0):
        array= np.arange(inicio,fin,2)
    else:
        inicio=inicio+1
        array = np.arange(inicio, fin, 2)

    return array

hola=pares (10,100)
print(hola)
