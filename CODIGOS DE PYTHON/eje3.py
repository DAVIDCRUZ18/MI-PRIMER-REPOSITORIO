frase = input("Digite una frase: ")

contador = 0;
for i in frase:
    if(i == " "):
        contador += 1
contador += 1

print("Cantidad de palabras en la frase es: ", contador)     