
import pandas as pd
import numpy as np

array1 = np.arange(9).reshape(3,3)
# concatenar arrays
array3 = np.concatenate([array1,array1]) # concatena hacia abajo manteniendo 3 columnas.
array4 = np.concatenate([array1,array1],axis=1) # concatena hacia la derecha, serían 6 columnas.

#concatenar series
serie1 = pd.Series([1,2,3],index=('a','b','c'))
serie2 = pd.Series([4,5,6], index =('d','e','f'))

serie3 = pd.concat([serie1,serie2],keys=['serie1','serie2']) # nos concatena a continacion los indices y los valores. keys: añade clave para cada serie
# quedaría así.
# serie1  a    1
#         b    2
#         c    3
# serie2  d    4
#         e    5
#         f    6

#CONCATENAR DATAFRAMES

df1 = pd.DataFrame(np.random.rand(3,3),columns=['a','b','c'])
df2 = pd.DataFrame(np.random.rand(2,3),columns=['a','b','c'])

df3 = pd.concat([df1,df2],ignore_index=True) # concatena a continuación, ignore index,para que siga con el indice del primero y continue
print(df3)

# 0  0.945780  0.676373  0.495864
# 1  0.361367  0.958837  0.925369
# 2  0.485943  0.533562  0.017442
# 0  0.434013  0.285932  0.754271
# 1  0.412258  0.970520  0.047526




