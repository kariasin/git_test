import random

num = random.sample(range(100), 10)
print(num)

print(len(num))

def test(n):
    tmp = ''
    for i in range(len(num)):
        #print("{0}: ".format(i), num[i], n )
        if n == num[i]:
            tmp = i
    if tmp == '':
        tmp = "None"
    return tmp
print(test(100))
