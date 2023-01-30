#4. Levantando excepciones
# En Python, se generan excepciones cuando se producen los errores correspondientes en tiempo de ejecución.
# Nosotros tambien podemos levantar de forma forzada las excepciones utilizando la palabra clave raise.
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")

except ValueError as ve:
    print(ve)