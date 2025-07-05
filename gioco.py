import random

numero = random.randint(1, 10)
tentativo = 0

print("Indovina il numero tra 1 e 10")

while tentativo != numero:
    tentativo = int(input("Scrivi un numero: "))

    if tentativo < numero:
        print("Troppo piccolo!")
    elif tentativo > numero:
        print("Troppo grande!")
    else:
        print("Hai indovinato!")
