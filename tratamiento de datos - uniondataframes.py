import pandas as pd


dataframe1 = pd.DataFrame({'c1':['1','2','3'],'clave':['a','b','c']})
# print(dataframe1)
dataframe2 = pd.DataFrame({'c2':['4','5','6'],'clave':['c','b','e']})

# print((dataframe2))

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2, on ='clave') # solo aparecen los datos que tengan claves en comun a las dos on:
# para que prevalezca el dataframe 1 y añada solo lo común del 2:
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='left') # prevalede el dataframe1 de la izquierda, o right derecha prevalece
#how=outer pone todas las filas de los dos dataframes y donde no encuentra valores pone null
print(dataframe4)






