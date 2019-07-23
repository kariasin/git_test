list1 = ['1','100','33']
def solution(mylist):
    answer = ''
    for i in mylist:
        answer += i
    return answer

print(solution(list1))
#파이썬의 join을 사용하면 이 코드를 두 줄로 줄일 수 있습니다 .
print(''.join(list1))

# 이 문제에는 표준 입력으로 정수 n이 주어집니다.
# 별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.

n = int(input().strip())
for i in range(1, n+1):
    print('*'*i)

