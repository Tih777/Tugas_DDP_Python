# class
class Mobil:
    def __init__(self, merk, cc, warna):
        self.merk = merk
        self.cc = cc
        self.warna = warna

    def dekripsi(self):
        print("Merk mobil saya adalah ", self.merk , "CC nya adalah ", self.cc , "Warnanya adalah ", self.warna )

# objek
mobil1 = Mobil("Avanza", 1500, "Hitam")

mobil1.dekripsi()