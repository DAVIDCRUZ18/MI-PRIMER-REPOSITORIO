# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:15:21 2021
realizar un programa que comprueba si una cadena leida por 
teclado comienza por una subcadena introducida por teclado
@author: Acer
"""
#entrada
primera_cadena=input('ingrese una cadena de caracteres: ')#hola amiguitos
subcadena=input("ingrese la subcadena a buscar: ")#hola
control=0
#proceso
for i in subcadena:
        if(i in primera_cadena):
                control+=1
            
if (control==len(subcadena)):
        print("la primera cadena si comienza por la subcadena")
else:
        print("la primera cadena no comienza por la subcadena")
        
        

