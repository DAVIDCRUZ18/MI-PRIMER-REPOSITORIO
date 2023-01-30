cantidad_invertir=float(input('Ingrese cantidad a invertir: ')) 
interes_anual=float(input('Ingrese interes anual: '))
Num_an= float(input('ingrese numero de años: '))
conv=interes_anual/100
C= cantidad_invertir*conv*Num_an
print("capital obtenido de la inversión es: $",C )