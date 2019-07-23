#문자열을 숫자로 변경해서 출력
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(int(i))
    return answer

list1 = ['1','100','33']
print(solution(list1))
# 파이썬에서 map을 사용하여 변경하는 법
list2 = list(map(int,list1))
print(list2)

# solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴

def solution2(mylist):
    answer = list(map(len,mylist))
    return answer

print(solution2(list1))    

