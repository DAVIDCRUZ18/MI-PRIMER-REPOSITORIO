//Dise�ar una funci�n que reciba un numero en forma de cadena y lo devuelva como numero
//entero. El programa podr� recibir n�meros de hasta 3 d�gitos. Nota: no poner n�meros con
//decimales ni letras. Ejemplo: ingresando "100"(car�cter) debe convertirse en 100(entero).
Algoritmo Devolviendo
	Definir numCade Como Caracter;
	Definir size,numEntero Como Entero;
	
	
	Mostrar "Ingrese numero: ";
	Leer NumCade;
	size=Longitud(NumCade);
	
	//VALIDAR
	Mientras size>3 Hacer
		Mostrar "ERROR, EL n�mero ingresado contiene m�s de 3 digitos";
		Leer NumCade;
		size=Longitud(NumCade);
	FinMientras
	numEntero=ConvertirANumero(NumCade);
	Mostrar "En texto : � " NumCade " �";
	Mostrar "En n�mero " numEntero;
FinAlgoritmo


