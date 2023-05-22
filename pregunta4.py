import random

def crearmatrizaleatoria(n):
    matriz = []
    for _ in range(n):
        fila = [random.randint(1, 10) for _ in range(n)]
        matriz.append(fila)
    return matriz
def impmatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()
def metodogauss(matriz):
    num = len(matriz)
    for i in range(num):
        if matriz[i][i] == 0:
            for j in range(i + 1, num):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break
        rest = matriz[i][i]
        if rest != 0:
            for j in range(num * 2):
                matriz[i][j] /= rest
            for j in range(num):
                if j != i:
                    cofmul = matriz[j][i]
                    for k in range(num * 2):
                        matriz[j][k] -= cofmul * matriz[i][k]
    return matriz
def tenerinv(matrizamp):
    num = len(matrizamp)
    matrizinv = [[matrizamp[i][j] for j in range(num, num * 2)] for i in range(num)]
    return matrizinv
tamañom = random.randint(3, 5)
matrizori = crearmatrizaleatoria(tamañom)
matrizampliada = []
for i in range(tamañom):
    fila = matrizori[i] + [1 if j == i else 0 for j in range(tamañom)]
    matrizampliada.append(fila)
matrizampt = metodogauss(matrizampliada)
matrizinv = tenerinv(matrizampt)
print("Matriz original:")
impmatriz(matrizori)
print("Matriz inversa:")
impmatriz(matrizinv)