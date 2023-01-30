'''Ejemplo condicional simple'''

#Entradas
p_interes=int(input("Ingresar porcentaje interes: "))
capital=int(input("Ingresar capital: "))
interes=capital * ((p_interes)/100)

#procedimiento y salida
if interes>7000:
        capf=capital+interes
        print("El capital final es: ",capf)

