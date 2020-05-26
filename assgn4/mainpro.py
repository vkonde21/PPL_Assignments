# Implementation of classes for various animals and shapes (10 classes each) to learn concepts like virtual functions,  abstract classes, base class, derive class, interfaces, polymorphism , modularity and hierarchy in Python
import shapes
import animals 
import abstract

#s = abstract.Shape() This line gives an error since abstract classes cannot be instantiated
#A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.
#An abstract method can have an implementation in the abstract class! Even if they are implemented, designers of subclasses will be forced to override the implementation.
print("\n RECTANGLE\n")
r = shapes.Rectangle(100, 60)
r.printarea()
r.get_sides()
r.printperimeter()
r.draw()

print("\n SQUARE\n")
s = shapes.Square(4, 120)
s.printarea("square")
s.get_sides("square")
s.printperimeter("square")
s.diagonal()
s.draw()

print("\n EQUILATERAL TRIANGLE \n")
t = shapes.Triangle(3, 140)
t.printarea("equilateral triangle")
t.get_sides("equilateral triangle")
t.printperimeter("equilateral triangle")
t.draw()

print("\n RHOMBUS \n")
rh = shapes.Rhombus(50, 120)
rh.printarea()
rh.get_sides()
rh.printperimeter()
rh.draw()

print("\n PARALLELOGRAM \n")
p = shapes.Parallelogram(200, 100)
p.printarea()
p.get_sides()
p.printperimeter()
p.draw()

print("\n HEXAGON \n")
h = shapes.Hexagon(6, 150)
h.printarea("Hexagon")
h.get_sides("Hexagon")
h.printperimeter("Hexagon")
h.draw()

print("\n CIRCLE \n")
c = shapes.Circle(100)
print("Area of circle is: ",c.area())
print("Circumference of circle is: ",c.circumference())
c.draw()

print("\n ELLIPSE \n")
c = shapes.Ellipse(100, 50)
print("Area of ellipse is: ",c.area())
print("Circumference of ellipse is: ",c.circumference())
c.draw()

print('\n Sphere \n')
s = shapes.Sphere(100)
print("Surface area of sphere is: ", s.surface_area())


