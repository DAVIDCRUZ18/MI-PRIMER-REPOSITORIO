"""CALCULAR PRECIO DE VENTA"""

#entradas

nombre_producto=input("ingrese nombre del producto: ")
codigo_producto=input("ingrese codigo producto: ")
costo_produccion=float(input("ingrese costo produccion: "))

#procedimiento

valor_sin_impuesto=costo_produccion*1.2
impuesto=costo_produccion*0.15
valor_venta=costo_produccion+valor_sin_impuesto+impuesto

#salida

print("el  valor de venta del producto: ", nombre_producto," con codigo: ", codigo_producto, " es: $", )


