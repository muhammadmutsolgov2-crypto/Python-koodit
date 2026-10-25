class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos

        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.tamanhetkinen_nopeus * tuntimaara



uusi_auto = Auto("ABC-123", 142)


uusi_auto.tamanhetkinen_nopeus = 60
uusi_auto.kuljettu_matka = 2000

uusi_auto.kulje(1.5)
print(f"Kuljettu matka metodikutsun jälkeen: {uusi_auto.kuljettu_matka:f} km")