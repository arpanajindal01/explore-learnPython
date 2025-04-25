class Parent:
    def greet(self, name = None):
        if name is None:
            return "Hello, Unknown Person."

        else:
            return f"Hello, {name}."

class Child(Parent):
    def greet(self, name = None, age = None):    ## Method Overriding, using the same method and arguments but returning different message
        if name is None:
            return "Hey, who are you and how old are you?"
        else:
            return f"Hey, {name}, you are {age} years old."

my_parent = Parent()
print(my_parent.greet())
print(my_parent.greet("Dmitry"))

my_child = Child()
print(my_child.greet())
print(my_child.greet("Bob", 30))