def outer_func():
    print('call outer func function')

    def inner_func():
        return 'call inner_func function'

    print(inner_func())
print(outer_func())

# print(inner_func()) 외부에서는 내부함수 호출 불가
