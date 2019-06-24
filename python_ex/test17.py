# 1 2015년 9월 초의 네이버 종가는 표 3.2와 같습니다. 09/07의 종가를 리스트의 첫 번째 항목으로 입력해서 naver_closing_price라는 이름의 리스트를 만들어보세요.
naver_closing_price = [474500, 461500, 501000, 500500, 488500]

print("1", naver_closing_price)

#2 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에 종가를 기준으로 가장 높았던 가격을 출력하세요.
#  (힌트: 리스트에서 최댓값을 찾는 함수는 max()이고, 화면에 출력하는 함수는 print()입니다.)
max_price = max(naver_closing_price) 
print("2", max_price)

#3 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에 종가를 기준으로 가장 낮았던 가격을 출력하세요.
#  (힌트: 리스트에서 최솟값을 찾는 함수는 min()이고, 화면에 출력하는 함수는 print()입니다.)
min_price = min(naver_closing_price)
print("3", min_price)

#4 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에서 가장 종가가 높았던 요일과 가장 종가가 낮았던 요일의 가격 차를 화면에 출력하세요..
print ("4", max_price - min_price )

#5 문제 3-1에서 만든 naver_closing_price를 이용해 수요일의 종가를 화면에 출력하세요.
print("5", naver_closing_price[2])

#6 문제 3-1의 표 3.2를 이용해 날짜를 딕셔너리의 키 값으로, 종가를 딕셔너리의 값으로 사용해 naver_closing_price2라는 딕셔너리를 만드세요.

naver_closing_price2 = {"09/07":474500, "09/08":461500, "09/09":501000, "09/10":500500, "09/11":488500}
print("6",naver_closing_price2)

#7 문제 3-6에서 만든 naver_closing_price2 딕셔너리를 이용해 09/09일의 종가를 출력하세요.
print(naver_closing_price2['09/09'])

#1 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
a = '881120-1068234'
x,y = a.split('-')
print("1", x,y)

#2 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = '881120-1068234'
print("2", pin[7])

#3 문자열의 replace 함수를 이용하여 위 문자열을 다음과 같이 고치시오.
b = 'a:b:c:d'
print("3", b.replace(':','#'))

#4 문자열의 split와 join 함수를 이용하여 위 문자열을 다음과 같이 고치시오.
b = 'a:b:c:d'
b = ('#').join(b.split(':'))
print("4", b)

#1 중복을 허용하지 않는 집합 자료형의 특징을 이용하여 다음 a 리스트에서 중복된 숫자들을 제거해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)

print("1", b)


#2 집합 자료형은 다음과 같이 만들 수 있다.
a = {'a', 'b', 'c'}
print(a)
print(type(a))

a = set()
print(type(a))






















