class Student:
    def __init__(self, name, age = None, grade = None):
        self.name = name
        self.age = age
        self.grade = grade


student_1 = Student("Dmitry")
student_2 = Student("Bob", 25)
student_3 = Student("Charlie", grade= "A")
student_4 = Student("Olga", 40, "A")