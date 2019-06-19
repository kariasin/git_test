#91 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
#boolean
print("91: " + str(bool(0)))

#92 아래 코드의 출력 결과를 예상하라
print("92: " + str(3 == 5)) 

# -> false

#93 아래 코드의 출력 결과를 예상하라
print("93: " + str(3 < 5))

# -> true

#94 아래 코드의 결과를 예상하라.
x = 4
print("94: " + str(1 < x < 5))

# -> true

#95 아래 코드의 결과를 예상하라.
print ("95: " + str((3 == 3) and (4 != 3)))

# -> true

#96 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
print("96: " + str(3 >= 4))

# -> (=>) 잘못 사용함 (>=) 이걸로 변경해야함

#97 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("97: Hello World")

#-> 아무것도 출력안됨

#98 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("98: Hello World.")
else:
    print("98: Hi, there.")

# -> Hi, there.

#99 아래 코드의 출력 결과를 예상하라
if True :
    print ("99: 1")
    print ("99: 2")
else :
    print("99: 3")
print("99: 4")


# -> 1, 2, 4

#100 아래 코드의 출력 결과를 예상하라

if True :
    if False:
        print("100: 1")
        print("100: 2")
    else:
        print("100: 3")
else :
    print("100: 4")
print("100: 5")

# -> 3, 5