#51 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]

print("51: " + str(price[1:]))

#52 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("52: " + str(nums[0::2]))


#53 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("53: "+ str(nums[1::2]))

#54 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print("54: " + str(nums[::-1]))


#55 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라. --> 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
interest.remove("LG전자")
print("55: " + str(interest[0]), str(interest[1]))

#56 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("56: " + ' '.join(interest))
#
#57 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("57: " + '/'.join(interest))


#58 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

interest_str = "\n".join(interest)
print("58: " + interest_str)

#59 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# 이를 interest 이름의 리스트로 분리 저장하라.
string = "삼성전자/LG전자/Naver"
interest = [string[0:4],string[5:9],string[10:15]]

print("59: " + str(interest))

#60 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# 이를 interest 이름의 리스트로 분리 저장하라.
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"

interest = string.split('/')
print("60: " + str(interest))