#FUNCIONES GENERADORAS GENERA VALORES SOBRE LA MARCHA
range(0,11) # generaria del 0 al 10
for numero in range(0,11): # o podemos poner Range(11)
    print(numero)



def pares(maximo): # funcion generadora de pares
    for numero in range(maximo):
        if (numero % 2 == 0): # quiere decir que es un numero par.
            yield numero

maximo = 20
for numero in pares(maximo):
    print(numero)