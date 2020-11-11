# HTML con PYTHON
import pandas as pd
import numpy as np

desired_width=320 # para ver más columnas

pd.set_option('display.width', desired_width)


pd.set_option('display.max_columns',10)

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.read_html(url)
# print(dataframe)
print(dataframe)
datafootball = dataframe[0]
# print(datafootball)


# datafootball = datafootball.rename(columns=dict(datafootball.loc[1])) # si e titulo de las columnas está mal, lo sustituye por el indice que le digamos//en este caso no hace falta las columnas las cogio bien
# print(datafootball)
# print(datafootball)
datafootball = datafootball.drop(0) #para borrar la fila 0
datafootball = datafootball.drop('Notas',axis=1) #para borrar la columna notas

print(datafootball)




