from abc import ABC, abstractmethod
class animal(ABC):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def type(self):
		pass
    	
	def is_endangered(self):
		pass
    	
	def food(self):
		pass

class Cat(animal):
	legs = 4
	def info(self):
		print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

	def make_sound(self):
		print("Meow")
        
	def type(self):
		print("Terrestrial")
		
	def is_endangered(self):
		return False
		
	def food(self):
		print("Rat, milk")

class Dog(animal):
	legs = 4
	def info(self):
		print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

	def make_sound(self):
		print("Bark")
        
	def type(self):
		print("Terrestrial")
		
	def is_endangered(self):
		return False
		
	def food(self):
		print('Bone Broth, Raw Goat Milk')
		
		
class Wild(animal):
	legs = 4
	def food(self):
		print("Most of them eat other animals living in the jungle")
		
	def type(self):
		print('Mammal')
		
	def is_endangered(self):
		pass
    	
class Lion(Wild):
	def is_endangered(self):
		return True
	def sound(self):
		print("Roar")
	def famous(self):
		print("famous as king of jungle")
    	
class Reptile(animal):
	def type(self):
		print("Vertebrates")
		
	def scales(self):
		print("all reptiles have scales")
		
	def type(self):
		print("They produce eggs. They are not mammals.")
		
class Snake(Reptile):
	def famous(self):
		print("Venomous snakes are used for making vaccines")
		
class Elephant(Wild):
	def famous(self):
		print("World's  largest land animal")
	def food(self):
		print("Plants, Grass")
	def other_qualities(self):
		print("Their tusks never stop growing")
	def is_endangered(self):
		return False
		
class Bird(ABC):
	@abstractmethod
	def can_fly(self):
		pass
	def type(self):
		print("Aves")
	def wings(self):
		print("All birds have wings, although not all birds fly. ")
	@abstractmethod
	def beak_type(self):
		pass
	@abstractmethod
	def famous(self):
		pass
class Ostrich(Bird):
	def can_fly(self):
		return False
	def beak_type(self):
		print("Broad beak with rounded tip")
	def famous(self):
		print("Tallest bird")
		
	
