# 데코레이터 작성하기(for method)
def h1_tag(function):
    def func_wrapper(self,*args,**kwargs):  # self를 무조건 첫 파라미터로 넣어야 메서드에 적용 가능
        return "<h1>{0}</h1>".format(function(self,*args,**kwargs))
    return func_wrapper

#클래스 선언시 메서드에 데코레이터 적용하기
class Person:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @h1_tag
    def get_name(self):
        return self.first_name + ' ' + self.last_name

davelee = Person('Lee','Dave')
print(davelee.get_name())
    