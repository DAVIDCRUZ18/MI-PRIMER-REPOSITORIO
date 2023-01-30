# 3. Multiples excepciones en un mismo except.

def reciproco3(milista):
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
        except (TypeError,ZeroDivisionError):
            print("Error de tipo de dato o de divsión por zero")
        except:
            pass #Operación núla, nada sucede
        
milistaNumeros = [3, 0, "a", 4 ,5]
reciproco3(milistaNumeros)