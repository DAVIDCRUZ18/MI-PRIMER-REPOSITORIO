'''Ejemplo de GUI simple'''

import tkinter

def mostrar():
        mensaje.configure(text="Hola mundo")

ventana=tkinter.Tk()
mensaje=tkinter.Label(ventana,text="",width=18)
mensaje.place(x=100,y=100)
boton=tkinter.Button(ventana,text="Saludar",width=10,command=mostrar)
boton.grid()

ventana.mainloop()