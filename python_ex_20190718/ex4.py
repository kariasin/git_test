# 임의의 수 곱하기
# def func_mul(num):
#     if num > 1:
#         return num * func_mul(num - 1)
#     else:
#         return num
# print(func_mul(10))


import random

data = random.sample(range(100), 10)
print(data)
def func_sum(obj):
    sum = 0
    for num in obj:
        sum += num
    return sum

print(func_sum(data))



def func_sum2(obj):
    if(len(obj) == 1):
        return obj[0]
    return obj[0] + func_sum2(obj[1:])

print(func_sum2(data))

