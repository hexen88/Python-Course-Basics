#DATAFRAMES
import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA' #nos lleva a la web.
# webbrowser.open(website) # abrir la pagina en el navegador
dataframe_nba = pd.read_clipboard() # esto captura lo que hay en el portapapeles x ejemplo de una web
var1 = dataframe_nba.columns# nos dice las columnas
var2 = dataframe_nba['nombre exacto de la columna'] # nos devuelve solo esa columna.
var3 = dataframe_nba.loc[5] # solo nos dara la fila 5.
var4 = dataframe_nba.head # nuestra 5 primeras filas
var5 = dataframe_nba.tail # nos enseña los 5 ultimas filas.

# PASAR DICCIONARIO A DATAFRAME
lista_asignaturas = ['mates','fisica']
notas = [8,7]
diccionario = {'asignaturas':lista_asignaturas,'Notas':notas}

dataframe_notas = pd.DataFrame(diccionario)

print(dataframe_notas)

#ELIMINAR ELEMENTOS EN SERIES Y DATAFRAMES
import pandas as pd
import numpy as np
np.arange(4) # devuelve del 0 al 4 en una array
serie = pd.Series(np.arange(4),index=['a','b','c','d'])

series = serie.drop(index=('c'))  #borraremos el indice c en la serie, pero no lo borra
print(serie)

lista_valores = np.arange(9).reshape(3,3) # 9 valores de 3 filas y 3 columnas
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']
dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
print(dataframe)
dataframe = dataframe.drop('b') # borra el indice que le hemos dicho del dataframe
print(dataframe)
dataframe = dataframe.drop('c2',axis=1) # borrar columna
print(dataframe)

# SELECCIONADO DATOS EN LAS SERIES
#IMPORTAMOS PANDAS Y NUMPY
lista_v = np.arange(3) # creamos array 0-3
lista_i = ['i1','i2','i3']
serie = pd.Series(lista_v,index=lista_i)
serie[0:2] # nos devuelve valores entre medio
serie[i1]
serie[1]
serie[i1:i3]
#seleccionar con condición
serie[serie >3] = 9 # cambiamos el valor.

#SELECCIONANDO ENTRADAS PARA DATAFRAMES

#IMPORTAMOS NUMPY Y PANDAS
import pandas as pd
import numpy as np
listava = np.arange(25).reshape(5,5) # creamos una array de 0-24 en 5 filas 5 columnas
listaind = ['i1','i2','i3','i4','i5']
listacol = ['c1','c2','c3','c4','c5']

dataprueba = pd.DataFrame(listava,index=listaind,columns=listacol)

print(dataprueba['c2']) # solo nos mostraria la columna dos con sus respectivos indices

print(dataprueba['c2']['i2'])  # valor concreto columna 2 i2
print(dataprueba[['c3','c4']]) # muestra columna 3 y 4
print(dataprueba[dataprueba['c2']> 15]) # nos da valores mayores que 15 de la columna 2
print(dataprueba > 20) # nos devuelve los que son mayores de 20 con un true

dataprueba.loc['i3'] #selecciona la fila 3 con las respectivas columnas solamente .loc para seleccionar con indice.



#OPERACIONES SOBRE SERIES Y DATAFRAMES
import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])

serie2 = pd.Series([3,4,5,6],index=['a','b','c','d'])

seriesuma = serie1+serie2 # suma los índices de dos series.
listaval = np.arange(4).reshape(2,2)
listi = list('ab') # construye una lista con un elemento 'a' y un elemento 'b' separados
listacolumnas = list('12')
framedata = pd.DataFrame(listaval,index=listi,columns=listacolumnas)
print(framedata)

listaval2 = np.arange(9).reshape(3,3)
listai2 = list('abc')
listacol2 = list('123')

dataframe2 = pd.DataFrame(listaval2,index=listai2,columns=listacol2)
print(dataframe2)

dataframe3= dataframe2+framedata # si suma asi da valores null para la partes que no tiene con quien sumar
dataframe3 = framedata.add(dataframe2,fill_value=0) #Suma con 0, no da null aunque las matrices tengan diferente tamaño
print(dataframe3)

#ORDENAR Y CLASIFICAR SERIES
#IMPORTAMOS PANDA Y NUMPY

listaval4 = range(4)
listaindices9 = list('CABD')
series = pd.Series(listaval4,index=listaindices9)

# los indices estan desordenados. vamos a ordenarlos por alfabetico
series.sort_index() #ordena por indice alfabetico
series.sort_values()# ordena por los valores
series.rank() # ordena sobre el valor más pequeño al mas grande.
serie2 = pd.Series(np.random.randn(10)) # creamos 10 valores random de 10 numeros
print(serie2.rank()) # da la posicion que ocupa cada uno e un rankin

print(serie2.sort_values().rank()) # ordenaria el ranking.

#ESTADÍSTICAS EN DATAFRAMES

array = np.array([1,8,3],[5,6,7])
dataframe5 = pd.DataFrame(array, index=['a','b'],columns=[list('123')])
dataframe5.sum() # suma por columnas y da el resultado final
dataframe5.sum(axis=1) # suma por filas
dataframe5.min() # minimo valor por columnas
dataframe5.max() #  maximo valor por columnas
dataframe5.idxmin() # minimo valor pero devuelve con indice y columna

dataframe5.describe() # nos da una serie de parametros como la media, desviacion, cuantos elementos hay, minimo... maximo

# VALORES NULOS

#importamos padas y numpy

lv10 = ['1','2',np.nan,'4']

serie = pd.Series(lv10,index=list('abcd'))

serie.isnull # nose dice true en el que esta nulo
serie.dropna() #elimina la fila null.

lv12 = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]
lind = list('123')
lcol = list('abc')

dataframe12 = pd.DataFrame(lv12,index=lind,columns=lcol)

dataframe12.isnull() # nos dice true donde es nulo
dataframe12.dropna() # borra todas las filas que contengan null.
dataframe12.fillna(0) # rellenar null con valor 0.

# JERARQUIA EN LOS ÍNDICES
#IMPORTAMOS PANDA Y NUMPY

lval1 = np.random.rand(6) # array con 6 elementos random.
lind1 = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
series0001 =  pd.Series(lval1,index=lind1)
# en este caso el array tiene indice 1 luego a b c para cada numero y luego 2, a b c, como doble indice.
series0001[1] #nos mostrara a b c del 1.
series001[1][b] #nos mostrara solo el 1B

series001 = series.unstack() # el indice principal lo pone como indice de fila y el segundo abc lo pone como columna.

lval12 = np.arange(16).reshape(4,4)
lind111 = list('1234')
lcol112 = list('abcd')

datafram113 = pd.DataFrame(lval12,index=lind111,columns=lcol112)
# a partir de este dataframe podemos crear doble indice.
serie3 = datafram113.stac() # esto crea ( de izq a der) indice 1 - abcd - 01234 y así. metodo contrario al anterior.

#EJERCICIO SERIES DATAFRAME

listaclases = ['clase1','clase2','clase3']
numeroalumnos = np.random.randint(0,40,3)
listacolal = list('abc')

serieclases = pd.Series(numeroalumnos,index=listaclases)
print(serieclases)
















