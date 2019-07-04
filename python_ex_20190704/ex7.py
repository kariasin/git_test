#다중상속
class Person:
    def sleep(self):
        print('sleep')
class Student(Person):
    def study(self):
        print('Studay hard')

    def play(self):
        print('play with friends')    
class Worker(Person):
    def work(self):
        print('work hard')
    def play(self):
        print('drinks alone')    

#다중상속
class PartTimer(Student,Worker):
    def find_jon(self):
        print('Find a jon')
parttimer1 = PartTimer()
parttimer1.study()
parttimer1.work()
parttimer1.play()

class Saladent(Worker,Student):
    def play(self):
        print("drinks alone")

parttimer2 = PartTimer()
parttimer2.play()
