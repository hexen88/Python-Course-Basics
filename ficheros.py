##ABRIR FICHEROS
fichero=open("ejemplo.txt","rt")
datosfichero = fichero.read()

print(datosfichero)

#GRABAR FICHERO DE TEXTO O CREAR.
fichero = open("fichero_grabar.txt","wt") # CREARA UN FICHERO
texto_del_fichero = "hola, esta es la línea que vamos a grabar en el fichero"
fichero.write(texto_del_fichero)
fichero.close()

#AÑADIR INFORMACIÓN A TEXTO YA EXISTENTE.

fichero = open("fichero_grabar.txt","at")
cadena_para_incluir="\nesta es la ultima linea del fichero"
fichero.write(cadena_para_incluir)
fichero.close()

#BORRAR FICHERO DE TEXTO
import os
os.remove("hola.txt")

