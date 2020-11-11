# combinaciones de elementos
import pandas as pd
import numpy as np

listaval = np.arange(25).reshape(5,5)

df = pd.DataFrame(listaval)

combinacionaleatoria = np.random.permutation(5) # genera del 0 al 4 de manera aleatoria

df = df.take(combinacionaleatoria) #muestas las filas en el orden de la combinación

print(df)
