#SQLITE INSERTAR VARIOS REGISTROS EN NUESTRA TABLA

import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor =  conexion.cursor()

lista_personas = [('pedro','rodriguez','perez',26),('Maria','Lopez','gomez',45),('luis','gonzalez','perez',46)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)",lista_personas)
conexion.commit()
conexion.close()

