Algoritmo contador_de_numeros
	Definir numax,numin,num,contador Como Entero
	Escribir "Define el valor m�ximo del rango"
	Leer numax
	Escribir "Define el valor m�nimo del rango"
	Leer numin
	Escribir "Escriba un numero dentro del rango"
	Leer num
	contador=0
	Mientras num < numax Y num > numin
		Escribir "Escriba un numero dentro del rango"
		Leer num
		contador= contador+1
	FinMientras
	Escribir "La cantidad de n�meros digitados son: ",contador
FinAlgoritmo
