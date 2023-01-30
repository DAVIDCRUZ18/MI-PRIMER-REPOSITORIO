//Dada una matriz de orden n * m (donde n y m son valores ingresados por el usuario) realizar
//un subprograma que llene la matriz de numeros aleatorios. Despues, crearemos otro
//subprograma que calcule y muestre la suma de los elementos de la matriz. Mostrar la matriz y
//los resultados por pantalla.

Algoritmo ej10guia4
	definir n,m, matriz como enteros
	escribir "ingrese un valor para la fila y otro para la columna"
	leer n, m
	
	Dimension matriz(n, m)
	llenarMatriz(matriz, n, m)
	mostrarMatriz(matriz, n,m) 
	sumamatriz(matriz, n, m) 
	
FinAlgoritmo


SubProceso llenarMatriz( matriz Por Referencia, n, m)
	definir i, j Como Entero
	
	Para i<-0 Hasta n-1 Con Paso 1 Hacer
		Para j<-0 Hasta m-1 Con Paso 1 Hacer
			matriz(i,j)= Aleatorio(0, 100) 
		Fin Para
	Fin Para
	
FinSubProceso

SubProceso mostrarMatriz( matriz Por Referencia, n, m)
	definir i, j Como Entero
	
	Para i<-0 Hasta n-1 Con Paso 1 Hacer
		Para j<-0 Hasta m-1 Con Paso 1 Hacer
			escribir Sin Saltar matriz(i,j), " "
		Fin Para
		Escribir " "
	Fin Para
FinSubProceso


SubProceso sumamatriz( matriz Por Referencia, n, m)
	definir i, j, suma Como Entero
	suma=0
	Para i<-0 Hasta n-1 Con Paso 1 Hacer
		Para j<-0 Hasta m-1 Con Paso 1 Hacer
			suma= suma + matriz(i,j)
		Fin Para
	Fin Para
	Escribir " la suma de los elementos de la matriz es: ", suma 
FinSubProceso
	