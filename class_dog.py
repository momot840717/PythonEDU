class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f'{self.name} is sitting now.')

	def name_data(self):
		print(f'The name of my dogs is {self.name}')

	def age_data(self):
		print(f'The age of my dogs is {self.age}')

	def dog_data(self):
		self.name_data()
		self.age_data()