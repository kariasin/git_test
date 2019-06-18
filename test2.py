#11 아래 코드의 실행 결과를 예상하라.
a = "3"
b = "4"
print(a+b) #--> 34

#12 변수 s와 t에는 각각 문자열이 바인딩 되어있다. s = "hello" t = "python"
#두 변수를 이용하여 아래와 같이 출력하라. -> hello! python
s = "hello"
t = "python"
s = s + "! " + t
print(s)

#13 아래 코드의 실행 결과를 예상하라.
print("Hi" * 3)

#14 화면에 '-'를 80개 출력하라.
print("-"*80)

#15 변수에 다음과 같은 문자열이 바인딩되어 있다. 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력하여라.
#t1 = 'python'   t2 = 'java'
#변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력하여라.
#python java python java python java python java
t1 = "python "
t2 = "java "
s = t1 + t2
print(s*4)

#16 LG전자 주식을 10주 보유하고 있습니다. 금일 종가 20,000원일 경우 총 평가 금액을 화면에 출력하라
num = 10
price = 20000
print(num * price)

#17 아래 코드의 실행 결과를 예측하라.
2 + 2  * 3
print(2 + 2  * 3)


#18 type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#>> a = 128
#>> print (type(a))
#<class 'int'>
#아래 변수에 바인딩된 값의 타입을 판별하라. -> a = "132"
a = "132"
print(type(a))

#19 문자열 '720'를 정수형으로 변환하라.
s = "720"
print(int(s))


#20 정수 100을 문자열 '100'으로 변환하라.
num = 100
print(str(num))