import numpy as np

mA = np.random.randint(1, 11, size=(3, 3))

mB = np.random.randint(11, 31, size=(3, 3))

mC = np.random.randint(-10, 0, size=(3, 3))

print("Matriz A:")
print(mA)
print()

print("Matriz B:")
print(mB)
print()

print("Matriz C:")
print(mC)
print()

msuma = mA + mB
resultado1 = np.dot(msuma, mC)

print("Suma de (A + B):")
print(msuma)
print()

print("Multiplicación de (A + B) · C:")
print(resultado1)
print()

resultado2 = np.dot(mA, mC)

print("Multiplicación de A · C:")
print(resultado2)
print()

resultado3 = np.dot(mB, mC)

print("Multiplicación de B · C:")
print(resultado3)
print()
msuma2= resultado2 + resultado3
print("Suma de A · C + B · C: ")
print(msuma2)
print()
if np.array_equal(resultado1, resultado2 + resultado3):
    print("(A + B) · C = A · C + B · C es verdadera.")
else:
    print("(A + B) · C = A · C + B · C es falsa.")
