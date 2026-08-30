kaupungit = []

for _ in range(5):
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nSyötetyt kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)