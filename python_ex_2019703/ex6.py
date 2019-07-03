class Person():
    def work(self):
        print('work hard')
class Student(Person):
    def work(self):
        Person.work(self) #부모 클래스 메서드 호출
        print("Study hard")
    def parttime(self):
        super().work()
    def general(self):
        self.work()
student1 = Student()
student1.work()
