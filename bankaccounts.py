class BankAccount:
    def __init__(self, firstName, lastName, accountId, accountType, pin, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.accountId = accountId
        self.accoutType = accountType
        self.pin = pin
        self.balance = int(balance)
        
    def deposit(self, toAdd):
        self.balance += toAdd
        print(f"{toAdd}$ deposited. New balance is {self.balance}$")
    
    def withdraw(self, toSub):
        self.balance -= toSub
        print(f"{toSub}$ withdrawn. New balance is {self.balance}$")
    
    def displayBalance(self):
        print(f"Your current balance is {self.balance}$")

myAccount = BankAccount("Dawid", "Czaplicki", "92471", "Personal", "1111", 600)

myAccount.deposit(96)
myAccount.withdraw(25)
myAccount.displayBalance()    