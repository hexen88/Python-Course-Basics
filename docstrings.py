#DOCSTRINGS CADENAS PARA DOCUMENTAR

def hello (nombre):
    """
    esto será un comentario de la funcion saludar
    :param nombre:
    :return:
    """
    print("buenos días", + nombre)

class prueba1:
    """esta clase tendra......"""
    def buenos_dias(self,nombre):
        """ esto saluda a la gente"""
        print("buenosdías {}".format(nombre))

    def adios2 (self,nombre):
        """ esto despide a la gente"""
        print("adios {}".format(nombre))

# UNA VEZ TENGAMOS LA DOCUMENTACION EN LAS FUNCIONES CREAMOS EL PYDOC.
# abrimos el terminal y buscamos el directorio donde esta guardado docstrings.py
#PYDOCS
# pydoc y la ruta del fichero completo.
# nos sale el help de la función


# help(prueba1) # con esto venos esas lineas verdes comentadas para saber como funciona la función

# DOCTEST -  GENERAR PRUEBAS DENTRO DE LA DOCUMENTACION
#ponemos >>> para probar la funcion y el resultado debajo
#al final pondremos import doctest doctest.testmod()
#en el terminal pondreoms python nombredelfichero.py y -v y realizará el test.

def sumar (num1,num2):
    """
    esta es una funcion que suma dos numeros

    >>> sumar(4,3)
    7

    """
    return num1 + num2
resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()

# UNITTEST -  SIRVE PARA GENERAR PRUEBAS DENTRO DEL PROPIO CODIGO.
import unittest


def multiplicar(num1, num2):
    return num1 * num2

resultado2 = multiplicar(3, 6)
print(resultado2)


class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(4, 2), 8)
        self.assertEqual(multiplicar(4, 2), 9)

if __name__ == '__main__':
    unittest.main()
