
class Shapes:
    def __init__(self):
        self._name = ''  # Protected member

    def get_name(self):
        print(self._name)


# Triangle
class Triangle(Shapes):
    def __init__(self):
        self._side = 3
        self._sideLength = 10
    # We can access protected members

    def set_name(self):
        self._name = 'Triangle'

    def get_side(self):
        print(self._side)


class Pentagon(Shapes):
    def __init__(self):
        self._side = 5
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Pentagon'

    def get_side(self):
        print(self._side)




class Hexagon(Shapes):
    def __init__(self):
        self._side = 6
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Hexagon'

    def get_side(self):
        print(self._side)




class Heptagon(Shapes):
    def __init__(self):
        self._side = 7
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Heptagon'

    def get_side(self):
        print(self._side)

   
class Octagon(Shapes):
    def __init__(self):
        self._side = 5
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Octagon'

    def get_side(self):
        print(self._side)



class Equilateral(Triangle):
    # We have access to protected members
    def set_name(self):
        self._name = 'Equilateral Triangle'

    def get_side(self):
        print(self._side)


# Circle


class Circle(Shapes):
    def __init__(self):
        self.__r = 0

    def set_name(self):
        self._name = 'Circle'

    def set_radius(self, r):
        self.__r = r

    def get_area(self):
        print(3.14 * (self.__r)**2)

    
# Ellipse


class Ellipse(Shapes):
    def __init__(self):
        self.__a = 0
        self.__b = 0

    def set_name(self):
        self._name = 'Ellipse'

    def set_params(self, a, b):
        self.__a = a
        self.__b = b

    def get_area(self):
        print(3.14 * self.__a * self.__b)

    def get_name(self):
        print(self._name)



# Rectangle


class Rectangle(Shapes):
    def __init__(self):
        self.__side = 4
        self.__a = 10
        self.__b = 20
    # We have access to protected members

    def set_name(self):
        self._name = 'Rectangle'

    def get_side(self):
        print(self.__side)

    

class Square(Rectangle):
    def __init__(self):
        self.sides = 4
        self.a = 10
    # We have access to protected members

    def set_name(self):
        self._name = 'Square'

    def get_side(self):
        print(self.sides)

    
