class Vehicle:
    def __init__(self, company, year, feature):
        self.company = company
        self.year = year
        self.feature = feature

class Bicycle(Vehicle):
    def __init__(self, company, year, feature):
        super().__init__(company, year, feature)
        self.model = feature

    def info(self):
        print(f"Bicycle: {self.company}, Year: {self.year}, Model: {self.model}")
        
class Motorcycle(Vehicle):
    def __init__(self, company, year, feature):
        super().__init__(company, year, feature)
        self.cc = feature

    def info(self):
        print(f"Motorcycle: {self.company}, Year: {self.year}, cc: {self.cc}")

class Car(Vehicle):
    def __init__(self, company, year, feature):
        super().__init__(company, year, feature)
        self.seat = feature

    def info(self):
        print(f"Car: {self.company}, Year: {self.year}, Seat: {self.seat}")

validCmd = {"Bicycle", "Car", "Motorcycle", "print","stop"}
series = {}

while True:
    try:
        data = input().split()
    except EOFError:
        break

    if not data:
        continue

    cmd = data[0]
    if cmd not in validCmd:
        break
    else:
        if cmd == "Bicycle":
            series[data[1]] = Bicycle(data[1],data[2],data[3])
        elif cmd == "Car":
            series[data[1]] = Car(data[1],data[2],data[3])
        elif cmd == "Motorcycle":
            series[data[1]] = Motorcycle(data[1],data[2],data[3])
        elif cmd == "print":
            for obj in series.values():
                obj.info()
        elif cmd == "stop":
            break
        

        

    
