# print('{} {}'.format(10, 100))
# print('{0} {2} {0} {1}'.format(10,100,20))
# print('{1} {0}'.format(10, 100))
# print('{aa} {bb}'.format(aa = 'aaaa', bb = 'cccc'))

# 중첩 함수의 하나 더 깊게 두어 생성
def decorator1(num):
    def outer_wrapper(function):
        def innter_wrapper(*args, **kwargs):
            print('decorator1 {}'.format(num))
            return function(*args, **kwargs)
        return innter_wrapper
    return outer_wrapper



@decorator1(1)
def print_hello():
    print('hello.')
print_hello()

@decorator1(num=2)
def print_hello2():
    print('hello')
print_hello2()
    
