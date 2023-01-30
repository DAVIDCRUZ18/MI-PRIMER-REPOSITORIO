Algoritmo EJ4_Vectores
	menu();
FinAlgoritmo

SubAlgoritmo menu()
	Definir op Como Caracter;
	Definir sum,res,N,VecA,VecB,VecC,i  Como Entero;
	Mostrar "Ingrese El tamaño de los vectores";
	Leer N;
	Dimension VecA[N],VecB[N],VecC[N];
	
	Hacer
		Mostrar "*****MENÚ*****";
		Mostrar "A. Llenar Vector A. Este vector es de tamaño N y se debe llenar de manera aleatoria";
		Mostrar "B. Llenar Vector B. Este vector también es de tamaño N y se llena de manera aleatoria";
		Mostrar "C. Llenar Vector C con la suma de los vectores A y B.";
		Mostrar "D. Llenar Vector C con la resta de los vectores B y A.";
		Mostrar "E. Mostrar Vector A, B, o C.";
		Mostrar "F. SALIR";
		Mostrar "Digite su opción: ";
		Leer op;
		
		op=Mayusculas(op);
		
		Mostrar "";
		Segun op Hacer
			"A":
				Mostrar "...Llenando vector A...";
				Mostrar "...";
				LlenarVector(VecA,N);
				Mostrar "Vector A Llenado correctamente";
				Mostrar "Digite cualquier tecla para vovler al menu";
				Esperar Tecla;
				Limpiar Pantalla;
			"B":
				Mostrar "Llenando vector A...";
				Mostrar "...";
				LlenarVector(VecB,N);
				Mostrar "Vector B Llenado correctamente";
				Mostrar "Digite cualquier tecla para vovler al menu";
				Esperar Tecla;
				Limpiar Pantalla;
			"C":
				Mostrar "Llenando vector C con la SUMA del Vector A+B...";
				Suma(VecA,VecB,VecC,N);
				Mostrar "...";
				Mostrar "Vector C Llenado correctamente con la Suma";
				Mostrar "Digite cualquier tecla para vovler al menu";
				Esperar Tecla;
			"D":
				Mostrar "Llenando vector C con la resta del Vector B-A...";
				Resta(VecA,VecB,VecC,N);
				Mostrar "...";
				Mostrar "Vector C Llenado correctamente con la Resta";
				Mostrar "Digite cualquier tecla para vovler al menu";
				Esperar Tecla;
			"E":
				Mostrando(VecA,VecB,VecC,N);
				Mostrar "";
				Mostrar "Digite cualquier tecla para vovler al menu";
				Esperar Tecla;
			"F":
				
			De Otro Modo:
				Mostrar "OPCIÓN INCORRECTA:";
		Fin Segun
		Mostrar "";
	Mientras Que (op<>"F" )
FinSubAlgoritmo

SubProceso LlenarVector(vector por Referencia, tam)
	Definir i,num Como Entero;
	
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		vector[i]=Aleatorio(-100,100);
	Fin Para
FinSubProceso

SubProceso suma(vectorA Por Referencia, vectorB Por Referencia, vectorC por Referencia, tam)
	Definir i,resultado Como Entero;
	
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		vectorC[i]=vectorA[i]+vectorB[i];
	Fin Para
	
FinFuncion

SubProceso Resta(vectorA Por Referencia, vectorB Por Referencia, vectorC por Referencia, tam)
	Definir i,resultado Como Entero;
	
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		vectorC[i]=vectorB[i]-vectorA[i];
	Fin Para

FinFuncion

Funcion Mostrando(vectorA Por Referencia, vectorB Por Referencia, vectorC por Referencia, tam)
	Definir op Como Caracter;
	Mostrar "Que vector desea mostrar A B o C";
	Leer op;
	op=Mayusculas(op);
	Segun op Hacer
		"A":
			ImprimirVector(vectorA,tam);
		"B":
			ImprimirVector(vectorB,tam);
		"C":
			ImprimirVector(vectorC,tam);
	Fin Segun
FinFuncion

SubProceso ImprimirVector(vector por Referencia, tam)
	Definir i,num Como Entero;
	
	Para i<-0 Hasta tam-1 Con Paso 1 Hacer
		Mostrar Sin Saltar "[",vector[i],"]";
	Fin Para
FinSubProceso