//Programe una función recursiva que calcule la suma de un arreglo de números enteros.
//explicación https://puntocomnoesunlenguaje.blogspot.com/2012/07/ejemplos-de-recursividad-suma-desde-1.html
Algoritmo EJ7_EXTRAS
	Definir vector,N Como Entero;
	N=3;
	Dimension vector[N];
	LlenarVector(vector,N);
	MostrarVector(vector,N);
	Definir i Como Entero;
	Mostrar "La suma de los elementos del arreglo es: " suma(vector,N);
	
FinAlgoritmo
SubProceso LlenarVector(vector por Referencia,tam)
	Definir i Como Entero;
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		vector[i]=Aleatorio(1,50);
	Fin Para
FinSubProceso

SubProceso MostrarVector(vector por Referencia,tam)
	Definir i Como Entero;
	Mostrar "";
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		Mostrar Sin Saltar "[",vector[i],"]";
	Fin Para
	Mostrar "";
FinSubProceso

Funcion resultado<-suma(vector por Referencia,tam)
	Definir resultado,sum Como Entero;
	
	si tam==1 Entonces//Condición Base
		resultado=vector[tam-1];
	sino
		resultado= vector[tam-1]+suma(vector,tam-1);
	FinSi
	
FinFuncion
	