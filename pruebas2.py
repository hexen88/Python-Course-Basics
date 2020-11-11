import pandas as pd
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt
desired_width=320 # para ver más columnas
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

listaval = np.random.randn(6,4)
listacol = list('abcd')

df = pd.DataFrame(listaval,columns=listacol)

print(df)


sns.lmplot('a','b',df,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'blue'}) # regresión lineal
plt.show()


rango = list(range(1900,2000,5))
print(rango)









def listaleatorios(n,lista):

    for i in range(n):
        lista[i] = random.randrange(10,100)
        return lista

print("ingrese cuantos numeros aleatorios quiere obtener")
n =int(input())
lista = [n]

aleatorios=listaleatorios(n,lista)
print(aleatorios)






