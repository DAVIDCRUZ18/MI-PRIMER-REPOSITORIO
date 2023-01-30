//Realizar un procedimiento que permita realizar la división entre dos números y muestre el
//cociente y el resto utilizando el método de restas sucesivas.
//El método de división por restas sucesivas consiste en restar el dividendo con el divisor hasta
//obtener un resultado menor que el divisor, este resultado es el residuo, y el número de restas
//realizadas es el cociente. Por ejemplo: 50 / 13:
//		50 / 13 = 37 una resta realizada
//		37 / 13 = 24 dos restas realizadas
//		24 / 13 = 11 tres restas realizadas

Algoritmo EJ8_RestasSucesivas
	Definir dividendo,divisor Como Entero;
	
	dividendo=50;
	divisor=13;
	divisionesSucesivas(dividendo,divisor);
	
	
FinAlgoritmo

SubProceso divisionesSucesivas( dividendo ,divisor)
	Resultado es real;
	i es entero;
	i=1;
	
	Hacer
		Resultado=dividendo - divisor;
		dividendo =Resultado;
		Imprimir dividendo "/" divisor " = " Resultado " ",i, " resta realizada";
		i=i+1;
//		Imprimir n1;
//		Imprimir n2;
//		Imprimir Resultado;
	Mientras Que Resultado>=divisor
	
	
FinSubProceso
	