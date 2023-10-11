from dog_exception import DogException


class Animal:
    def __init__(self):
        self.number_of_nose = 1

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        self.number_of_legs = 4
        super().__int__()

    @property
    def number_of_legs(self):
        return self.number_of_legs

    @number_of_legs.setter


    def walk(self):
        print(f"walking with {self.number_of_legs}")

    def eat(self):
        print("eating")

    def walk(self):
        print("walking")


class Fish(Animal):
    def swim(self):
        print("swimming")

    def eat(self):
        print("eating")
