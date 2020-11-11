class Coche:

    def __init__(self,color,marca,combustible,cilindrada):
        self.color = color
        self.marca = marca
        self.combustible = combustible
        self.cilindrada =1.6

    def mostrar_caracteristicas(self):
        print("este coche es de marca {} de color {} y con cilindrada de {}".format(self.marca,self.color,self.combustible,self.cilindrada))


media=lambda nota1,nota2,nota3 : (nota1 +nota2 + nota3)/3