# fibo

def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)
for i in range(1, 11):
    print("fibo({0}):".format(i), fibo(i))

