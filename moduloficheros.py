class fichero:
    def __init__(self,nombre):
       self.nombre=nombre

    def recordfile(self,texto):
        file = open(self.nombre, "wt")
        file.write(texto)
        file.close()

    def readfile(self):
        file = open(self.nombre, "rt")
        file2=file.read()
        return file2

    def includefile(self,texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()






