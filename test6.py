#61 다음 코드의 결과값에 대해 예측하여라
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)
# -->  ['Naver', 'LG전자', 'SK Hynix']



#62 다음 코드의 결과값에 대해 예측하여라
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)

# --> ['삼성전자', 'LG전자', 'SK Hynix']

#63 my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()

#64 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
# --> 이코드 오류남 t[0] = 'a'
print(t)

# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# --> 튜플은 변경 불가

#65 숫자 1 이 저장된 튜플을 생성하라.
num = (1,)

#66 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))

# --> 튜플

#67 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#68 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_list = list(interest)
print(interest_list)

#69 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest_tuple = tuple(interest)
print(interest_tuple)


#70 아래 코드의 실행 결과를 예측하라
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)














