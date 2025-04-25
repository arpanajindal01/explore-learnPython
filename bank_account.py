class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise  ValueError("Balance cannot be negative")
        self.__balance = new_balance


    def deposit(self, amount):
        if amount <= 0:
            raise  ValueError("Deposit amount cannot be zero or negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise  ValueError("Withdraw cannot be zero or negative")
        if amount > self.balance:
            raise ValueError("Not enough funds..!!!")
        self.balance -= amount


my_account = BankAccount()
my_account.deposit(1000)
print(f"Balance in the account is: {my_account.balance}")

my_account.withdraw(50)
print(f"Balance in the account after withdraw is: {my_account.balance}")

