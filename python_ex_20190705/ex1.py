class Person:
    def __init__(self):
        print('I am a person')
class Student(Person):
    def __init__(self):
        super().__init__()
        print('I am a student')
class Worker(Person):
    def __init__(self):
        super().__init__()
        print('I am a worker')
class PartTimer(Student,Worker):
    def __init__(self):
        super().__init__()
        print('I am a part-timer and student')
part = PartTimer()

print(PartTimer.__mro__)