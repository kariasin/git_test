import string

str_text = string.ascii_letters +' '
text = "abcdef"
print(len(text))
# for i in range (len(text)):
#     print(text[i])

def solution(s, n):
    answer = ''
    for index in range(len(s)):
        for index2 in range(len(str_text)):
            if s[index] == str_text[index2]:
                index2 = int(index2) +  n
                answer += str_text[index2]
    return answer




text = ''
print(solution(text,1))



days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i, day in enumerate(days):
    print('{}월의 날짜수는 {}일 입니다.'.format(i + 1, day))

numbers = [ (1,2),(10,0) ]

for a,b in numbers:
    if b == 0:        
        print("0으로 나눌 수는 없습니다.")
    else:
        # 이 부분이 else문에 들어있지 않도록 수정해야 합니다.
        continue
        print("{}를 {}로 나누면 {}".format(a,b,a/b))
    