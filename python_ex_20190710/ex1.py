#데코레이터
import datetime

def logger_login():
    print(datetime.datetime.now())
    print("Dave login")
    print(datetime.datetime.now())

#logger_login()




# 데코레이터 작성하기
def datetime_decorator(func):       # datetime_decorator는 데코레이터 이름,func가 이 함수 안에 넣을 함수가 됨
    def wrapper():
        print('time  ' + str(datetime.datetime.now()))  #함수 앞에서 실행할 내용
        func() # 함수
        print(datetime.datetime.now()) # 함수 뒤에서 실행할 내용
    return wrapper

# 데코레이터 적용하기
@datetime_decorator # @데코레이터
def logger_login_david():
    print("David login")

#logger_login_david()

@datetime_decorator
def logger_login_anthony():
    print("Anthony login")

#logger_login_anthony()  

@datetime_decorator
def logger_login_tina():
    print("Tina login")    

#logger_login_tina()

# decorator 함수 정의
def outer_func(function):
    def inner_func():
        print('decoration added')
        function()
    return inner_func

# decoration할 함수
def log_func():
    print('logging')

#log_func()

decorated_func = outer_func(log_func)
decorated_func()

#decorating으로 변경하면
@outer_func
def log_func2():
    print("logging")
log_func2()