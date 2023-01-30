"""Una panaderia vende barras de pan a 3.49"""

#ENTRADAS

barras_vencidas = int(input("Ingrese el numero de barras vencidas: "))
descuento = int(input("Ingrese el descuento a aplicar:  "))

#CALCULOS

precio_habitual = 3.49
descuento_porcentaje = descuento / 100
valor_descuento = round((precio_habitual * descuento_porcentaje),1)
costo_final = round((precio_habitual - valor_descuento),1)

#SALIDAS      

print ("El precio de una barra habitual es de: ", precio_habitual)
print ("El descuento que se hace por no ser fresca es de:", valor_descuento)
print ("El costo final de la barra es de", costo_final)

#tipo de datos
print ("barras_vencidas", type(barras_vencidas))
print ("descuento", type(descuento))
print ("precio_habitual", type(precio_habitual))
print ("descuento_porcentaje", type(descuento_porcentaje))
print ("valor_descuento", type (valor_descuento))
print ("costo_final", type(costo_final))            