#sqlite3 actualizar datos tabla
import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor = conexion.cursor()
cursor.execute("UPDATE PERSONAS SET edad = 30 where nombre = 'ANTONIO'")
conexion.commit()
conexion.close()

