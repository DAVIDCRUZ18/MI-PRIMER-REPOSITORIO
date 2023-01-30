'''Ejemplo recibir parametro y devolver diccionario con las apariciones'''

dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1	

for campo,valor in dict.items():
	print (campo,"->",valor)
