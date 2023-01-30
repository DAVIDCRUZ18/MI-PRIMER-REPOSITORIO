//Crea una función EsMultiplo que reciba los dos números pasados por el usuario, validando
//que el primer número múltiplo del segundo y devuelva verdadero si el primer número es
//	múltiplo del segundo, sino es múltiplo que devuelva falso.
Algoritmo EJ3_Multiplo
	Definir n1,n2 Como Entero;
	Definir resultado Como Logico;
	
	Mostrar Sin Saltar "Digite N1: ";
	Leer n1;
	Mostrar Sin Saltar "Digite N2: ";
	Leer n2;
	
	resultado=EsMultiplo(n1,n2);
	
	Mostrar resultado;
	
	
FinAlgoritmo

Funcion resultado<-EsMultiplo(n1,n2)
	Definir resultado Como Logico;
	si (n1 mod n2=0) Entonces
		resultado=Verdadero;
	SiNo
		resultado=Falso;
	FinSi
FinFuncion
	