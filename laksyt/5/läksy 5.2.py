luvut = []

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen luku.")

luvut.sort(reverse=True)

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in luvut[:5]:
    print(luku)