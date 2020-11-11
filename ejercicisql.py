import sqlite3
conexion = sqlite3.connect("basedatos.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (id TEXT, nombre TEXT,precio INTEGER)")
lista =[(1,'impresora',300),(2,'raton',20),(3,'ordenadores',600)]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",lista)
conexion.commit()
cursor.execute("SELECT * FROM PRODUCTOS")
datos=cursor.fetchall()
conexion.close()

for v1 in datos:
    print(datos)
