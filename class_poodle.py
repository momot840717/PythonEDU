from class_dog import Dog

#  把 Dog 物件的變數、函數 繼承過來 就不用重新寫一次程式
class Poodle(Dog):  # Poodle 繼承 Dog
    def __init__(self, name, age):
        super().__init__(name, age)

    def Poodle_color(self, color):
        print(f'The color of poodle is {color}.')