from random import randint

intentos = 0
num_probado = 0
numero_secreto = randint(1,100)
nombre = input("¿Cuál es tu nombre?: ")

print(f" {nombre}, adivina el número entre 1 y 100 que he elegido. Tienes 5 intentos.")

while intentos < 5:
    num_probado = int(input("\nDigita el número: "))
    intentos += 1

    if num_probado < numero_secreto:
        print("\tEl número es mayor.")
    elif num_probado > numero_secreto:
        print("\tMi numero es mas bajo.")
    else:
        print(f"\tFelicitaciones {nombre}! Has adivinado en {intentos} intentos.")
        break

if num_probado != numero_secreto:
    print(f"\tSe acabaron tus intentos. El número era: {numero_secreto}.")