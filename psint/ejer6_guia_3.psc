//Realizar un procedimiento que permita intercambiar el valor de dos variables de tipo entero.
//La variable A, debe terminar con el valor de la variable B.
Algoritmo ejer6_guia_3
	definir a, b como entero 
	
	a=1
	b=2
	
	intercambio(a,b)
	
	escribir a
	escribir b
	
FinAlgoritmo

SubProceso intercambio(a por referencia, b Por Referencia)
	Definir c como entero 
	
	c=a
	a=b
	b=c
	//escribir a
	//escribir b
FinSubProceso
	