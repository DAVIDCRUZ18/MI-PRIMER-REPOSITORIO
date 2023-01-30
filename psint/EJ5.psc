//Realizar un programa que rellene un vector de tama�o N, con valores ingresados por el
//usuario. A continuaci�n, se deber� crear una funci�n que reciba el vector y devuelva el valor
//m�s grande del vector.

Algoritmo EJ5
	Definir N,Vec Como Entero;
	
	Mostrar "Ingrese El tama�o del vector";
	Leer N;
	Dimension Vec[N];
	
	LlenarVector(Vec, N);
	Mostrar "El n�mero mayor del vector es: " EncontrarMayor(Vec, N);
	
FinAlgoritmo

SubProceso LlenarVector(vector por Referencia, tam)
	Definir i,num Como Entero;
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		Mostrar "Ingrese n�mero " (i+1);
		Leer num;
		vector[i]=num;
	Fin Para
FinSubProceso

Funcion mayor<-EncontrarMayor(vector por Referencia, N)
	Definir mayor, may,i Como Entero;
	may=vector[0];
	
	Para i<-0 Hasta N-1 Con Paso 1 Hacer
		Si may<vector[i] Entonces
			may=vector[i];
		Fin Si
	Fin Para
	mayor=may;
FinFuncion
	