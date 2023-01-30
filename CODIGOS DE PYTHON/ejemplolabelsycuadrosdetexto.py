#-------------------------------------------------------------------------------
# Name:        Ejemplo Cuadros de texto con labels
# Author:      Gab
# Created:     25/02/2021
# Copyright:   (c) Gab 2021
#-------------------------------------------------------------------------------

import tkinter

#CONFIGURACIÓN RAIZ
menu=tkinter.Tk() #SE CREA LA RAIZ o ventana LLAMADA menu
menu.geometry("600x600")
menu.config(bg="aquamarine")  #CONFIGURA AZUL LA RAIZ
menu.title("TERCER EJEMPLO")  #SE LE COLOCA TITULO A LA RAIZ
menu.resizable(0,0) #SE DICE QUE SE PUEDA MODIFICAR EL TAMAÑO

#CONFIGURACIÓN LABELS
#se crea el label cuadrounolabel y se le coloca el texto NOMBRE
cuadrounolabel=tkinter.Label(menu,text="NOMBRES")  
#Se configura el label en la fila 0, columna 0, y 10 pixeles de espacio alrededor
cuadrounolabel.grid(row=0,column=0,padx=10, pady=10) 
#se crea el label cuadrounolabel y se le coloca el texto NOMBRE
cuadrodoslabel=tkinter.Label(menu,text="APELLIDOS")  
#Se configura el label en la fila 0, columna 0, y 10 pixeles de espacio alrededor
cuadrodoslabel.grid(row=2,column=0,padx=10, pady=10) 

#CONFIGURACIÓN CUADROS DE TEXTO
uno=tkinter.StringVar()  #se crea la variable uno como un string
#se crea el cuadro de texto llamado cuadrouno
cuadrouno=tkinter.Entry(menu,textvariable=uno) 
##Se configura el cuadro en la fila 0, columna 2, y 10 pixeles de espacio
cuadrouno.grid(row=0,column=2,padx=10, pady=10) 

dos=tkinter.StringVar()  #se crea la variable uno como un string
#se crea el cuadro de texto llamado cuadrodos
cuadrodos=tkinter.Entry(menu,textvariable=dos) 
##Se configura el cuadro en la fila 0, columna 2, y 10 pixeles de espacio
cuadrodos.grid(row=2,column=2,padx=10, pady=10) 

menu.mainloop()



