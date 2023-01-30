import tkinter

def mostrar():
        mensaje.configure(text="Hola")

ventana=tkinter.Tk()
mensaje=tkinter.Label(ventana,text="",width=12)
mensaje.grid(row=1,column=1)
boton=tkinter.Button(ventana,text="Saludo",command=mostrar)
boton.grid()

ventana.mainloop()
