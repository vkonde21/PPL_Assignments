from abc import ABC, abstractmethod
#base abstract class
class Shape(ABC):
	@abstractmethod
	def printarea(self):
		pass
	@abstractmethod
	def printperimeter(self):
		pass
	@abstractmethod
	def get_sides(self):
		pass
