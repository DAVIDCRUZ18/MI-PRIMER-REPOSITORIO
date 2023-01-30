# -*- coding: utf-8 -*-
"""
Elabora programa que calcule y escriba el precio de venta
para un articulo, se tiene, el nombre del producto y el costo
El precio de venta se calcula añadiendo el 120% como utilidad
y el 15% de impuesto
"""

nom_prod=input("ingrese el nombre del procucto: ")
cos_prod=float(input("ingrese el costo de produccion del producto: "))


def calcular(nom,costo):
    utilidad=costo*1.2
    impuesto=(utilidad+costo)*0.15
    total=utilidad+impuesto+costo
    return(total)
    
    
    
val_venta= calcular(nom_prod,cos_prod)

print("el valor de venta del producto ",nom_prod, " es: ", val_venta)
