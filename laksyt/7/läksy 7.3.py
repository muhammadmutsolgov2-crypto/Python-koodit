lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Valintasi (1/2/3): ").strip()

    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ").strip().upper()
        nimi = input("Syötä lentoaseman nimi: ").strip()
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaa lentoasema: {lentoasemat[icao]}")
        else:
            print(f"ICAO-koodilla {icao} ei löytynyt lentoasemaa.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen.")