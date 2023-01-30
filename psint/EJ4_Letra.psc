//Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. La
//función debe devolver la cantidad de veces que encontró la letra. Nota: recordar el uso de la
//	función Subcadena().

Algoritmo EJ4_Letra
	Definir frase, letra Como Caracter;
	Definir cantiEncontrado Como Entero;
	
	Mostrar sin saltar "Ingrese una frase: ";
	Leer frase;
	Mostrar sin saltar "Ingrese una letra a buscar en esa frase: ";
	Leer letra;
	
	frase=Minusculas(frase);
	letra=Minusculas(letra);
	
	Escribir "La cantidad de veces que encontró la letra ",letra, " en la frase ", frase, " fue de " ContarLetras(frase,letra);
	
FinAlgoritmo

Funcion cantiEncontrado<- ContarLetras(frase,letra)
	Definir i,cantiEncontrado, size  Como Entero;
	cantiEncontrado=0;
	
	size=Longitud(frase);
	Para i=0 Hasta size-1 Con Paso 1
		si (letra=SubCadena(frase,i,i))
			cantiEncontrado=cantiEncontrado+1;
		FinSi
	FinPara
FinFuncion
	