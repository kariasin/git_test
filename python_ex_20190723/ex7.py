#짝수만 제곱하기
def solution(mylist):
    answer = []
    for i in mylist:
        if i % 2 == 0:
            answer.append(i ** 2)
    return answer
list1 = [3,2,6,7]    
print(solution(list1))

# List comprehension의 if 문 
answer = [i ** 2 for i in list1 if i % 2 == 0]

print(answer)



#두 변수의 값 바꾸기
a = 3
b = 'abc'

print(a, b)

a , b = b, a
print(a, b)

# 이진검색
import bisect
mylist = [1,2,3,7,9,11,33]
print(bisect.bisect(mylist,7))