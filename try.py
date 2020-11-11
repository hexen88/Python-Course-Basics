#TRY PERMITE VERIFICAR SI UN BLOQUE DE CODIGO TIENE ERRORES.
##try:
  #  numero1 = 5
 #   numero2 = 0
 #   div = numero1/numero2
#    print(div)
#except ZeroDivisionError:
#    print("ha habido un error entre 0")
#except:
#    print("ha habido un error")
#else:
#    print("todo correcto")
#finally:
#print("la prueba ha acabado")


try:
    num1=5
    num2=4
    num3=2


    resta=num2-num3
    div=num1/resta
    print(div)
except ZeroDivisionError:
    print("ha habido una división entre 0")
else:
    print("error")
finally:
    print("se ha ejecutado correctamente")



