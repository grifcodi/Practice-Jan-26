class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage   # setter

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Mileage cannot be negative")
        self._mileage = value

    def drive(self, kilometers):
        if kilometers < 0:
            raise ValueError("Kilometers must be positive")
        self.mileage += kilometers

    def __str__(self):
        return f"{self.brand} ({self.year}), mileage: {self.mileage}"


class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # setter

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.balance -= amount





# car = Car('BMW', 2000, 5000)
# print(car.mileage)
# car.mileage = -20
# print(car.mileage)
# del car.mileage

acc = BankAccount(100)
print(acc.balance)
#acc.deposit(-20)
#print(acc.balance)
acc.withdraw(304)
print(acc.balance)