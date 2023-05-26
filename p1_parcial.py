import numpy as np

mA = np.random.randint(0, 11, size=(4, 4))
mB = np.random.randint(0, 11, size=(4, 4))
mC = np.random.randint(0, 11, size=(4, 4))

mAcubo = np.power(mA, 3)
MinvB = np.linalg.inv(mB)
resultado = np.dot(np.dot(mAcubo, MinvB), mC) + np.linalg.inv(mAcubo)
print("Matriz A:")
print(mA)
print("Matriz B:")
print(mB)
print("Matriz Acubo")
print(mAcubo)
print("Matriz C:")
print(mC)
print("Matriz resultante:")
print(resultado)
