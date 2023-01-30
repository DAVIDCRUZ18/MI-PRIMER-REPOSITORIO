'''Ejemplos tuplas y listas'''

a=(1,2,3,4) #Se crea una tupla llamada a
b=[5,6,7,8] #Se crea una lista llamada b

print(type(a)) 
print(type(b))
print(a)
print(b)
print(a,b)
print(a[2]) #Imprime el objeto de la posición 2 de la tupla a
print(a[0],b[3]) #Imprime posiciones 0 y 3 de la tupla a y la lista b 
a=list(a) #Se convierte a de tupla a lista
c=a+b   #Se crea una lista c que contiene los elementos de a y b
print(c)
print(type(c))

e=[]  #Se crea una lista llamada e vacia

#Se utiliza un for para llenar una lista g con numeros del 2 al 5 
for i in a:
        d="{}".format(i+1)
        e.append(d)
print(e)

g=[]  #Se crea una lista llamada g vacia

#Se utiliza un for para llenar una lista g con numeros del 0 al 4
for i in range(0,5):
        f="{}".format(i)
        g.append(f)
print(g)      
