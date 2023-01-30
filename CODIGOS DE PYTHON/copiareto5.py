#entradas

def inventario(tablaentrada):
    
    q=0
    for u in tablaentrada:
        q+=tablaentrada[u][1]*tablaentrada[u][2]
    return q

def promedio(tablaentrada):
    z=0
    for j in tablaentrada:
        z+=tablaentrada[j][1]
        z/=len(tablaentrada)
    return z

def preciomayor(tablaentrada):
    claves=list(tablaentrada.keys())
    mayor_precio=tablaentrada[claves[0]][1]
    nombre_mayor=tablaentrada[claves[0]][0]
    for n in tablaentrada:
        if tablaentrada[n][1]>mayor_precio:
            mayor_precio=tablaentrada[n][1]
            nombre_mayor=tablaentrada[n][0]
    return nombre_mayor

 
def preciomenor(tablaentrada):
    claves=list(tablaentrada.keys())
    menor_precio=tablaentrada[claves[0]][1]
    nombre_menor=tablaentrada[claves[0]][0]

    for n in tablaentrada:
        if tablaentrada[n][1]<menor_precio:
            menor_precio=tablaentrada[n][1]
            nombre_menor=tablaentrada[n][0]
    return nombre_menor

def agregardatos(tablaentrada,productoentrada):
    if productoentrada[0]in tablaentrada:
        return False
    else:
        h=productoentrada[0]
        productoentrada.pop(0)
        tablaentrada[h]=productoentrada
        return True

def BORRARDATOS(tablaentrada,productoentrada):
    if productoentrada[0]in tablaentrada:
        productoentrada.pop(productoentrada[0])
        return True
    else:
        return False

def ACTUALIZARDATOS(tablaentrada,productoentrada):
    if productoentrada[0]in tablaentrada:
        x=productoentrada[0]
        productoentrada.pop(0)
        tablaentrada[x]=productoentrada
        return True
    else:
        return False
def hacer():
    procedimiento=input()
    productoentrada=input().split()
    productoentrada[0]=int(productoentrada[0])
    productoentrada[2]=float(productoentrada[2])
    productoentrada[3]=int(productoentrada[3])
    return procedimiento,productoentrada

def productos():
    tablaentrada={1:["manzanas",6000.0, 25],
                    2:["Limones",2900.0, 555],
                    3:["Peras",2700.0, 33],
                    4:["Arandanos",9300.0, 34],
                    5:["Tomates",2100.0, 42],
                    6:["Fresas",4100.0, 10],
                    7:["Helado",4500.0, 41],
                    8:["Galletas",500.0, 8],
                    9:["Chocolates",4600.0,999],
                    10:["Jamon",15000.0, 10],}

    procedimiento,productoentrada=hacer()
    if procedimiento == "AGREGAR":
        LOQSEA=agregardatos(tablaentrada,productoentrada)
    elif procedimiento == "BORRAR":
        LOQSEA=BORRARDATOS(tablaentrada,productoentrada)
    elif procedimiento == "ACTUALIZAR":
        LOQSEA=ACTUALIZARDATOS(tablaentrada,productoentrada)
    if LOQSEA:
        print(preciomayor(tablaentrada),
             preciomenor(tablaentrada),
             round(promedio(tablaentrada),1),
             round(inventario(tablaentrada),1))

productos()