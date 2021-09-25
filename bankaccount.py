class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        print("New account successfully created!")
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! New balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print(f"Insufficient funds in account! $5 penalty will be assessed! \n New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def display_account_info(self):
        print(f"Current account balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def yield_interest(self):
        ydInt = self.balance*self.int_rate
        self.balance += ydInt
        print("$"+"%.2f"%ydInt,end="")
        print(" interest added!")
        return self

acct1 = BankAccount(0.03, 3000)
acct2 = BankAccount(0.025, 2200)
acct1.deposit(200).deposit(200).deposit(100).withdraw(750).yield_interest().display_account_info()
acct2.deposit(300).deposit(1000).withdraw(150).withdraw(200).withdraw(50).withdraw(400).yield_interest().display_account_info()