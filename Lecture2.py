# Classes

# Classes are blueprint for creating Objects
# Objects they bundle Attributes and Methods (Functions)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Welcome to the GDG Bootcamp {self.name}, you are {self.age} years old")  # noqa


class Student(Person):
    def __init__(self, name, age, Dept):
        super().__init__(name, age)
        self.Dept = Dept

    def greet(self):
        print(f"Heyyyy {self.name} from {self.Dept}, You are {self.age} years old!!")  # noqa


person1 = Person("Paul", "25")
person2 = Person("Akeem", "19")
student1 = Student("Akeem", "19", "Electrical and Electronics")
person1.greet()
person2.greet()
student1.greet()