'''Ejemplos Diccionarios'''

#Ejemplo diccionario de un elemento
diccionario = {"A":"Un elemento"}
print(diccionario)

#Ejemplo diccionario de dos elemento
diccionario = {"A":"Un elemento", "B":"Dos elemento"}
print(diccionario)

#Ejemplo diccionario con varios elementos e impresión por elemento
diccionario = {"nombre":"carlos", "edad":22, "Cursos":["python", "Django"]} 
print(diccionario)
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["Cursos"])

#Comparación del ejercicio anterior con una lista
lista1 = ["nombre", "carlos", "edad", 22, "cursos", ["python","Django"]]
print(lista1)
print(lista1[1])
print(lista1[3])
print(lista1[5])

#Ejemplo del uso de diccionarios con algunos paises y sus capitales
diccionarioCapitales = {
                        "España":"Madrid",
                        "Inglaterra":"Londres",
                        "Colombia":"Bogota",
                        "Argentina":"Buenos aires",
                        "Ecuador":"Quito"
                        }

print("la capital de españa es: ", diccionarioCapitales["España"])
print("Algunas de las capitales del mundo son: ", diccionarioCapitales)

#Ejemplo comparaciones y funciones con diccionarios
comparacion = diccionario == diccionarioCapitales
print("¿Diccionario es igual a diccionario capitales?: ", comparacion)

#Agregar un valor de otro diccionario y/o cambiar un valor
diccionarioNuevo = {"Colombia":diccionarioCapitales["Colombia"]}    
print(diccionarioNuevo)
diccionarioNuevo["Colombia"] = 20
print(diccionarioNuevo)

#Funciones con diccionarios
print(len(diccionarioNuevo))    #Tamaño del diccionario
print(len(diccionarioCapitales))

print(diccionarioNuevo.keys())  #Muestra las llaves del diccionario
print(diccionarioCapitales.keys())  
print(diccionarioNuevo.values())    #muestra los valores del diccionario
print(diccionarioCapitales.values())

diccionarioNuevo.clear()    #Eliminar los elementos que hay en el diccionario
print(diccionarioNuevo)
#diccionarioNuevo.del()  #Elimina el diccionario por completo
#print(diccionarioNuevo)  #Genera un error ya que el diccionarioNuevo fue eliminado 
diccionarioNuevo.update(diccionarioCapitales)
print(diccionarioNuevo)


#Ejemplos de un diccionario con valores númericos y funciones númericas 
diccionarioNumerico = {"valor1":int(10),"valor2":int(3),"valor3":int(16)}
print(max(diccionarioNumerico))
print(min(diccionarioNumerico))
print(max(diccionarioNumerico.values()))
print(min(diccionarioNumerico.values()))
diccionario = diccionarioNumerico.copy()
print(diccionario)

#Ejemplo recorriendo diccionarios con for
for k in diccionarioCapitales:
        print(k.upper())  #Convierte a mayuscula los elementos del diccionario

for k in diccionarioCapitales:
        print(k.lower()) #Convierte a minuscula los elementos del diccionario


