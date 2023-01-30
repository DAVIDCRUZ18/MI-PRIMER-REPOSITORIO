Algoritmo concatenar_1
	definir palabra,cadena2 como cadena
	definir num1 como entero 
	
	escribir "ingrese una palabra"
	leer palabra 
	
	num1=Longitud(palabra)
	
	
	Si num1=4 Entonces
		cadena2<-Concatenar(palabra,"!")
		escribir cadena2
	SiNo
		cadena2<-Concatenar(palabra,"?")
		escribir cadena2
	Fin Si
	
FinAlgoritmo
