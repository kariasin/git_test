#21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하라.
s = "letters"
print(s[0])
print(s[2])


#22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라.
#license_plate = "24가 2210"
license_plate = "24가 2210"
print(license_plate[4:])

#23 아래의 문자열에서 '홀' 만 출력하라.
#string = "홀짝홀짝홀짝"
string = "홀짝홀짝홀짝"
print(string[0::2])

#24 문자열을 거꾸로 뒤집어 출력하라.
string = "PYTHON"
print(string[::-1])

#25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하라
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))


#26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하라
phone_number = "010-1111-2222"
print(phone_number.replace("-",""))


#27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하라.
url = "http://sharebook.kr"
print(url)

#28 아래 코드의 실행 결과를 예상하라
#lang = 'python'
#lang[0] = 'P'
#print(lang)



#29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하라.
string = 'abcdfe2a354a32a'

print(string.replace('a','A'))

#030 아래 코드의 실행 결과를 예측하라.
string = 'abcd'
string.replace('b', 'B')
print(string) # -> abcd