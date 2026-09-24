# tanpa constructor
class Mahasiswa:
    num = 0  #public 
    name = ""
    
    def perkenalan(self, nim, name):
        self.num = nim
        self.name = name
        
mh = Mahasiswa()
mh.perkenalan("123", "alice")

print(mh.name)
print(mh.num)

# constructor
class Siswa:
    name = ""
    nim = 0

    def __init__(self, name, nim):
        self.name = name #state
        self.nim = nim  #state
    
    def __str__(self):  #behavior
        return f"nama saya: {self.name}, nim: {self.nim}"

    def __eq__(self, other):  #behavior
        return self.name == other.name and self.nim == other.nim
    
mhs1 = Siswa("budi", 23)
mhs2 = Siswa("budi", 23)
print(mhs1.name)
print(mhs1.nim)
print(f"mahasiswa : {mhs1}")
print(f"hasilnya: {mhs2 == mhs1}")

# constructor raise
class BankAccount:
    def __init__(self, no, saldo=0): #default param
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self.no = no
        self.saldo = saldo

budi = BankAccount("937849", 1000)
joko = BankAccount("938949", -1000)

print(budi.saldo)