import random

data_list = random.sample(range(100), 10)

print("정렬 전:", data_list)
def insertion_sort(data):
    for stand in range(len(data)):
        key = data[stand]
        for num in range(stand, 0, -1):
            if key < data[num - 1]:
                data[num], data[num - 1] = data[num - 1], data[num]
            else:
                break
    return data

print("정렬 후:",insertion_sort(data_list))

def sorting(data):
    for index in range(len(data)- 1):
        lowest = index
        for index2 in range(index + 1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]
    return data
print("정렬 후:",sorting(data_list))