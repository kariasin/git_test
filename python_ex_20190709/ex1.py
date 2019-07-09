class Student(object):
    def __init__(self,name,age=20,height=180,weight=60,major='cs'):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.major = major
    def view(self):
        print(self.name, self.age, self.height, self.weight, self.major)
student1 = Student('Dave')
student2 = Student(major='ds',name='David')
student1.view()
student2.view()