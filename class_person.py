"""
class Person:：這是定義類的開始，Person 是類的名字。
__init__ 方法：Person的參數(name, age)會在這裡代入，並在下面賦值給 self.name, self.age ----告訴程式: 這是屬於 Person 物件的 name, 這是屬於 Person物件的age
self n. 自己
greet 方法：這是一個實例方法 ----告訴程式: 這是屬於 Person 物件的函數功能。
"""


class Person:
	def __init__(self, name, age):  # self 就是 Person 物件
		self.name = name
		self.age = age

	def greet(self):  # Person的greet函數
		return f"Hello, my name is {self.name} and I am {self.age} years old."


# person1 = Person('Brian', 11)  # 實例化
# print(person1.greet())  # 使用實例函數


"""
class 的繼承
新的class 可以繼承原有的class所有屬性、函數
"""


class Student(Person):
	def __init__(self, name, age):
		super().__init__(name, age)


student1 = Student('Mario', 20)
print(student1.name)
print(student1.age)
print(student1.greet())