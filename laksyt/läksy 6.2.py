import random


def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


# Pääohjelma
maksimi = int(input("Syötä nopan tahkojen yhteismäärä: "))

tulos = 0
while tulos != maksimi:
    tulos = heita_noppaa(maksimi)
    print(f"Heiton tulos: {tulos}")