#순차 탐색: 주어진 리스트 데이터에서 특정한 데이터가 있는 위치 탐색하기
import random

data_list = random.sample(range(20), 10)
print(data_list)

def find_list(data,num):
    for index in range(len(data)):
        print(data[index])
        if data[index] == num:
            return index
print(find_list(data_list,15))