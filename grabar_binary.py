#graba lista de colores en binario.
import pickle
lista_colores=["azul","verde","rojo","amarillo"]
fichero = open("fichero_colores.pckl","wb")

pickle.dump(lista_colores,fichero)
fichero.close()

#leer fichero binario
import pickle
fichero=open("fichero_colores.pckl","rb")
lista_leida = pickle.load(fichero)
print(lista_leida)

frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

fichero = open("frutas_lista.pckl","wb")
pickle.dump(frutas,fichero)
fichero.close()
fichero = open("frutas_lista.pckl","rb")
lista_leida2 = pickle.load(fichero)
print(lista_leida2)
lista_leida2.values() # para comprobar estructura diccionario que esta bien





