class Bank:
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        if amount < self.money:
            self.money -= amount
        else:
            print("Insufficient funds")
    def balance(self):
        print(self.money)

accounts = {}
while True:
    data = input().split()
    cmd = data[0]
    if cmd == "stop":
        break
    elif cmd == "create":
        accounts[data[1]] = Bank(data[1],int(data[2])) 
    elif cmd == "deposit":
        if data[1] not in accounts:
            print("Account not found")
        else:
            accounts[data[1]].deposit(int(data[2]))
    elif cmd == "withdraw":
        if data[1] not in accounts:
            print("Account not found")
        else:
            accounts[data[1]].withdraw(int(data[2]))
    elif cmd == "balance":
        if data[1] not in accounts:
            print("Account not found")
        else:
            accounts[data[1]].balance()