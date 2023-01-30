'''Ejemplo funciones simples, con uno, dos y tres argumentos'''

def ejemplo():
        print("Soy una funcion sin argumentos")

def ejemplosuma(a,b):
        suma=a+b
        return suma

def ejemplomult(a,b,c):
        mult=a*b*c
        return mult

def ejemplovariasoperaciones(a,b,c):
        suma=a+b+c
        resta=a-b-c
        mult=a*b*c
        return (suma,resta,mult)

ejemplo()
print(ejemplosuma(2,3))
print(ejemplomult(2,5,10))
print(ejemplovariasoperaciones(100,20,35))

