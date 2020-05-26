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

    # getters

    def __get_kingdom(self):  # private member function
        print("Animal Kingdom is " + self.__kingdom)

    def __get_name(self):  # private member function
        print("Animal name is " + self.name)

    def __get_lifespan(self):  # private member function
        print("Lifespan is " + self._lifespan)

    def displaydetails(self):  # public member function
        self.__get_kingdom()
        self.__get_name()
        self.__get_lifespan()

# Derived classes


class Dog(Animal):

    def set_name(self):
        self.name = "Dog"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    def animalProperty(self):
        print("Dog Barks")


class Lizard(Animal):
    def set_name(self):
        self.name = "Lizard"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    def animalProperty(self):
        print("Lizard crawls")


class Butterfly(Animal):
    def set_name(self):
        self.name = "Butterfly"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Butterflies are beautiful")


class Monkey(Animal):
    def set_name(self):
        self.name = "Monkey"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Monkeys Jumps a alot")


class Cat(Animal):
    def set_name(self):
        self.name = "Cat"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Cat drinks Milk")


class Camel(Animal):
    def set_name(self):
        self.name = "Camel"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Camels usually found in desert")


class Peacock(Animal):
    def set_name(self):
        self.name = "Peacock"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    def animalProperty(self):
        print("Peacock is a bird")


class Crow(Animal):
    def set_name(self):
        self.name = "Crow"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Crows are black")


class Vulture(Animal):
    def set_name(self):
        self.name = "Vulture"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    def animalProperty(self):
        print("Vulture eats carrion")


class Lion(Animal):
    def set_name(self):
        self.name = "Lion"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan


    def animalProperty(self):
        print("Lion is king")
