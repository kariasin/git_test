from typing import NamedTuple

class Employee(NamedTuple):
    name:str = 'Guido'
    id:int = 3


employee1 = Employee()
print(employee1)
print(employee1.name,employee1.id)


employee2 = Employee('Dave',4)
print(employee2)
print(employee2.name,employee2.id)


class Em(NamedTuple):
    name:str='testName'
    age:int=20
    org:str='abc'
em1 = Em()
print(em1)    


