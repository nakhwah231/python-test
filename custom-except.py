class BalanceNotEnough(Exception):
    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return self.massage

class BankAcc:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough("saldo di atm tidak mencukupi!")
        self.balance -= amount

try:
    bank_account = BankAcc("12415", 100)
    bank_account.transfer(1000)
except BalanceNotEnough as e:
    print(f"error: {e}")
print("program selesai")