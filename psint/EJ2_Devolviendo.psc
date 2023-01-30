//Diseñar una función que reciba un numero en forma de cadena y lo devuelva como numero
//entero. El programa podrá recibir números de hasta 3 dígitos. Nota: no poner números con
//decimales ni letras. Ejemplo: ingresando "100"(carácter) debe convertirse en 100(entero).
Algoritmo Devolviendo
	Definir numCade Como Caracter;
	Definir size,numEntero Como Entero;
	
	
	Mostrar "Ingrese numero: ";
	Leer NumCade;
	size=Longitud(NumCade);
	
	//VALIDAR
	Mientras size>3 Hacer
		Mostrar "ERROR, EL número ingresado contiene más de 3 digitos";
		Leer NumCade;
		size=Longitud(NumCade);
	FinMientras
	numEntero=ConvertirANumero(NumCade);
	Mostrar "En texto : « " NumCade " »";
	Mostrar "En número " numEntero;
FinAlgoritmo


