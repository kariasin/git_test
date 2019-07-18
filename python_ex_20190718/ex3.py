def factorial(num):
    factorial_value = 1
    for factorial_item in range(1, num + 1):
        factorial_value = factorial_value * factorial_item
    return factorial_value
print(factorial(5))


def factorial2(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num
for num in range(1,5):
    print(factorial2(num))