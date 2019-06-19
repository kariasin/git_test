#121 아래 for 문에서 print 문은 몇 번 호출 되는가?
print("121:")
for i in ["가", "나", "다", "라"]:
    print(i)

# -> 4번


#122 아래 코드의 실행 결과를 예측하라.
print("122:")
for i in ["사과", "귤", "수박"]:
    print(i)


#123 아래 코드의 실행 결과를 예측하라.
print("123:")
for i in ["사과", "귤", "수박"]:
    print(i)
    print("--")


#124 아래 코드의 실행 결과를 예측하라.
print("124:")
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
print("--")

#125 menu 리스트에는 판매중인 메뉴가 저장돼 있다. 아래와 같이 화면에 출력하라.

menu = ["김밥", "라면", "튀김"]
print("125:")
for i in menu:
    print("오늘의 메뉴: ", i)


#126 portfolio에는 보유중인 주식 목록이 저장돼 있다. 아래와 같이 화면에 출력하라.
print("126:")
portfolio = ["SK하이닉스", "삼성전자", "LG전자"]

for i in portfolio:
    print(i, "보유중")


#127 다음과 같이 애완 동물 리스트가 있을 때 애완 동물의 이름과 애완 동물의 글자수를 출력하라.
print("127:")
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
num = 0
for i in pets:
    print(i, len(pets[num]))
    num += 1

#128 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 화면에 출력하라. 단 부가세는 10원으로 가정한다.
print("128:")
prices = [100, 200, 300]
for i in prices:
    print(i+10)


#129 prices 리스트에는 가격정보가 문자열로 저장돼 있다. prices 리스트에 저장된 모든 데이터를 파이썬 숫자 형으로 변환 후 화면에 출력하라.
print("129:")
prices = ["129,300", "1,000", "2,300"]


for i in prices:
    temp = i.replace(',','')
    print(temp)
  

#130 menu 리스트에는 음식이름이 뒤집혀 저장돼 있다. 이를 읽기 좋게 뒤집어서 아래와 같이 출력하라.
menu = ["면라", "밥김", "김튀"]
for i in menu:
    print(i[::-1])
    

