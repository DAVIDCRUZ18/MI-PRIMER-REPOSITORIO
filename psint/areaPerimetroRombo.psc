Algoritmo areaPerimetroRombo
	// 5)Mostrar el área y perímetro de un rombo.
	Definir lado1, diagonal1, diagonal2 Como Real
	Definir area, perimetro Como Real
	
	Escribir "Ingrese el un lado del rombo: "; Leer lado1
	Escribir "Ingrese la primera diagonal: "
	Leer diagonal1
	Escribir "Ingrese la segunda diagonal: "
	Leer diagonal2
	
	perimetro = lado1 * 4
	area = (diagonal1 * diagonal2) / 2
	
	Escribir "El area del rombo es: ", area
	Escribir "El perimetro del rombo es: ", perimetro
FinAlgoritmo
