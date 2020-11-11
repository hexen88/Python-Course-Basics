#reemplazar datos en series
import pandas as pd

serie = pd.Series([1,2,3,4,5],index=list('abcde'))
# serie = serie.replace(1,6)     # cambia valor 1 por el 6
seroe = serie.replace({2:8,3:9}) # cambiamos valores mediante diccionarios cambia el 2 por el 8 y el 3 por el 9



