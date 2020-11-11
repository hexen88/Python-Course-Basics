#MAp aplicar una funcion a una lista
def multiplicar(numero):
    return numero*2
multiplicar(2)

numeros = [2,4,6]

mapeo = map(multiplicar,numeros)

resultado =list(mapeo)
print(resultado)

# lista_resultado = list(map(multiplicar,numeros))  # lo mismo pero todo en 1 linea

#ejecutar lo mismo sin crear una función para ello

lista_resultado = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado)



