Algoritmo sin_titulo
	
	///Realiza un programa que s�lo permita introducir los caracteres ?S? y ?N?. Si el usuario
	///ingresa alguno de esos dos caracteres se deber� de imprimir un mensaje por pantalla que
	///diga "CORRECTO", en caso contrario, se deber� imprimir "INCORRECTO".
	
	definir ele Como caracter
	
	escribir" por favor ingrese uno de los dos siguientes caracteres: S o N"
	Escribir "S"
	Escribir "N"
	leer ele
	segun ele hacer
		"S":
			escribir "correcto"
		"N":
			Escribir "correcto"
		de otro modo:
			escribir "incorrecto"
	finsegun
FinAlgoritmo
