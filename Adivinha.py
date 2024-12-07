import random

numero = random.randint(1,100)

tentativas = 0

while tentativas < 3:
    tentativa = int(input("Indique um número entre (1-100)"))
    if tentativa == numero:
        print("Parabéns, acertou o número!")
        break
    elif tentativa < numero:
        print("Introduza um número maior")
        tentativas += 1
    else:
        print("Introduza um número menor")
        tentativas += 1