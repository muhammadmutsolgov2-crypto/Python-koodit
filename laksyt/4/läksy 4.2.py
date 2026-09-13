while True:
    tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa): "))
    if tuumat < 0:
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {sentit:.2f} cm")