Algoritmo sin_titulo
	
	//Escriba un programa que pida 3 notas y valide si esas notas est�n entre 1 y 10. Si est�n
	//entre esos par�metros se debe poner en verdadero una variable de tipo l�gico y si no
	//ponerla en falso. Al final el programa debe decir si las 3 notas son correctas usando la
	//variable de tipo l�gico.
	
	definir nota1, nota2, nota3 Como Entero
	
	escribir "ingrese la nota numero 1"
	leer nota1
	
	escribir "ingrese la nota numero 2"
	leer nota2
	
	escribir "ingrese la nota numero 3"
	leer nota3
	
	Si (nota1 >= 1) y (nota1 <=10)  Entonces
		escribir "verdadero"
	SiNo
		escribir "falso"
	Fin Si
	
	Si (nota2 >= 1)y (nota2 <=10) Entonces
		escribir "verdadero"
	SiNo
		escribir "falso"
	Fin Si
	
	Si (nota3 >= 1)y (nota3 <=10) Entonces
		escribir "verdadero"
	SiNo
		escribir "falso"
	Fin Si
	
FinAlgoritmo
