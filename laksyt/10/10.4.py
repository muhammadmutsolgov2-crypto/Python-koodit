import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def muuta_nopeutta(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus = pituus_km
        self.autot = autot

    def tunti_kuluu(self):

        for auto in self.autot:
            auto.muuta_nopeutta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10}{'Nopeus (km/h)':>15}{'Matka (km)':>14}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10}{auto.nopeus:>15}{auto.kuljettu_matka:>14}")

    def kilpailu_ohi(self):

        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"\nTilanne {tunnit} tunnin jälkeen:")
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättyi {tunnit} tunnin jälkeen. Lopputilanne:")
kilpailu.tulosta_tilanne()