import tkinter
raiz = tkinter.Tk()
raiz.title("mi programa")

from tkinter import messagebox, filedialog

# tkinter filedialog para abrir un fichero.
# definimos abrir fichero
def abrirfichero():
    ruta = filedialog.askopenfilename(title="abrir fichero")
    tkinter.messagebox.showinfo("LA ruta es:",ruta)

boton = tkinter.Button(raiz, text="pulsar para empezar", command=abrirfichero)
boton.pack()



raiz.mainloop()


