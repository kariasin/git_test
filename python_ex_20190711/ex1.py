#이터레이터
#list,set,dictionary 등의 컬렉션
# list, set, dictionary 등의 컬렉션(collection)
# 문자열: 문자열을 이루는 각 문자 Sequence
# 이와 같은 컬렉션(collection), Sequence등을 iterable 객체(iterable Object)라고 함
# 간단히 for 구문으로 각 데이터를 탐색할 수 있는 데이터 집합

# 예1: 리스트 컬렉션
# for num in [1,2,3,4,5]:
#     print(num, end='')
# print("")
# # 예2: 문자 sequence
# for char in "Dave Lee":
#     print(char, end='')
# print("")

# itrable 객체 : iterator를 리턴할 수 있는 객체
# iterator : 순차적으로 다음 데이터를 리턴할 수 있는 객체
#            내장 함수 next 함수를 사용해서, 순환하는 다음 값을 반환함


class Counter:
    def __init__(self, stop):
        self.stop = stop    #반복을 끝낼 숫자

    def __iter__(self):                     # iterable 객체는 __iter__ 메서드가 존재함
        return Counter_Iterator(self.stop)  # Counter의 iterator 객체를 리턴해줌
class Counter_Iterator:
    def __init__(self, stop):
        self.current = 0    # 현재 상태를 확인하기 위한 속성
        self.stop = stop
    
    def __next__(self):             # iterator는 __next__메서드가 존재함
        if self.current < self.stop: # 현재 상태가 stop보다 적을 때는 현재 상태값을 리턴해주고 , 1씩 상태값을 중가
            return_value = self.current
            self.current += 1
            return return_value 
        else:                       # 현재 상태가 stop가 동일 또는 클 때는 StopIteration 이벤트를 발생시킴
            raise StopIteration     # 예외 발생
Counter_Iterator = iter(Counter(5))


print(next(Counter_Iterator))
print(next(Counter_Iterator))
print(next(Counter_Iterator))
print(next(Counter_Iterator))
print(next(Counter_Iterator))
print(next(Counter_Iterator))


