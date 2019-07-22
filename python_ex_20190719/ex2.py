# 랜덤으로 되어있는 list 숫자 작은수로 정렬하기
import random

data_list = random.sample(range(100), 10)
print(data_list)

data_list = random.sample(range(100), 10)
def sorting(data):
    for index in range(len(data) - 1):
        lowest = index
        for index2 in range(index + 1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]
    return data

print(sorting(data_list))

# data_list = random.sample(range(100), 10)
# print(data_list)
# def sorting(data):
#     for index in range(len(data_list) - 1):
#         lowest = index
    
#         for index2 in range(index + 1, len(data_list)):
#             if data_list[lowest] > data_list[index2]:
#                lowest = index2
#         data_list[index], data_list[lowest] = data_list[lowest], data_list[index]   
#     return data_list
# print(sorting(data_list))











