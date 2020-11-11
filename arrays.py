# # #NUMPY ARRAYS
import numpy as np
np.zeros(4)
np.ones(4)
np.arange(5)

lista9 = np.arange(2,12,3)


lista2 = [2,3,4,5,6,7]
lista3 = [5,4,2,1,5,6]
listadoble = (lista2,lista3)
arrayprueba = np.array(listadoble)

#np.shape(arrayprueba) nos dice las filas y columnas
#np.dtype(arrayprueba) nos dice tipo de valores que tiene dentro.
print(arrayprueba)

# OPERACIONES CON ARRAYS

#primero importamos el modulo(ya esta arriba)
array1 = np.array([1,2,3,4])
array1 = array1 *2
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_d = (lista1,lista2)
arraydouble = np.array(lista_d)

#indexacion con arrays
array = np.arange(0,11)
array3 = array[0:3] #cogera los 3 primeros valores de la array.
array4 = array[:] #todos los valores cogerá
array_copia = array.copy
array_copia[0:3] = 20 # los 3 primeros elmentos valdrán 20

array2 = np.array(([1,2,3],[4,5,6],[7,8,9])) # tendra 3 filas x 3 columnas
# array2[0]  # nos dará la primera fila
# array[1][0] nos dará de la segunda columna el valor 0

#ARRAYS O MATRICES TRASPUESTAS
array = np.arange(15).reshape((3,5)) # array de 15 elementos con 3 filas y 5 columnas
#cambiar filas por columnas
array_trans = array.T
print(array_trans)

#ENTRADA Y SALIDA DE ARRAYS
array6 = np.arange(6)
np.save('array1s',array6) # guarda array con otro nombre
np.load('array1s.npy')     #carga el array guardado
array7 = np.arange(6)
array8= np.arange(6)
np.savez('arrays',x=array7,y=array8) # guarda las dos arrays en una variable de numpy
arrays_recuperados = np.load('arrays.npz')
arrays_recuperados[x]
arrays_recuperados[y]

np.savez('arrays',x=array7,y=array8) # guarda las dos arrays en una variable de numpy
arrays_recuperados = np.load('arrays.npz')







