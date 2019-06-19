#131 my_list에는 네 개의 데이터가 저장되어 있다. 첫 번째 데이터를 제외하고 나머지 데이터를 한 라인에 하나씩 출력하라.
print("131:")
my_list = ["가", "나", "다", "라"]

for i in my_list[1:]:
    print(i)


#132 my_list의 데이터 중에서 홀수 번째 위치의 값을 화면에 출력하라.
print("132:")
my_list = [1, 2, 3, 4, 5, 6]

for i in my_list[0::2]:
    print(i)

#133 my_list의 데이터 중에서 짝수 번째 위치의 값만을 화면에 출력하라.
print("133:")
my_list = [1, 2, 3, 4, 5, 6]

for i in my_list[1::2]:
    print(i)


#134 my_list의 데이터를 아래와 같이 역방향으로 출력하라.
print("134:")
my_list = ["가", "나", "다", "라"]
for i in my_list[::-1]:
    print(i)



#135 my_list에서 음수를 출력하라
print("135:")
my_list = [3, -20, -3, 44]
for i in my_list:
    if i < 0:
        print(i)



#136 my_list에서 3의 배수를 출력하라.
print("136:")
my_list = [3, 100, 23, 44]
for i in my_list:
    if i % 3 == 0:
        print(i)


#137 my_list에서 세 글자 이상의 문자를 화면에 출력하라
print("137:")
my_list = ["I", "study", "python", "language", "!"]
for i in my_list:
    if len(i) > 3:
        print(i)


#138 my_list에서 5보다 크고 10보다 작은 수를 화면에 출력하라
print("138:")
my_list = [3, 1, 7, 10, 5, 6]
for i in my_list:
    if 5 < i < 10:
        print(i)


#139 my_list에서 10보다 크고 20 보다 작으면서 3의 배수일 경우 화면에 출력하라
print("139:")
my_list = [13, 21, 12, 14, 30, 18]
for i in my_list:
    if 10 < i < 20 and i % 3 == 0:
        print(i)

#140 my_list에서 3의 배수이거나 4의 배수를 화면에 출력하라
print("140:")
my_list = [3, 1, 7, 12, 5, 16]

for i in my_list:
    if i % 3 == 0 and i % 4 == 0:
        print(i)