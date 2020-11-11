#consultar con una det condicion

import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor = conexion.cursor()
cursor.execute("select * from personas where edad > 40")
personaseleccion = cursor.fetchall()
for persona in personaseleccion:
    print(persona)

conexion.close()

#consultar datos y ordenarlos por columna.
import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor= conexion.cursor()
cursor.execute("select * from personas ORDER by edad")
listapersonasedad = cursor.fetchall()
for persona in listapersonasedad:
    print(persona)
    conexion.close()
