# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:03:55 2021

@author: Acer
"""

n=int(input("digite el primer valor: "))
m=int(input("digite el segundo valor: "))

for i in range(n,n*m+1,1):
        print("la multiplicacion de ", n, " por ", i, " es : ", n*i)
