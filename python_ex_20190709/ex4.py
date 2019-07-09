#클래스 없이 객체를 생성할 수 있는 방법 - 클래스에 attribute만 있는 경우 해당
# tuple 클래스 활용
# attribute만 있는 클래스의 경우 해당

import collections

Employee = collections.namedtuple('Employee', ['name','id'])
employee1 = Employee('Dave','4011')
employee2 = Employee(id='4012',name='David')
print(employee1)
print(employee2)

name,id = employee2
print(name,id)

class EmplyeeClass:
    def __init__(self,name,age,org):
        self.name = name
        self.age = age
        self.org = org
emClass = EmplyeeClass('testName',15,'Y')
print(emClass.name,emClass.age,emClass.org)
em = collections.namedtuple('em',['name','age','dept'])
em1 = em('testName',15,'Y')
name,age,dept = em1
print(name,age,dept)



















