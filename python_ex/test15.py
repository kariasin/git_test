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




# 회문수는 같은 방법으로 읽습니다. 두 자리 숫자 두 개를 곱하여 만든 최대 회문은 9009 = 91 × 99입니다.

# 2 자리 3 자리 숫자의 곱으로 만들어진 최대 회문을 찾으십시오.
#4번문제
maxValue = 0

for i in range(10,999):
    for j in range(19,999):
        product = i * j
        if(str(product) == str(product)[::-1]):
            if product > maxValue:
                maxValue = product
print(maxValue)                



#5.문제
import math
 
lcm=1
for i in range(1,21):
    gcd = math.gcd(lcm,i)
    lcm = int(lcm*i/gcd)
    print(i,lcm)


#6.문제
import math


sum = 0
sum2 = 0
for i in range(1,101):
    sum += math.pow(i,2)
    sum2 += i
print(int(sum))
print(sum2)
print(int(math.pow(sum2,2)) - int(sum))


#7.문제 너무 오래 걸림
import math
a = []
count = 0
i = 2 
num = 0
while True:
    num = i + 1
    for j in range(1, num):
        if i % j == 0:
            count += 1
        j += 1
    if(count == 2):
        a.append(i)
    count = 0
    if(len(a) == 1000):
        break
    i += 1                
print(a[-1])   


#8.문제

str_txt = '''
73167176531330624919225119674426574742355349194934 
96983520312774506326239578318016984801869478851843 
85861560789112949495459501737958331952853208805511 
12540698747158523863050715693290963295227443043557 
66896648950445244523161731856403098711121722383113 
62229893423380308135336276614282806444486645238749 
30358907296290491560440772390713810515859307960866 
70172427121883998797908792274921901699720888093776 
65727333001053367881220235421809751254540594752243 
52584907711670556013604839586446706324415722155397 
53697817977846174064955149290862569321978468622482 
83972241375657056057490261407972968652414535100474 
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586 
17866458359124566529476545682848912883142607690042 
24219022671055626321111109370544217506941658960408 
07198403850962455444362981230987879927244284909188 
84580156166097919133875499200524063689912560717606 
05886116467109405077541002256983155200055935729725 
71636269561882670428252483600823257530420752963450
'''.replace('\n','').replace(' ','')

print(str_txt)
maxValue = 0
for i in range(1,1000):
    product = 1
    for j in str_txt[i:i+13]:
        product = product * int(j)
    if product > maxValue:
        maxValue = product
print(maxValue) 


#9.문제

import math

for i in range(1,1000):
    for j in range(1,i):
        if math.pow(i,2) + math.pow(j,2) == math.pow(1000-i-j,2):
            print(i, j, 1000-i-j)
            print(i * j * (1000-i-j))
            break




