//Crea una funci�n EsMultiplo que reciba los dos n�meros pasados por el usuario, validando
//que el primer n�mero m�ltiplo del segundo y devuelva verdadero si el primer n�mero es
//	m�ltiplo del segundo, sino es m�ltiplo que devuelva falso.
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
	