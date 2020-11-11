import sqlite3
conexion = sqlite3.connect("bdatos.db")
cursor=conexion.cursor()
cursor.execute("select * from personas") #selecciona todos los datos de la tabla
personas = cursor.fetchall()   #recogemos los resultados y los ponemos en la variable personas

for persona in personas:
     print(persona)
     conexion.close()


