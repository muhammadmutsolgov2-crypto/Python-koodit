class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()
        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("PALOHÄLYTYS!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


talo = Talo(1, 6, 3)
talo.aja_hissia(2, 4)
talo.aja_hissia(1, 3)

talo.palohalytys()