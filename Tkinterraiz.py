#tkinter componente raiz(componente comun con raiz.mainloo())
import tkinter
raiz = tkinter.Tk()
raiz.title("Mi programa")


#creamos componente frame
frame = tkinter.Frame(raiz)
frame.config(bg="blue",width =400,height=300)
frame.pack()

#tkinter componente label
texto = "Hola carol"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack()
#Entrada de datos por teclado componente entry.
entrada= tkinter.Entry(raiz)
entrada.config(justify="center",show="*")#ponerlo tipo password que no se vea con ***
entrada.pack()
#Tkinter componente text, campo de texto largo para introducir texto por teclado

entrada =  tkinter.Text(raiz)
entrada.config(width=20, height=10,font=("Verdana",15), padx=10,pady=10,fg="green",selectbackground="lightgrey")
entrada.pack()

#tkinter -  componente button (botón para realizar una acción)
# definimos la función accion
def accion():
    print("hola seba estoy megapythoneado XD")
boton = tkinter.Button(raiz,text="ejecutar",command=accion)
boton.pack()

#tkinter componente radiobutton
def seleccionar():
    print("la opción seleccionada es {}",format(opcion.get()))
    opcion = tkinter.IntVar()
radiobutton1 =tkinter.Radiobutton(raiz, text="opcion1",variable=opcion,value=1,command=seleccionar)
radiobutton1.pack()

#tkinter checkbutton boton de verificación.
def verificar():
    valor = check1.get()
    if (valor ==1):
        print("activado")
    else:
        print("desactivado")

check1 = tkinter.IntVar()
checkboton1 = tkinter.Checkbutton(raiz,variable=check1,onvalue=1,offvalue=0,command=verificar)
checkboton1.pack()

#messagebox(mostrarinformacion)
#creamos componente popup.ventana de informacion
from tkinter import messagebox, filedialog


def avisar():
    tkinter.messagebox.showinfo("Titutlo","mensaje con la información")

variable1= tkinter.Button(raiz,text="pulsar para aviso",command=avisar)
variable1.pack()

# tkinter -  messagebox pregunta.

#from tkinter import messagebox hay que ponerlo
def preguntar (): # definimos funcion

    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","quieres borrar el fichero=")
    if (resultado=="yes"):
        print("qiuere borrar el fichero?")
    else:
        print("No, no quiero borrarlo")

boton = tkinter.Button(raiz, text="pulsar para preguntar",command=preguntar)

#tkinter filedialog para abrir un fichero.
#definimos abrir fichero
def abrirfichero():
    ruta = filedialog.askopenfilename(title="abrir fichero")

boton = tkinter.Button(raiz,text="pulsar para empezar",command=abrirfichero)
boton.pack()

raiz.mainloop()


