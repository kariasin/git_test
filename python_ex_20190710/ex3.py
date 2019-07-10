# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기

def general_decorator(function):
    def wrapper(*args, **kwargs):
        print('function is decorated')
        return function(*args, **kwargs)
    return wrapper

# 데코레이터 적용하기
@general_decorator
def calc_square(digit):
    return digit * digit

@general_decorator
def calc_plus(digit1, digit2):
    return digit1 + digit2

@general_decorator
def calc_quad(digit1, digit2, digit3, digit4):
    return digit1 * digit2 * digit3 * digit4


# 함수 호출하기
print(calc_square(2))
print(calc_plus(2,3))
print(calc_quad(2,3,4,5))


#한 함수에 데코레이터 여러 개 지정하기
def decorator1(function):
    def wrapper():
        print('decorator1')
        function()
    return wrapper

def decorator2(function):
    def wrapper():
        print('decorator2')
        function()
    return wrapper


@decorator1
@decorator2
def hello():
    print('hello')

hello()