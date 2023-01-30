import tkinter

def aparecer_lab():
        lab=tkinter.Label(root,text="")
        lab.config(text="HOLA MUNDO")
        lab.place(x=20,y=150)

def abrirSegundaVentana():
        rootDos =tkinter.Tk()
        rootDos.geometry("400x300")
        rootDos.config(bg="pink")  #CONFIGURA AZUL LA RAIZ
        rootDos.title("EJEMPLO SEGUNDA VENTANA")  #SE LE COLOCA TITULO A LA RAIZ
        labDos=tkinter.Label(rootDos,text="")
        labDos.config(text="Hola soy la segunda ventana")
        labDos.place(x=20,y=140)
 
root=tkinter.Tk()
root.geometry("400x300")
root.config(bg="turquoise")  #CONFIGURA AZUL LA RAIZ
root.title("EJEMPLO")  #SE LE COLOCA TITULO A LA RAIZ

#Se crean los botones y llaman sus respectivas funciones
bot=tkinter.Button(root,text="Aparecer Label",command=aparecer_lab)
bot.place(x=20,y=40)

botDos=tkinter.Button(root,text="Segunda Ventana",command=abrirSegundaVentana,width=18)
botDos.place(x=20,y=70)

botTres=tkinter.Button(root,text="Cerrar",command=root.destroy)
botTres.place(x=20,y=100)

root.mainloop()