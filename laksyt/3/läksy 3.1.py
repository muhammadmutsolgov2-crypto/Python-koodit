pituus = float(input("Anna kuhan pituus senttimetreinä: "))
SALLITTU_MITTA = 37

if pituus < SALLITTU_MITTA:
    puuttuu = SALLITTU_MITTA - pituus
    print(f"Laske kuha takaisin järveen! Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun mitan mukainen, voit pitää sen!")