# agrupar datos categorias
import pandas as pd
import numpy as np

precios = [42,55,48,23,5,21,88,34,26]
rangodeprecios = [10,20,30,40,50,60,70,80,90,100]
precios_con_rango = pd.cut(precios,rangodeprecios)  # agrupa los precios dento del rango
print(precios_con_rango)

contar = pd.value_counts(precios_con_rango) # contar cuantos hay en cada categoria

print(contar)
