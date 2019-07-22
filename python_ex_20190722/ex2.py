# 선택정렬(selection sort)
# 리스트에 숫자가 낮은 순으로 위치를 바꾸는것
# 파이썬에는 sorted()함수가 있음
# sorted(data_list)

import random

data_list = random.sample(range(100), 10)
print(data_list)
def sorting(data):
    for index in range(len(data) - 1):
        lowest = index
        for index2 in range(index + 1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]
    return data

print(sorting(data_list))




