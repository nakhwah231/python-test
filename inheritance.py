#parent
class Kendaraan:  # parent class/ sub class
    def __init__(self, merk, thn):
        self.merk = merk 
        self.thn = thn

    def info(self):
        return f"kendaraan {self.merk}, thn: {self.thn}"

    def nyalakan(self):
        print(f"{self.info()} dinyalakan!")
#child
class Mobil(Kendaraan): # child class/ sub class
    def __init__(self, merk, thn, jumlah_roda):
        super().__init__(merk, thn)
        self.jumlah_roda = jumlah_roda

    def info(self):
        return f"{super().info()} dan rodanya ada: {self.jumlah_roda}"

    def klakson(self):
        print(f"mobil {self.info()} memiliki klakson")

class Motor(Kendaraan):
    def klakson(self):
        print(f"motor {self.info()} memiliki klakson")

    def nyalakan(self):
        dasar = super().info() #overriding
        print(f"{dasar} otomatis menyala!")

avanza = Mobil("avanza", 2003, 4)
avanza.nyalakan()
avanza.klakson()
print(avanza.jumlah_roda)
honda = Motor("crf", 2000)
honda.klakson()
honda.nyalakan()