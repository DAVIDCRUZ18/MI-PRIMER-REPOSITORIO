cadena = input("Por favor ingrese una frase: ")
caracter1 = "ab"
caracter2 = "cd"

while len(caracter1) != 1 or len(caracter2) != 1:
        print("Debe ingresar solo un caracter")
        caracter1 = input("Por favor ingrese el primer caracter: ")
        caracter2 = input("Por favor ingrese el segundo caracter: ")

print(cadena.replace(caracter1, caracter2))
