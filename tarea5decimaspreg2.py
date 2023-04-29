import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1 = [[random.randint(0, 5) for j in range(columnas)] for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        print(m1[i][j], end=' ')
    print()
fila2 = int(input("Ingrese la cantidad de filas: "))
columna2 = int(input("Ingrese la cantidad de columnas: "))
m2 = [[random.randint(0, 5) for j in range(columna2)] for i in range(fila2)]

for i in range(fila2):
    for j in range(columna2):
        print(m2[i][j], end=' ')
    print()
def sumar_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return None
    m3 = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        m3.append(fila)
    return m3
def restar_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return None
    m3 = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])
        m3.append(fila)
    return m3
m3 = sumar_matrices(m1, m2)
if m3 is not None:
    print("La suma de las matrices es:")
    for fila in m3:
        print(fila)
    print()
else:
    print("No se pueden sumar las matrices porque son de diferentes dimensiones.")
    print()

m4 = restar_matrices(m1, m2)
if m4 is not None:
    print("La resta de las matrices es:")
    for fila in m4:
        print(fila)
    print()
else:
    print("No se pueden restar las matrices porque son de diferentes dimensiones.")
    print()