# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

# sum = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)

#fibo
a = [1,2]
sum = 0

while True:
    sum = a[-1] + a[-2]
    if sum < 4000000:
        a.append(sum)
    else:
        break
    #print("i ",  i, a[i])
print(a)
sum = 0    
for i in a:
    if i % 2 == 0:
        sum += i

print(sum)