palabra = input("Ingresa la palabra: ")
palabra = palabra.lower()
contadorA= 0
contadorE= 0
contadorI= 0
contadorO= 0
contadorU= 0
for letra in palabra:
    if letra == "a":
        contadorA += 1
    elif letra == "e":
        contadorE += 1
    elif letra == "i":
        contadorI += 1
    elif letra == "o":
        contadorO += 1
    elif letra == "u":
        contadorU += 1  
print(f"La palabra {palabra} tiene esta cantidad de vocales:")
print(f"Tiene {contadorA} A")
print(f"Tiene {contadorE} E")
print(f"Tiene {contadorI} I")
print(f"Tiene {contadorO} O")
print(f"Tiene {contadorU} U")
