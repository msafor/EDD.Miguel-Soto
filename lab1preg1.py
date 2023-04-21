import random
filas= input("Ingrese la cantidad de filas de la matriz: ")
columnas= input("Ingrese la cantidad de columnas de la matriz: ")
filas = int(filas)
columnas = int(columnas)
#Genera la matriz aleatoria
m1= [[random.randint(0,5) for i in range(filas) for j in range(columnas)]]
#La idea es imprimir la matriz
for i in range(filas):
    for j in range(columnas):
        print(f"La matriz generada es {m1[filas][columnas]}")

#Y aquí hacer lo mismo con la matriz2
m2= [[random.randint(0,5) for i in range(filas) for j in range(columnas)]]
for i in range(filas):
    for j in range(columnas):
        print(m2[filas][columnas])
#Y aquí estaria la suma de las dos matrices
suma= [[m1[filas][columnas]+m2[filas][columnas]]]
#Aqui se comenzaria a crear la tercera matriz
filam3= input("Ingrese la cantidad de filas de la matriz 3: ")
columnam3= input("Ingrese la cantidad de columnas de la matriz 3: ")
#Genera la matriz aleatoria
m3= [[random.randint(0,5) for i in range(filam3) for j in range(columnam3)]]
for i in range(filam3):
    for j in range(columnam3):
        print(f"La matriz generada es {m3[filam3][columnam3]}")
#Y aquí estaria la "resta" de las matrices
resta= [[suma[][]-m3[filam3][columnam3]]]