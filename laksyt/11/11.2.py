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


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti 


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki  # litraa

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.muuta_nopeutta(120)
polttomoottoriauto.muuta_nopeutta(100)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"{sahkoauto.rekisteritunnus}: {sahkoauto.kuljettu_matka} km")
print(f"{polttomoottoriauto.rekisteritunnus}: {polttomoottoriauto.kuljettu_matka} km")