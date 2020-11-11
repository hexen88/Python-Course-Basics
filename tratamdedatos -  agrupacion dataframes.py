# agrupacion de dataframes
import pandas as pd
import numpy as np

listaval = {'clave1':['x','x','y','y','z'],'clave2':['a','b','a','b','a'],'datos1':np.random.rand(5),'datos2':np.random.rand(5)}

df=pd.DataFrame(listaval)
#   clave1 clave2    datos1    datos2
# 0      x      a  0.361964  0.587989
# 1      x      b  0.493613  0.597827
# 2      y      a  0.817729  0.328638
# 3      y      b  0.766874  0.677610
# 4      z      a  0.434221  0.973698

grupo1 = df['datos1'].groupby(df['clave1'])
print(grupo1.mean())


