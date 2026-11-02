import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autolista = autolista

    def tunti_kuluu(self, tunnit=1):
        for auto in self.autolista:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(tunnit)

    def tulosta_tilanne(self):
        print(f"\n--- Kilpailun tilanne: {self.nimi} ---")
        print(f"{'Rekisteri':<12} | {'Huippunopeus':<12} | {'Nopeus':<8} | {'Matka (km)':<10}")
        print("-" * 55)
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<12} | {auto.nopeus:<8} | {auto.matkamittari:<10.1f}")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matkamittari >= self.pituus_km:
                return True
        return False


autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippunopeus = random.randint(150, 200)
    autot.append(Auto(rekisteri, huippunopeus))

romuralli = Kilpailu("Suuri romuralli", 8000, autot)

tunteja = 0
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu(1)
    tunteja += 1
    if tunteja % 10 == 0:
        romuralli.tulosta_tilanne()

print("\nKILPAILU ON PÄÄTTYNYT! Lopputulokset:")
romuralli.tulosta_tilanne()