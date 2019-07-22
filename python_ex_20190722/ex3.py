# 삽입정렬
# 삽입정렬은 두 번째 인덱스부터 시작
# 해당 인덱스(key 값)앞에 있는 데이터(B)부터 비교해서 key값이
# 더 작으면 B값을 뒤 인덱스로 복사

import random

data_list = random.sample(range(100), 4)
print(data_list)
# def insertion_sort(data):
#     for stand in range(len(data_list)):
#         key = data[stand]
#         for num in range(stand, 0 , -1):
#             if key < data[num - 1]:
#                 data[num - 1], data[num] = data[num], data[num - 1]
#             else:
#                 break
#     return data    


def insertion_sort(data):
    for stand in range(len(data)):
        key = data[stand]
        for num in range(stand, 0 , -1):
            if key < data[num-1]:
                data[num - 1], data[num] = data[num], data[num-1]
            else:
                break
    return data


print(insertion_sort(data_list))






def sorting(data):
    for index in range(len(data) - 1):
        lowest = index
        for index2 in range(index + 1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]
    return data

print(sorting(data_list))






