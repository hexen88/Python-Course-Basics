#expresiones regulares (search,findall,split,sub)
#buscar cadena en una cadena
texto ="hola, mi nombre es Cristian"
import re
resultado = re.search("nombre$",texto) #con dolar lo busca x el final
#"^Hola" busca esa parte de la cadena
# "mi.*es que busque mi y es pero entre medio que haya caracteres.

if(resultado):
    print("cadena encontrada")
else:
    print("cadena no encontrada")

#findall
texto2="""
el coche de luis es rojo,
el coche de antonio es blanco,
el coche de maria es verde
"""
variable = re.findall("coche.*rojo",texto2)# que empiece por la palabra coche y acabe en rojo
print(variable)

#SPLIT
texto = "La silla es blanca y vale 80€"
v1=re.split("\s",texto)
print(v1)
#SUB sustituye todas las coincidencias de una cadena.
v2=re.sub("blanca","roja",texto)
print(v2)


