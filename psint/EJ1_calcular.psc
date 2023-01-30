//Realizar una función que calcule y retorne la suma de todos los divisores del número n
//distintos de n. El valor de n debe ser ingresado por el usuario.

Algoritmo calcular
	Definir N Como Entero;
	
	Mostrar Sin Saltar "INGRESE N: ";
	Leer N;
	
	Mostrar "La suma de los divisores de " N " es: " Suma(N);
FinAlgoritmo

Funcion resultado<-Suma(N)
	resultado, i es entero;
	resultado=0;
	Para i=1 Hasta N Hacer
		
		Si (N MOD I =0 Y i<>N )
			resultado=resultado+i;
		FinSi
	FinPara
	
FinFuncion
	