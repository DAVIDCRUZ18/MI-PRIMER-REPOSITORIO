'''Ejemplo 2 ciclo while'''

numero=int(input("ingrese un numero entre 0 y 20: "))
while numero < 0 or numero>20:
        numero=int(input("ingrese un numero entre 0 y 20: ")) 

print("El número es: ", numero)