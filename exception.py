class BankAcc:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise ValueError("saldo tidak cukup!")
        self.balance -= amount

try:
    bank_account = BankAcc("12415", 100)
    bank_account.transfer(1000)
except ValueError as e:
    print(f"error: {e}")
print("program selesai")