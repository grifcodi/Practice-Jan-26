class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f'{self.brand} {self.year} {self.mileage}'

    def info(self):
        print(f"Car brand: {self.brand}, year of release: {self.year}, current mileage: {self.mileage}")

    def drive(self, kilometers):
        self.mileage += kilometers
