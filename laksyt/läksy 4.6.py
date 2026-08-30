import random

N = int(input("Syötä arvottavien pisteiden kokonaismäärä: "))

n = 0
laskuri = 0

while laskuri < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1

    laskuri += 1

pii_likiarvo = 4 * n / N
print(f"Piin likiarvo: {pii_likiarvo}")