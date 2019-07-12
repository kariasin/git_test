name1 = 'Dave'
name2 = 'David'

# 1차원 배열: 리스트로 구현시
data_list = [1,2,3,4,5]
data_list2 = [[1,2,3],[4,5,6],[7,8,9]]
print(data_list2[2][2])
for index in range(2, -1, -1):
    for index2 in range(2, -1, -1):
        print(data_list2[index][index2])
