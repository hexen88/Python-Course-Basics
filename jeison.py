#JSON
#CONVERTIR DATOS DE UN DICCIONARIO PYTHON A ESTRUCTURA JSON
producto1 = {"nombre":"silla","color":"blanco","precio":80}
import json
estruc = json.dumps(producto1)
print(estruc)

#convertir estructura json a diccionario

producto2 = json.loads(estruc)
print(producto2)
