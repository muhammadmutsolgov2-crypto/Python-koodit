def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


def pääohjelma():
    while True:
        gallona_määrä = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
        if gallona_määrä < 0:
            print("Ohjelma lopetettu.")
            break

        litrat = gallonat_litroiksi(gallona_määrä)
        print(f"{gallona_määrä} gallonaa on {litrat:.2f} litraa.\n")
pääohjelma()