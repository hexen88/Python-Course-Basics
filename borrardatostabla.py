#sqlite3 borrar datos tabla
import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'luis'")
conexion.commit()
conexion.close()
