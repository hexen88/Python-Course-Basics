import re
texto="esto es una frase de pruebas para hacer busquedas"
palabra = "una"
resultado = re.search(palabra,texto)
if resultado:
    print("se ha encontrdo la cadena {}".format(palabra))
    inicial = resultado.start()
    final =  resultado.end()
    print("empieza: {}, acaba: {}".format(inicial,final))
else:
    print("no se ha encontrado la palabra {}".format("frase"))
print(resultado)


#EJERCICIO SERIES DATAFRAME
import pandas as pd
import numpy as np
listaclases = ['clase1','clase2','clase3']
numeroalumnos = np.random.randint(0,40,3)
listacolal = list('abc')

serieclases = pd.Series(numeroalumnos,index=listaclases)
print(serieclases)













