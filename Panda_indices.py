#indices en panda
import pandas as pd
listavalores = [1,2,3]
listaindices = ['a','b','c']
serie = pd.Series(listavalores,index = listaindices)
serie.index[0] # no se pueden cambiar los indices da error
print(serie.index)

lista_valores = [(6,7,8),(5,3,2),(5,6,7)]
lista_indices = ['mates','historia','fisica']
nombres =['antonio','pedro','juan']

dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=nombres)
print(dataframe)
print(dataframe.index)

