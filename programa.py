#IMPORTAR FUNCIONES DE ARCHIVO MODULO2.PY
#import modulo2

#coche1 = modulo2.Coche("fiat","blanco","diesel", "1.4")
#print(coche1.mostrar_caracteristicas())

#media = modulo2.media(3,9,4)
#print("nuestra nota media es: {}".format(media))#

import moduloficheros
name ="cristian.txt"

fichero = moduloficheros.fichero(name)

texto="eoeoeoeoeoeoeoeoeoeoeoeoeoeoeoeoe\noeooeeoeoeoeo"

fichero.recordfile(texto)

fichero.includefile("\nnueva linea")

texto_leido = fichero.readfile()

print(texto_leido)



















