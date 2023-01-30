'''ejemplo para crear una baraja de cartas'''

valores = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
tipos = ["Corazon", "Trebol", "Espadas", "Diamantes"]
Baraja = []

for i in valores:
        for j in tipos:
                carta= "{} de {}".format(i,j)
                Baraja.append(carta)
print(Baraja)

#print(Baraja[10])
