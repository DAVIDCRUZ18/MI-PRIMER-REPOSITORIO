
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
costoHora = int(input("Ingrese el precio de la hora de trabajo: "))

horasExtra = 0
pago = 0
horasAdicionales = 0
if horasTrabajadas <=40:
        pago = costoHora * horasTrabajadas   
elif horasTrabajadas>40 and horasTrabajadas<=48:
        horasExtra = horasTrabajadas - 40
elif  horasTrabajadas>48:       
        horasExtra = 8
        horasAdicionales = horasTrabajadas -48      
pago = ((horasTrabajadas-horasExtra)*costoHora) + (horasExtra * (costoHora*2)) + (horasAdicionales*(costoHora*3))

print ("El pago seria: ",pago )