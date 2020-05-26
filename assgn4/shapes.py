
import math
from abstract import Shape
import turtle		
		
class Rectangle(Shape):
	sides = 4
	
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
		
	def printarea(self):
		print("Area is:", self.length * self.breadth)
		
	def printperimeter(self):
		print("Perimeter is:", 2 * (self.length + self.breadth))
		
	def get_sides(self):
		print("Number of sides are:", self.sides)

	def draw(self):
		t = turtle
		t.forward(self.length)
		t.left(90)
		t.forward(self.breadth)
		t.left(90)
		t.forward(self.length)
		t.left(90)
		t.forward(self.breadth)
		t.left(90)
		t.done()
		try:
			t.exitonclick()
		except:
			pass

		
#regPolygon is inherited from Shape
#Polymorphism is shown by printarea, printperimeter an get_sides function
class regPolygon(Shape):
	def __init__(self, nsides = 3, side = 4):
		self.n = nsides
		self.l = side
		
	def printarea(self, name):
		p = self.l * self.n
		a = p/abs(math.tan(180/self.n))
		A = p * a
		print(f"Area of {name} is: ",A/2)
		
	def printperimeter(self, name):
		print(f"Perimeter of {name} is: ", self.n * self.l)
		
	def get_sides(self,name):
		print(f"Number of sides in a {name} are: ", self.n)

	def draw(self):
		pass
		
	
	
#Square is inherited from regPolygon
class Square(regPolygon):
	def diagonal(self):
		print("Length of diagonal is: ", math.sqrt(2) * self.l)

	def draw(self):
		t = turtle
		t.forward(self.l)
		t.left(90)
		t.forward(self.l)
		t.left(90)
		t.forward(self.l)
		t.left(90)
		t.forward(self.l)
		t.left(90)
		t.done()
		try:
			t.exitonclick()
		except:
			pass
		
		

class Triangle(regPolygon):
	def draw(self):
		t = turtle
		for _ in range(3):
			t.forward(self.l)
			t.left(120)
		t.done()
		try:
			t.exitonclick()
		except:
			pass
	
class Rhombus(Shape):
	sides = 4
	def __init__(self, height, base):
		self.h = height
		self.b = base
		
	def printarea(self):
		print("Area of rhombus is: ", self.b * self.h)
		
	def printperimeter(self):
		print("Perimeter of rhombus is: ",self.b * 4)
		
	def get_sides(self):
		print("Number of sides in a rhombus are:", self.sides)

	def draw(self):
		t = turtle
		t.forward(self.b)
		t.left(60)
		t.forward(self.b)
		t.left(120)
		t.forward(self.b)
		t.left(60)
		t.forward(self.b)
		t.left(120)
		t.done()
		try:
			t.exitonclick()
		except:
			pass



		
		
class Parallelogram(Rectangle):
	def draw(self):
		t = turtle
		t.forward(self.length)
		t.left(60)
		t.forward(self.breadth)
		t.left(120)
		t.forward(self.length)
		t.left(60)
		t.forward(self.breadth)
		t.left(120)
		t.done()
		try:
			t.exitonclick()
		except:
			pass

class Hexagon(regPolygon):
	sides = 6
		
	def draw(self):
		t = turtle
		for _ in range(6):
			t.forward(self.l)
			t.left(60)
		t.done()
		try:
			t.exitonclick()
		except:
			pass
        
	

class Circle:
	def __init__(self, r):
		self.radius = r
		
	def area(self):
		return math.pi * math.pow(self.radius,2)
		
	def circumference(self):
		return 2 * math.pi * (self.radius)

	def draw(self):
		t = turtle
		t.circle(self.radius)
		t.done()
		try:
			t.exitonclick()
		except:
			pass
        
		 
class Ellipse(Circle):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def area(self):
		return math.pi * (self.a) * (self.b)
		
	def circumference(self):
		return math.pi * ((self.a) + self.b)

	def draw(self):
		t = turtle
		t.right(45)
		for _ in range(2):
			t.circle(self.a, 90)
			t.circle(self.b, 90)
		t.done()
		try:
			t.exitonclick()
		except:
			pass

        
		
class Sphere(Circle):
	def surface_area(self):
		return 4 * self.area()
		

