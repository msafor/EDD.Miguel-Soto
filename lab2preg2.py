import random
filas= input("Ingrese la cantidad de filas de la matriz: ")
columnas= input("Ingrese la cantidad de columnas de la matriz: ")
filas = int(filas)
columnas = int(columnas)
#Genera la matriz aleatoria
m1= [[random.randint(0,10) for i in range(filas) for j in range(columnas)]]
#La idea es imprimir la matriz
for i in range(filas):
    for j in range(columnas):
        print(f"La matriz generada es {m1[filas][columnas]}")
escalar= int(input("Ingrese un escalar: "))
#La idea es multiplicar la matriz ccon el escalar
multiplicacion= [[m1*escalar[filas]*escalar[columnas]]]