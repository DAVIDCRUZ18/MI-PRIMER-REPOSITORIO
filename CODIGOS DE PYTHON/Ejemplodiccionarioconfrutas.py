
#crea el diccionario
precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
#abre un ciclo infinito
while True:
    #solicita al usuario la fruta
    fruta = input("Dime la fruta que has vendido:")
    #si la fruta no esta en el diccionario precios
    if fruta.lower() not in precios:
        #imprime que no esta
        print("Fruta no existe.")
    # si la fruta esta en el diccionario
    else:
        #pide la cantidad vendida
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        #imprime el precio total de la venta
        print("El precio %f es de " % (cantidad * precios[fruta]))
    #pregunta al usuario si desea hacer otra venta
    opcion = input("¿Quieres vender otra fruta (s/n)")
    #hace un while hasta que la opcion dada por el usuario sea n o s
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    #si la opcion es n rompe el ciclo y finaliza el programa
    if opcion.lower() == "n":
        break
    #si no es n vuelve al ciclo
