Algoritmo sin_titulo
	x,N,vec, DM, resultado es Real
	
	Escribir "Defina el tamaño del vector"
	Leer N
	Dimension vec[N]
	Escribir "Escriba una serie de números"
	
	Para x<-0 Hasta N-1 Con Paso 1
		Leer vec[x]
		
	FinPara
	Para x=0 Hasta n-1 Con Paso 1 Hacer
		resultado=cm(vec[x],x)
	FinPara
	Escribir resultado
	
FinAlgoritmo

Funcion retorno <- cm(DM,nm)
	Definir retorno,X,nota_mayor Como Real
	X=0
	Si DM > X Entonces
		X = DM
		
	FinSi
	Escribir DM
	
	
	
//	si nm == 0 Entonces
//		retorno = DM
//		
//	SiNo
//		
//		si DM > retorno Entonces
//			retorno = DM
//		FinSi
//		
//		
//		
//	FinSi
	
	
//	Para z<-0 Hasta N-1 Con Paso 1
//		vec1[z]=DM
//		retorno=vec1[z]
//		Si z=N-1 Entonces
//			retorno=vec1[z]
//			
//		FinSi
//		
//	FinPara
	
FinFuncion
