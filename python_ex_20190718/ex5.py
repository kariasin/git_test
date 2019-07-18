#최대공약수 만들기(테스트 함수)
def gcd(num1, num2):
    if type(num1) is not int:
        return 0
    if type(num2) is not int:
        return 0
    
    if num1 < 1 or num1 > 100:
        return 0
    if num2 < 1 or num2 > 100:
        return 0

    if num1 > num2:
        divisor = num2
    else:
        divisor = num1
# 10 ~ 1까지 테스트하면, 1일 때 불필요하게 나머지를 구하게 됨, 10 ~ 2까지로!
    for index in range(divisor, 0, -1):
        if (num1 % index == 0) and (num2 % index == 0):
            return index
    return 1
#테스트 입력
result = gcd(20.0,15)
result2 = gcd(93,15)

if result == 0:
    print("입력에 문제 있음")
else:
    print("최대 공약수는 " + str(result) + " 입니다.")

if result2 == 0:
    print("입력에 문제 있음")
else:
    print("최대 공약수는 " + str(result2) + " 입니다.")
