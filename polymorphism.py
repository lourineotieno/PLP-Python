
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🕊️"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
