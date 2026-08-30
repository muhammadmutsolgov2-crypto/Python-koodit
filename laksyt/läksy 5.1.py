import random

maara = int(input("Syötä arpakuutioiden lukumäärä: "))
summa = 0

for _ in range(maara):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print(f"Silmälukujen summa: {summa}")