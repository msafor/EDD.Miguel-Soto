import numpy as np 
import random
filas = random.randint(2, 5)
columnas = random.randint(2, 5)
print("Ingrese los elementos de la primera matriz:")
matriz1 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz1.append(fila)
print("Ingrese los elementos de la segunda matriz:")
matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz2.append(fila)
resultadoresta = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = matriz1[i][j] - matriz2[i][j]
        fila.append(elemento)
    resultadoresta.append(fila)
print("La resta de las matrices es:")
for fila in resultadoresta:
    print(fila)   
print("Ingresar elementos de la tercera matriz:")
tercerafila = columnas  
terceracolumna = np.random.randint(2, 6)
matriz3 = []
for i in range(columnas):
    filas = []
    for j in range(terceracolumna):
        elemento = int(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        filas.append(elemento)
    matriz3.append(filas)
resultadorestaf = np.array(resultadoresta)
matriz3f = np.array(matriz3)
productofinal = np.dot(resultadorestaf, matriz3f)
propiedad1 = np.transpose(np.dot(matriz1, matriz3)) 
propiedad2 = np.dot(np.transpose(matriz3), np.transpose(matriz1))
print("Matriz resultante de la multiplicación:")
print(productofinal)
print("Comprobación de la propiedad de las matrices traspuestas:")
print("Propiedad 1: ")
print(propiedad1)
print("Propiedad 2: ")
print(propiedad2)
