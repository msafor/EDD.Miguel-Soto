import numpy as np

Matriz = np.array([[5, 3, 1],
              [7, 2, 5],
              [2, 5, 7]])
Matrizinv = np.linalg.inv(Matriz)
producto = np.dot(Matriz, Matrizinv)
I = np.allclose(producto, np.eye(Matriz.shape[0]))
if I:
    print("La propiedad A * A^(-1) = I se cumple.")
else:
    print("La propiedad A * A^(-1) = I no se cumple.")