import itertools
import functools
import operator

#2차원 리스트를 1차원 리스트로 변경
list1 = [[1],[2]]
list2 = [['A','B'],['X','Y'],['1']]

# 방법 1 - sum 함수
answer = sum(list1,[])
print(answer)

# 방법 2 - itertools.chain
answer = list(itertools.chain.from_iterable(list1))
print(answer)

# 방법 3 - itertools와 unpacking
answer = list(itertools.chain(*list1))
print(answer)

# 방법 4 - list comprehesion 이용
print([element for array in list1 for element in array])

# 방법 5 - reduce 함수 이용1
print(list(functools.reduce(lambda x, y: x+y, list1)))

# 방법 6 - reduce 함수 이용2
print(list(functools.reduce(operator.add, list1)))
