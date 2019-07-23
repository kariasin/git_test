mylist = [[1,2,3],[4,5,6],[7,8,9]]
new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append(mylist[j][i])
print(new_list)

new_list2 = list(map(list, zip(*mylist)))
print(new_list2)
