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

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Lukuja ei syötetty.")