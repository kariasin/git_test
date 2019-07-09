def calc_square(digit):
    return digit * digit

def calc_plus(digit):
    return digit + digit

def calc_quad(digit):
    return digit * digit * digit * digit

def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit))
    print(result)

num_list = [1,2,3,4,5]

num = calc_square(2)

print(num)

func1 = calc_square
print(func1(2))
print(func1)

class MyClass:
    def my_class(self):
        print('안녕')
        pass
object1 = MyClass()
my_class1 = object1.my_class
my_class1()

list_square(calc_square,num_list)
list_square(calc_plus,num_list)
list_square(calc_quad,num_list)










