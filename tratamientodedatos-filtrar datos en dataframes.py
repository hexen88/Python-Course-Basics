# filtrar datos en dataframes

import pandas as pd
import numpy as np

listaval = np.random.rand(10,3) # numeros aleatorios
df = pd.DataFrame(listaval)
print(df)

columna0 = df[0]

print(columna0[columna0 > 0.40]) # devuelve datos mayores de 0.40

print(df[df > 0.40])




