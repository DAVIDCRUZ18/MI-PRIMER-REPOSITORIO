"""
    Script para explicar el manejo de excepciones en Python
"""
import sys

# 1. Try-except

def reciproco(milista):
    """Retorna el reciproco de cada numero de una lista de numeros.
    Parametros:
    milista: Lista de numeros
    Retorna:

    Lista con los reciprocos
    """
    for num in milista:
        try:
            print("Número:", num)
            r = 1/num
            print("El reciproco de {}, es: {}".format(num,r))
        except:
            print("Oops!",sys.exc_info()[0]," ocurrio.")

milistaNumeros = [3, 0, "a", 4 ,5]
reciproco(milistaNumeros)