# 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을
#  사전순으로 리턴하는 함수 solution을 완성해주세요.

import itertools
def solution(mylist):
    answer = [[]]
    answer = list(map(''.join, itertools.permutations(mylist)))
    return answer
list1 = ['A','B','C']
print(solution(list1))

import collections

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)
print(answer)