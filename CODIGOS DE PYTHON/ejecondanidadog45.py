'''Ejemplo condicional Anidado'''

#Entradas
num1=float(input("Ingresa un número: "))
num2=float(input("Ingresa un número: "))

#Procedimiento
if num1 == num2:
        resultado=num1*num2

elif num1>num2:
        resultado=num1-num2 

else: 
        resultado=num1+num2

#Salida
print("El resultado es: ",resultado)