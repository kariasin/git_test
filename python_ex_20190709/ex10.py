def outer_func(num):
    def inner_func():
        print(num)
        return '안녕'
    return inner_func

out = outer_func(100)
out()

def calc_square(digit):
    return digit * digit