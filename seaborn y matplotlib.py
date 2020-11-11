# #libreria para hacer graficos estadísticos
# #histogramas representacion grafica en forma de barras
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


datos1 = np.random.randn(100)

plt.hist(datos1)
plt.show() # para que enseñe los gráficos

sns.distplot(datos1,color='green') # muestra una linea en el histograma de datos
plt.show()

datos2 =np.random.randn(80)
plt.hist(datos2)
plt.hist(datos1,color='green',alpha=0.3,bins=20) # si los ponemos uno tras otro cuando lo enseñamos los junta los graficos.
plt.hist(datos2,color='blue',alpha=0.3,bins=20)
plt.show()
datos3 =np.random.randn(1000)
datos4 =np.random.randn(1000)
sns.jointplot(datos3,datos4,kind='hex')
plt.show()

#DISTRIBUCIONES-------------------------------------------------------------------
#COMBINANDO ESTILOS
#importamos pandas,numpy,matplotlib,seaborn


datos = np.random.randn(100)

sns.distplot(datos,rug=False, hist=False) # solo deja la linea
plt.show()

argumentos_curva = {'color':'black','label':'Curva'}
argumentos_histograma = {'color':'grey','label':'histograma'}
sns.distplot(datos,bins=25, kde_kws=argumentos_curva, hist_kws=argumentos_histograma) # pone la leyenda de la curva y las barras
plt.show()

serie= pd.Series(datos)
sns.distplot(serie,bins=25,color='green') # pasar serie a histograma

# GRAFICOS DE CAJA
# DIAGRAMA DE CAJA

#IMPOTAMOS PANDAS,NUMPY,MATPLOTLIB.PYPLOT Y SEABORN

datos10= np.random.randn(100)

sns.boxplot(datos10) # 50% de los datos estan en medio, y el resto 25% a los lados en medio la mediana.

#REGRESIONES LINEALES-----------------------------------

# Importamos numpy, seaborn,pandas

propinas = sns.load_dataset('tips') # conjunto de datos de propinas preconfigurados ya
print(propinas.head(10))


sns.lmplot('total_bill','tip',propinas,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'blue'}) # regresión lineal

plt.show()

sns.lmplot('total_bill','tip',propinas,fit_reg=False)# de izq a derecha, ejex, ejey. solo pone los puntitos sin linea

plt.show()

propinas['porcentaje'] =100*propinas['tip'] / propinas['total_bill'] # hemos añadido columnas porcentaje con su formula
print(propinas.head())

sns.lmplot('size','porcentaje',propinas)
plt.show()

sns.lmplot('total_bill','porcentaje',propinas,hue='sex',markers=['x','o']) # muestra x para mujeres o para homrbes
plt.show()

sns.lmplot('total_bill','porcentaje',propinas,hue='day')
plt.show()

# MAPAS DE CALOR (HEATMAPS)
#IMPORTAMOS PANDAS,NUMPY, SEABORN,

vuelos = sns.load_dataset('flights')
#para mapadecalor necesitaoms que sea una matriz.

vuelos=vuelos.pivot('month','year','passengers') # de izq a derecha, fila, columna, datos.

print(vuelos)
sns.heatmap(vuelos,annot=True,fmt='d')
plt.show()

#recoger valor concreto
print(vuelos.loc['May'][1956]) # nos da directamente el dato.
valor_central= vuelos.loc['May'][1956]
sns.heatmap(vuelos,center=valor_central, annot=True,fmt='d') # el valor central hace que a partir de este se acentuen los colores.
plt.show()

# poner leyenda vertical en la horizontal
sns.heatmap(vuelos,center=valor_central, annot=True,fmt='d',cbar_kws={'orientation':'horizontal'}) # el valor central hace que a partir de este se acentuen los colores.

plt.show()

