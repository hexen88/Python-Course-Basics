#FICHEROS FORMATO EXCEL

import pandas as pd
desired_width=320 # para ver más columnas
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)
fichero_excel = pd.ExcelFile('/home/cristian/PycharmProjects/untitled/excels/poblacion.xlsx')

misdatos = fichero_excel.parse('Hoja 1') # selecciona los datos de la hoja 1 y crea un dataframe
print(misdatos)
print(misdatos['Ciudad más poblada'][3])

fichero_csv = pd.read_csv('/home/cristian/PycharmProjects/untitled/excels/poblacion.csv')

print(fichero_csv['Ciudad más poblada'][1])