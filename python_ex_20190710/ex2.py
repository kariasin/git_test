# 파라미터가 있는 함수에 Decorator 적용하기
# 데코레이터
def outer_func(function):
    def inner_func(digit1,digit2):
        if digit2 == 0: #   유효성 검사의 예
            print('cannot be divided with zero')
            return
        return function(digit1,digit2)
    return inner_func
# def divide(digit1,digit2):
#     return digit1/digit2

#데코레이터 사용하기(유효성 검사)
@outer_func
def divide(digit1,digit2):
    return digit1/digit2

print(divide(9,0))


def type_checker(function):
    def inner_func(digit1, digit2):
        if(type(digit1) != int) or (type(digit2) != int):
            print('only integer support')
            return
        return function(digit1, digit2)
    return inner_func

@type_checker
def muliplexer(digit1, digit2):
    return digit1 * digit2

muliplexer(1.1,2)

