#101 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# input_txt = input()
# print("101: " + str(input_txt * 2))

#102 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# in_Num = int(input())
# in_Num += 10
# print("102: " + str(in_Num))


#103 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# in_Num = int(input())
# if in_Num % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

#104 사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 단 값의 범위는 0~255로 가정한다. 255를 초과하는 경우 255를 출력해야 한다.
# in_Num = int(input())

# print("104:")
# print("입력값:", in_Num)
# in_Num += 20
# if in_Num > 255:
#     in_Num = 255 
# print("출력값:", in_Num)

#105 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.
# in_Num = int(input())

# print("105:")
# print("입력값:", in_Num)
# in_Num -= 20
# if in_Num < 0:
#     in_Num = 0
# print("출력값:", in_Num)


#106 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# in_txt = input()
# print("106:")
# print("현재시간:", in_txt[0:2] + ":" + in_txt[2:])
# if in_txt[2:] == '00':
#     print("정각 입니다.")
# else:
#     print("정각 아닙니다.")


#107 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# in_txt = input()
# fruit = ["사과", "포도", "홍시"]
# if in_txt in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")


#108 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# in_txt = input()
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# if in_txt in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")


#109 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# in_txt = input()
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# if in_txt in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")


#110 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
in_txt = input()
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if in_txt in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")


