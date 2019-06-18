#21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하라.
s = "letters"
print("21: " + s[0], s[2])

#22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라.
#license_plate = "24가 2210"
license_plate = "24가 2210"
print("22: " + license_plate[4:])

#23 아래의 문자열에서 '홀' 만 출력하라.
#string = "홀짝홀짝홀짝"
string = "홀짝홀짝홀짝"
print("23: " + string[0::2])

#24 문자열을 거꾸로 뒤집어 출력하라.
string = "PYTHON"
print("24: " + string[::-1])

#25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하라
phone_number = "010-1111-2222"
print("25: " + phone_number.replace("-"," "))


#26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하라
phone_number = "010-1111-2222"
print("26: " + phone_number.replace("-",""))


#27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하라.
url = "http://sharebook.kr"
print("27: " + url[-2:])

#28 아래 코드의 실행 결과를 예상하라
#lang = 'python'
#lang[0] = 'P'
#print(lang)



#29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하라.
string = 'abcdfe2a354a32a'

print("29: " + string.replace('a','A'))

#030 아래 코드의 실행 결과를 예측하라.
string = 'abcd'
string.replace('b', 'B')
print("30: " + string) # -> abcd