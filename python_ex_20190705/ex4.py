# 1. 싱글톤 클래스 만들기
class Singleton(type):  #Type을 상속받음
    __instances = {}     #클래스의 인스턴스를 저장할 속성

    def __call__(cls,*args,**kwargs):   #클래스로 인스턴스를 만들 때 호출하는 메서드
        if cls not in cls.__instances:  #클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args,**kwargs) #생성하지 않았으면 인스턴스를 생성하여 해당 클래스 사전에 저장
        return cls.__instances[cls]     # 클래스로 인스턴스를 생성했으면 인스턴스 반환

# 2. 싱글톤 클래스 만들기
class PrintObject(metaclass=Singleton): #메타클래스로 Singleton을 지정
    def __init__(self):
        print("This is called by super().__call")

# 3. 싱클톤 객체 만들기(object1, object2 모두 동일)
object1 = PrintObject()
object2 = PrintObject()

print(object1)
print(object2)