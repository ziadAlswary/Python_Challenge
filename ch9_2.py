from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def say_the_type(self):
        pass

class Cat(animal):
    def say_the_type(self):
        print("it is a cat ")

class Dog(animal):
    def say_the_type(self):
        print("it is a dog")

c = Cat()
d = Dog()

c.say_the_type()

d.say_the_type()
