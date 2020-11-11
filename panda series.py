# #SERIES
import pandas as pd

serie1 = pd.Series([3,5,7]) # es como una array pero indexa con 0-1 1-5 2-7 3, y le asigna un ID a cada dato.
print(serie1)
asignaturas = ['matematicas','historia','fisica','literatura']
notas = [8,6,8,3]
series_notas_daniel = pd.Series(notas,index=asignaturas) # le decimos que indices queremos para que no los ponga automáticamente

print(series_notas_daniel)
print(series_notas_daniel['fisica'])

print(series_notas_daniel[series_notas_daniel >= 8])

series_notas_daniel.name = 'Notas de Daniel' # le ponemos un nombre

series_notas_daniel.index.name = 'asignaturas de daniel'

#CONVERTIR SERIE EN DICCIONARIO.
diccionario = series_notas_daniel.to_dict()
print(diccionario)
serie = pd.Series(diccionario)  # crear serie a partir de un diccionario.

print(serie)

#copiamos la serie y cambiamos el nombre
notas_ana =[2,3,4,5]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)

# suma de las notas de la clase
serie_notas_clase = (series_notas_daniel+serie_notas_ana)/2
print(serie_notas_clase)










