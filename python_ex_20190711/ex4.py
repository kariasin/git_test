## array 라이브러리 활용 예1
from array import *

data_array = array('l',[1,2,3,4,5])
# print(data_array[1])

## array 라이브러리 활용 예2

data_array2 = array('i',range(10))
# print(data_array2[0])
# print(data_array2[5])

#array 라이브러리 활용 예 4
data_array4 = array('i')
for num in range(1000):
    data_array4.append(num)
print(data_array4[10])
del data_array4[10]
print(data_array4[10])

array('i',[1,2,3,4,5])
array('i',range(1000))
array('i')



