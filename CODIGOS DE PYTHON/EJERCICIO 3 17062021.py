h = float(input("Ingrese el valor de la hipoteca: "))
n = int(input("Ingrese los años en los que se va a pagar la hipoteca: "))
i = float(input("Ingrese el interés anual: "))

def calcularInteresMensual(): 
    r = i/(100*12)
    return r

dividendo = h*calcularInteresMensual()
divisor = 1-(1+calcularInteresMensual())**-(12*n)
m = dividendo / divisor

print("Valor cuota mensual",round(m,2))
