# 2. Filtrando por tipo de excepción
#En el ejemplo anterior, no mencionamos ninguna excepción en la cláusula except.
#Esta no es una buena práctica de programación, ya que detectará todas las excepciones y manejará todos los casos 
#de la misma manera. Podemos especificar qué excepciones capturará una cláusula except.

def reciproco2(milista):
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
        except TypeError:
            print("La división se realiza entre números")
        except ZeroDivisionError:
            print("Las divisiones por cero no estan permitidas")
        except:
            pass #Operación núla, nada sucede
        
milistaNumeros = [3, 0, "a", 4 ,5]
reciproco2(milistaNumeros)