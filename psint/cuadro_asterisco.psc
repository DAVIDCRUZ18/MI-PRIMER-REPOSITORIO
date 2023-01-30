Algoritmo cuadro_asterisco
	Definir a,b,n Como Entero
	Escribir "Escribe un número"
	Leer n
	Para a = 1 Hasta n Hacer
		Para b = 1 hasta n Hacer
			si a > 1 y a < n y b > 1 y b < n Entonces
				Escribir "   " Sin Saltar
			SiNo
				Escribir "*  " Sin Saltar
			FinSi
		FinPara
		Escribir "   "
	FinPara
FinAlgoritmo

