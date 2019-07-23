mylist = [1,2,3]
new_list = [40,50,60]
for i in zip(mylist,new_list):
    print(i)



list1 = [1,2,3,4]
list2 = [100,120,30,300]
list3 = [392,2,33,1]

answer = []

for i,j,k in zip(list1,list2,list3):
    print(i + j + k)

animals = ['cat','dog','lion']
sounds = ['meow','woof','roar']
answer = dict(zip(animals,sounds))
print(answer)