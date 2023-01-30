# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:09:28 2021

@author: Acer
"""

n=int(input("digite el primer valor: "))
m=int(input("digite el segundo valor: "))

for i in range (n,n*m+1,1):
        if ((n*i)%n==0):
                print(n*i," es multiplo de ", n)
