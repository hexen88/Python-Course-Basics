import pandas as pd
import numpy as np

listaval = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]

listacol = list('abc')

df= pd.DataFrame(listaval,columns=listacol)

print(df.agg(['sum','min'],axis=1))# axis=1 suma por filas muestra suma del conjunto y minimo del conjunto

#         a     b     c
# sum  12.0  15.0  18.0
# min   1.0   2.0   3.0

