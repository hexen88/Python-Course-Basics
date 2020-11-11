# renombrar indices
import pandas as pd
import numpy as np

lista_valores = np.arange(9).reshape(3,3)
lista_indices = list('abc')
dataframe = pd.DataFrame(lista_valores,index=lista_indices)
print(dataframe)

#cambiar indices a letras en mayúsculas x ejemplo
nuevos_indices = dataframe.index.map(str.upper) # indices puesto en mayusculas
dataframe.index = nuevos_indices # asignamos nuevos indices al dataframe

 # otra forma de hacerlo
dataframe = dataframe.rename(index=str.lower)

newindex= {'a':'f','b':'g','c':'h'}

dataframe = dataframe.rename(index=newindex)

newindex2= {'f':'j','b':'g','c':'h'}
dataframe.rename(index=newindex2,inplace=True) # Inplace=true lo asigna directamente



