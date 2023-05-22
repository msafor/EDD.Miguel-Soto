matriz = [[3, 4, 2, 7, 5],
          [2, 3, 3, 8, 3],
          [7, 5, 3, 2, 1],
          [2, 5, 2, 9, 2],
          [3, 1, 2, 4, 9]]
sumacolumnas = [sum(fila[i] for fila in matriz) for i in range(len(matriz[0]))]
sumamaximacolumna = max(sumacolumnas)
print(f"Suma más alta entre las columnas: {sumamaximacolumna}")
sumafilas = [sum(fila) for fila in matriz]
sumaminimafilas = min(sumafilas)
print(f"Suma más baja entre las filas: {sumaminimafilas}")