import numpy

def sumamatrices(m1, m2):
    if m1.shape != m2.shape: #usé .shape para ver si las matrices tenian las mismas dimensiones 
        return None
    else:
        return numpy.add(m1, m2)
filas1 = int(input("Ingrese la cantidad de filas de la primera matriz: "))
columnas1 = int(input("Ingrese la cantidad de columnas de la primera matriz: "))
m1 = numpy.zeros((filas1, columnas1))
def restamatrices(m1, m22):
    if m1.shape != m2.shape:
        return None
    else:
        return numpy.subtract(m1, m2)
for i in range(filas1):
    for j in range(columnas1):
        datos = float(input("Ingrese el elemento ({},{}) de la matriz: ".format(i+1, j+1)))
        m1[i][j] = datos

print("La matriz creada es:")
print(m1)
filas2 = int(input("Ingrese la cantidad de filas de la segunda matriz: "))
columnas2 = int(input("Ingrese la cantidad de columnas de la segunda matriz: "))
m2 = numpy.zeros((filas2, columnas2))

for i in range(filas2):
    for j in range(columnas2):
        datos2 = float(input("Ingrese el elemento {}.{} de la matriz: ".format(i+1, j+1)))
        m2[i][j] = datos2

print("La matriz creada es:")
print(m2)
matriz_suma = sumamatrices(m1, m2)
if matriz_suma is None:
    print("Las matrices no se pueden sumar porque tienen dimensiones diferentes")
else:
    print("El resultado de la suma de las matrices es:")
    print(matriz_suma)
matriz_resta = restamatrices(m1, m2)
if matriz_resta is None:
    print("Las matrices no se pueden restar porque tienen dimensiones diferentes")
else:
    print("El resultado de la resta de las matrices es:")
    print(matriz_resta)