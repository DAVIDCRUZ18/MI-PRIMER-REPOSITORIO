//Rellenar en un subproceso una matriz cuadrada con números aleatorios salvo en la diagonal
//	principal, la cual debe rellenarse con ceros. Una vez llena la matriz debe generar otro
//	subproceso para imprimir la matriz.

Algoritmo ej11guia4
	definir matriz, tamColumna Como Entero
	tamColumna=3
	Dimension matriz(tamColumna, tamColumna)
	llenarMatriz(matriz, tamColumna,tamColumna)
	mostrarMatriz(matriz, tamColumna,tamColumna)
FinAlgoritmo


SubProceso llenarMatriz( matriz Por Referencia, n, m)
	definir i, j Como Entero
	
	
	Para i<-0 Hasta n-1 Con Paso 1 Hacer
		Para j<-0 Hasta m-1 Con Paso 1 Hacer
			si i <>j Entonces
				matriz(i,j)= Aleatorio(1, 99) 
			sino 
				matriz(i,j)= 0
			FinSi
	
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