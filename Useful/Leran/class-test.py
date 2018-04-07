class Person(object):
	def __init__(self,name):
		self.name=name
	def get_name(self):
		self.pet=None
		print(self.name)

		
class nuers(Person):

	def get_name(self):
		super(nuers,self).get_name()
		print('yes good job')

A=nuers('dog')
A.get_name()