numero=int(input("Ingrese un número entero diferente de cero (0) para iniciar "))
sumaPositivos=0

while numero!=0:
	if numero>0:
		positivos=numero
		sumaPositivos+=positivos
	print("La suma de los números positivos es igual a: ", sumaPositivos)
	numero=int(input("Ingrese un número entero diferente de cero (0) para iniciar "))

print("A ingresado cero (0) el programa finalizará")
print("La suma total es: ", sumaPositivos)