import pandas as pd
import numpy as np
#combinar series
serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6,])

serie3 = serie1.combine_first(serie2) # combina y si encuentra valor nulo lo cambia por el de la serie2

print(serie3)

#combinar dataframes

lv=[1,2,np.nan]
lv2 = [4,5,6]
df1 = pd.DataFrame(lv)
df2 = pd.DataFrame(lv2)
df3 = df1.combine_first(df2) # hace lo mismo que el caso anterior, rellena el hueco nulo con le sigiuente dataframe
print (df3)
