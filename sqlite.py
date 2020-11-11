#sqllite sistema de gestion de bases de datos // crear base de datos.
#creamos base de datos nueva si no existe
import sqlite3
conexion = sqlite3.connect("bdatos.db")

conexion.close()

import sqlite3
conexion = sqlite3.connect("bdatos.db")

cursor = conexion.cursor()  #se utiliza para ejecutar sentencias slq en la base de datos
#CREAMOS TABLA EN LA BASE DE DATOS
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT,apellido2 TEXT, edad INTEGER)")
conexion.commit()
conexion.close()

#INTERTAR FILA/DATOS
import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('ANTONIO','PEREZ','GOMEZ',35)")
conexion.commit()
conexion.close()





