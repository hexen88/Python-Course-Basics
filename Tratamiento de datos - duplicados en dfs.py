# ELIMINAR DULPICADOS EN DATAFRAMES
import pandas as pd

lv = [[1,2],[3,4],[5,6],[1,2]]

lind = list('mnop')
lcol = ['valor1','valor2']

df1 = pd.DataFrame(lv,index=lind,columns=lcol)
print(df1)
#eliminar filas que tengan valor duplicado

df1 = df1.drop_duplicates()
print(df1)
# eliminar duplicados dentro de la misma columna

df1 = pd.DataFrame(lv,index=lind,columns=lcol)

df2= df1
df2 = df2.drop_duplicates(['valor1']) # elimina los valores repetidos siguientes en la columna.
print(df2)


#df2 = df2.drop_duplicates(['valor1'],keep='last') # keep='last' deja siempre el valor ultimo y elimina el repetido intermedio