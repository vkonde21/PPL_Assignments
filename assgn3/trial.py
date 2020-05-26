# Classes Based on Animals


class Animal:
    def __init__(self):
        # Private
        self.__kingdom = ""
        # Protected
        self._lifespan = ""
        # Public
        # name means which animal it is
        self.name = ""

    # setters
    def set_kingdom(self, kingdom):
        self.__kingdom = kingdom

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    def set_name(self):
        self.name = "Dog"

    # getters

    def get_kingdom(self):
        print("Animal Kingdom is " + self.__kingdom)

    def get_name(self):
        print("Animal name is " + self.name)

    def get_lifespan(self):
        print(self.name + " lifespan is " + self._lifespan)


# Derived classes
class Dog(Animal):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = "Dog"

    def get_name(self):
        print(self.name)

    def animalProperty(self):
        print("Dog Barks")


class Lizard(Animal):
    pass


class Butterfly(Animal):
    pass


class Monkey(Animal):
    pass


class Cat(Animal):
    pass


class Camel(Animal):
    pass



class Peacock(Animal):
    pass


class Crow(Animal):
    pass


class Vulture(Animal):
    pass


if __name__ == "__main__":
    a1 = Animal()
    a1.set_kingdom("Mammal")
    a1.get_kingdom()
    a1.get_lifespan()
    d = Dog()
    d.set_name()
    d.get_name()
    d.animalProperty()