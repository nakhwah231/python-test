# independent
class Mtk:

    @staticmethod
    def tambah(a, b):
        return a + b
    
result = Mtk.tambah(1, 3)
print(result)

# class methods
class BankAcc:
    no = ""
    balance = 0
    active = True

    def __init__(self, no, balance=0): 
        self.no = no
        self.balance = balance

    @classmethod
    def disabled(cls, no, balance):
        result = cls(no, balance)
        result.active = False
        return result

andi = BankAcc('123', -1000)
joko = BankAcc.disabled("3123", 2000)
print(f"pass: {andi.no}, balance: {andi.balance}, active: {andi.active}")
print(f"pass: {joko.no}, balance: {joko.balance}, active: {joko.active}")
print(BankAcc.no)

#getter& setter cr lama
class Items:
    _name = "" #class field private

    def set_name(self, name):
        if name == "":
            raise ValueError("items tidak boleh kosong")
        self._name = name

    def get_name(self):
        return self._name

item = Items()
item.set_name("laptop")
print(item.get_name()) #menampilkan hasil laptop, klo laptop di hapus maka dia akan error

# cara baru
class Category:
    _name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("pesanan tidak boleh kosong")
        self._name = name

category1 = Category()
category1.name = "kulkas"
print(category1.name)

#encapsulation
class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    def get_balance(self):
        return self.__balance

    def top_up(self, amount):
        self.__balance += amount

    def cash_out(self, amount):
        if self.__balance < amount:
            raise ValueError("saldo anda tidak cukup")
        self.__balance -= amount

andi = BankAccount("1")
andi.top_up(2000)  #balance
print(andi.get_balance())
andi.cash_out(500) #amount
print(andi.get_balance())
