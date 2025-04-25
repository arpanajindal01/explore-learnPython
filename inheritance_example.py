class Parent:
    def __init__(self):
        print("Parent class is created")

    def speak(self):
        print("Parent is speaking")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class is created")

    def speak(self):
        super().speak()                             # Inheriting speak() method as is from the parent class using super keyword
        print("Child is speaking")                  # here we are overriding the speak() method
                                                    # in the child class inherited from parent class

my_child = Child()
my_child.speak()
