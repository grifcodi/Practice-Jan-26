class Animal:
    def sound(self):
        return "Animals make sound! Amazing!"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(type(animal).__name__, ":", animal.sound())