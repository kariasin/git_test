def func_mul(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

print(func_mul(100))

def func_mul2(num):
    return int (num * (num + 1) / 2)
print(func_mul2(100))

names = ['Dave', 'David', 'Anthony', 'Andy', 'Dave']

def func_mul3(name_list):
    for index, name in enumerate(name_list):           # 반복문에 주의!
        for index2 in range(index + 1, len(name_list)):   # 반복문에 주의!
            if (name == name_list[index2]):
                del name_list[index2]

    return name_list
print(func_mul3(names))