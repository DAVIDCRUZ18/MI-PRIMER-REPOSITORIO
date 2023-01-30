#entradas

cadena= input("Ingrese una cadena de caracteres ")
validacion = True
cuenta=0
#procedimiento

while validacion:
    busqueda=input("Ingrese un caracter a buscar ")
    if len(busqueda)==1:
        validacion= False
    
for i in cadena:
    if i==busqueda:
        cuenta+=1

#salidas    
print("Para la cadena", cadena, "el caracter '", busqueda, "' se repite", cuenta, "veces")