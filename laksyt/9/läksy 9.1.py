class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus:s}")
print(f"Huippunopeus: {uusi_auto.huippunopeus:d} km/h")
print(f"Tämänhetkinen nopeus: {uusi_auto.tamanhetkinen_nopeus:d} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka:d} km")