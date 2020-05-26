import animals 
import shapes

#Implementation of classes for various animals and shapes (10 classes each) to learn abstraction and encapsulation, public and private access specifiers in Python
print("Details of animals.....\n")
a1 = animals.Animal()
a1.set_kingdom("Mammal")
a1.set_lifespan("20")
a1.displaydetails()
print("\n")

d1 = animals.Dog()
d1.set_name()
d1.set_lifespan("20")
d1.displaydetails()
d1.animalProperty()
print("\n")

liz1 = animals.Lizard()
liz1.set_name()
liz1.set_lifespan("10")
liz1.displaydetails()
liz1.animalProperty()
print("\n")

b1 = animals.Butterfly()
b1.set_name()
b1.set_lifespan("2")
b1.displaydetails()
b1.animalProperty()
print("\n")

monkey1 = animals.Monkey()
monkey1.set_name()
monkey1.set_lifespan("20")
monkey1.displaydetails()
monkey1.animalProperty()
print("\n")

cat1 = animals.Cat()
cat1.set_name()
cat1.set_lifespan("10")
cat1.displaydetails()
cat1.animalProperty()
print("\n")

camel1 = animals.Camel()
camel1.set_name()
camel1.set_lifespan("17")
camel1.displaydetails()
camel1.animalProperty()
print("\n")

peacock1 = animals.Peacock()
peacock1.set_name()
peacock1.set_lifespan("10")
peacock1.displaydetails()
peacock1.animalProperty()
print("\n")

crow1 = animals.Crow()
crow1.set_name()
crow1.set_lifespan("10")
crow1.displaydetails
crow1.animalProperty()
print("\n")

v1 = animals.Vulture()
v1.set_name()
v1.set_lifespan("10")
v1.displaydetails()
v1.animalProperty()
print("\n")

l1 = animals.Lion()
l1.set_name()
l1.set_lifespan("25")
l1.displaydetails()
l1.animalProperty()
print("\n")


print("Printing shapes classes details....\n")

e1 = shapes.Equilateral()
e1.set_name()
e1.get_name()
print("side is ", end="")
e1.get_side()
print("\n")


t1 = shapes.Triangle()
t1.set_name()
t1.get_name()
print("side is ", end="")
t1.get_side()
print("\n")

p1 = shapes.Pentagon()
p1.set_name()
p1.get_name()
print("side is ", end="")
p1.get_side()
print("\n")


h1 = shapes.Hexagon()
h1.set_name()
h1.get_name()
print("side is ", end="")
h1.get_side()
print("\n")


h = shapes.Heptagon()
h.set_name()
h.get_name()
print("side is ", end="")
h.get_side()
print("\n")


o1 = shapes.Octagon()
o1.set_name()
o1.get_name()
print("side is ", end="")
o1.get_side()
print("\n")


r1 = shapes.Rectangle()
r1.set_name()
r1.get_name()
print("side is ", end="")
r1.get_side()
print("\n")


s1 = shapes.Square()
s1.set_name()
s1.get_name()
print("side is ", end="")
s1.get_side()
print("\n")


ell1 = shapes.Ellipse()
ell1.set_name()
ell1.get_name()
ell1.set_params(40, 80)
print("Area is ", end="")
ell1.get_area()
print("\n")


c1 = shapes.Circle()
c1.set_name()
c1.get_name()
c1.set_radius(20)
print("Area is ", end="")
c1.get_area()
print("\n")
