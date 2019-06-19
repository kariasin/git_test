#111 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.

# in_txt = input()

# if in_txt.islower():
#     print(in_txt.upper())
# else:
#     print(in_txt.lower())

#112 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~6p0	C
# 21~40	D
# 0~20	E

# in_num = int(input())
# str_txt = ""
# if 81 <= in_num <= 100:
#     str_txt ='A'
# elif 61 <= in_num <= 80:
#     str_txt ='b'
# elif 41 <= in_num <= 60:
#     str_txt ='C'
# elif 21 <= in_num <= 40:
#     str_txt ='D'
# else:
#     str_txt = "E"
# print("score: ", in_num)
# print("grade is", str_txt)


#113 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.


# don = {'달러':1167, '엔':1096, '유로':1268, '위안':171}
# amount, currency = input().split(' ')

# print("113:")

# if currency == '달러':
#     ratio = 1167
# elif currency == '엔':
#     ratio = 1096   
# elif currency == '유로':
#     ratio = 1268
# elif currency == '위안':
#     ratio = 171

# print("입력:", amount, "달러")
# print(int(amount) * ratio, "원")

#114 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# print("114:")
# num1 = int(input("number1: "))
# num2 = int(input("number2: "))
# num3 = int(input("number3: "))

# num_max= (num1, num2, num3)
# print(max(num_max))

#115 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
#print("115: ")
# p_list = {'011':'SKT', '016':'KT', '019':'LGU', '010':'알수없음'}
# phone = input("휴대전화 번호 입력: ").split('-')

# print("당신은", p_list[phone[0]], "사용자입니다.")
# print(phone)

#116 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# print("116: ")
# a_list = {'010':'강북구', '011':'강북구','012':'강북구','013':'도봉구','014':'도봉구',
#         '015':'도봉구','016':'노원구','017':'노원구','018':'노원구','019':'노원구',}
# addr = input("우편번호: ")
# print(a_list[addr[0:3]])


#117 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# gender = {'1':'남자', '2':'여자', '3':'남자', '4':'여자'}
# pri_num = input("주민등록번호: ")

# print(gender[pri_num[7]])

#118 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

# pri_num = input("주민등록번호: ")
# p_num = int(pri_num[8:10])
# if 0 < p_num < 8:
#     print("서울 입니다.")
# elif 9 < p_num < 12:
#     print("부산 입니다.")
# else:
#     print("서울이 아닙니다.")


#119 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

# 8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# print("119:")
# p_id = input("주민등록번호: ")
# num = 2
# sum = 0
# for i in p_id:
#     sum += int(i) * num
#     if num >= 9:
#         num = 2
#     elif num < 9:
#         num += 1
# sum -= int(p_id[12])
# sum = 11 - (sum % 11)
# print("sum: ", sum)
# if sum == p_id[12]:
#     print("유효한 주민등록번호")
# else:
#     print("유효하지 않은 주민등록번호")

#120 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다. 
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# import requests

# url = 'http://google.com'
# response = requests.get(url=url)
# print(response.status_code)

# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# print(btc)






