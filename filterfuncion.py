#FILTER FUNCION PARA FILTRAR RESULTADOS SEGUN UNA CONDICION

def positivo(numero):
    if (numero > 0):
        return True

    else:
        return False

numeros2 = [4,-2,8,-3,-5,-7,1,9]

filtro = filter(positivo, numeros2) #filtra valores positivos de la función directamente
resultado = list(filtro)
print(resultado)
