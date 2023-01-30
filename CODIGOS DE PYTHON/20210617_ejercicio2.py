# -*- coding: utf-8 -*-
"""
ejercicio 2 2021-06-17
"""

def calc_func(j,a1,b1,c1):
    total=a1*(j**2)+b1*j+c1
    return total
    
z1=int(input("ingrese el valor de z sub 1: "))
z2=int(input("ingrese el valor de z sub 2: "))
a=10
b=20
c=30

resul=calc_func(z1,a,b,c)
print("i ",z1," resultado: ",resul)
val_min=resul
val_max=resul

for i in range (z1+1,z2+1,1):
    resul=calc_func(i,a,b,c)
    print("i ",i," resultado: ",resul)
    if resul<val_min:
        val_min=resul
    if resul>val_max:
        val_max=resul

print("el valor minimo de la funcion fue: ",val_min)
print("el valor maximo de la funcion fue: ",val_max)