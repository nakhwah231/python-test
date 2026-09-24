class Kampus:
    nama = "uim"
    alamat = "madinah"

class Mahasiswa:
    nim = 123
    name = "budi"

    def perkenalan(self): #(self) referensi pd semua obj yg di mahasiswa
        print(f"halo nama saya: {self.name}")

kampus1 = Kampus()
print(type(kampus1))

mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()

# mahasiswa1.nim = 1234
mahasiswa1.name = "ali"
print(type(mahasiswa1))
print(mahasiswa1.nim)
print(mahasiswa1.name)
print(mahasiswa2.nim)
print(mahasiswa2.name)
print(mahasiswa2.perkenalan())