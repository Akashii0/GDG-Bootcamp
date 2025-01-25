# Classes

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Heyyyy welcome to the Bootcamp! {self.name}, You are {self.age} years old")  # noqa


class Student(Person):
    def __init__(self, name, age, Dept):
        super().__init__(name, age)
        self.Dept = Dept

    def greet(self):
        print(f"Heyyyy welcome to the Bootcamp! {self.name} from {self.Dept}")


person1 = Person("Paul", "25")
student1 = Student("Paul", "25", "Mechatronics")  # noqa
person1.greet()
student1.greet()
