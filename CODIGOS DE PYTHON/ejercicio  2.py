'''Diseña un algoritmo que calcule el IVA (16%) 
  de un producto dado su precio de venta sin IVA
'''

#Entradas
precio_producto=float(input("Ingrese el precio del producto: $"))

#Procedimiento
iva=precio_producto*0.16
precio_iva=precio_producto+iva

#Salidas
print("El precio del producto con IVA(16%): $", round(precio_iva,2))
print("El IVA del producto: $", iva)