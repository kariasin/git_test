import math

num = '''
75 
95 64 
17 47 82 
18 35 87 10 
20 04 82 47 65 
19 01 23 75 03 34 
88 02 77 73 07 63 67 
99 65 04 28 06 16 70 92 
41 41 26 56 83 40 80 70 33 
41 48 72 33 47 32 37 16 94 29 
53 71 44 65 25 43 91 52 97 51 14 
70 11 33 28 77 73 17 78 39 68 17 57 
91 71 52 38 17 14 91 43 58 50 27 29 48 
63 66 04 68 89 53 53 67 30 73 16 69 87 40 31 
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23    
'''

lines = len(int(num))
num = num.split('\n')
num = ('\n').split()   
numbers = []
for line in lines:
    print(line.split('\n'))
    nubers.append(line.split())


num1 = math.pow(1,4)
num2 = math.pow(6,4)
num3 = math.pow(3,4)
num4 = math.pow(4,4)

sum = num1 + num2 + num3 + num4
temp = 0
pow_temp = 0
num = []
sum = 0
k = 0
total = 0
for i in range(10000, 100000):
    temp = i
    #print(temp)
    for j in range(0, 5):
        pow_temp = int(temp % 10)
        sum += pow(pow_temp,5)
        #print(pow(pow_temp,5))
        temp = int(temp / 10)
    num.append(sum)
    #print(sum, i)
    if sum == i:
        print(i)
        k = k + 1
        total = total + sum
    sum = 0     
print(total)

#243 32 32768
print(pow(5,5) + pow(4,5) + pow(7,5) + pow(4,5) + pow(8,5))
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# print(sum)