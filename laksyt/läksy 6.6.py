import math


def laske_yksikköhinta(halkaisija_cm, hinta_eur):
    säde_m = (halkaisija_cm / 100) / 2
    pinta_ala_m2 = math.pi * (säde_m ** 2)
    return hinta_eur / pinta_ala_m2


def pääohjelma():
    print("--- Pizza 1 ---")
    halkaisija1 = float(input("Syötä 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä 1. pizzan hinta (€): "))

    print("\n--- Pizza 2 ---")
    halkaisija2 = float(input("Syötä 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä 2. pizzan hinta (€): "))

    yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)
    yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)

    print(f"\n1. pizzan yksikköhinta: {yksikköhinta1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {yksikköhinta2:.2f} €/m²\n")

    if yksikköhinta1 < yksikköhinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikköhinta2 < yksikköhinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat tarjoavat yhtä hyvän vastineen rahalle.")
pääohjelma()