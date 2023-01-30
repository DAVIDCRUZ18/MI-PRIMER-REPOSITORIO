'''Ejemplo de GUI simple'''

import tkinter

ventana=tkinter.Tk()
boton=tkinter.Button(ventana,text="CERRAR VENTANA",command=ventana.destroy)
boton.grid()

ventana.mainloop()