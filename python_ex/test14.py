#141 my_list 에서 대문자만 화면에 출력하라.
print("141: " , end='')
my_list = ["A", "b", "c", "D"]
for i in my_list:
    if i.isupper() == True:
        print(i)

#142 my_list 에서 소문자만 화면에 출력하라.
print("142: ", end='')
my_list = ["A", "b", "c", "D"]        

for i in my_list:
    if i.islower() == True:
        print(i)

#143 문자열의 upper() 메서드는 문자열을 대문자로 변경하고, lower() 메서드는 소문자로 변환한다.
#리스트의 문자를 대문자는 소문자로, 소문자는 대문자로 변환하라.
print("143: ", end='')

my_list = ["A", "b", "c", "D"]
for i in my_list:
    if i.islower() == True:
       print(i.upper(), end = "")
    else:
        print(i.lower(), end = "")


#144 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split 메서드를 사용)
print("144: ", end='')
file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']

for i in file_list:
    print(i.split(".")[0])


#145 파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h인 파일을 출력하라.
print("145: ", end='')
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in filenames:
    if i.split('.')[1] == 'h':
        print(i)

#146 파일 이름이 리스트에 저장되어 있을 때 확장자가 .h나 .c인 파일을 화면에 출력하라.
print("146: ", end='')
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in filenames:
    if i.split('.')[1] == 'h' or i.split('.')[1] == 'c':
        print(i)
    # if i.endswith(("h", "c")) :
    #     print(i)

#147 my_list에서 양수만 new_list 이름의 리스트에 저장하라.
print("147: ", end='')
my_list = [3, -20, -3, 44]
new_list = []
for i in my_list:
    if i > 0:
        new_list.append(i)
print(new_list)

#148 my_list 에서 대문자만을 upper_list에 저장하라.
print("148: ", end='')
my_list = ["A", "b", "c", "D"]

upper_list = []
for i in my_list:
    if i.isupper() == True:
        upper_list.append(i)

print(upper_list)

#149 my_list의 값을 sole_list에 저장하라. 단, 중복된 값은 제거한다.
print("149: ", end='')
my_list = [3, 4, 4, 5, 6, 6]
sole_list = []

for i in my_list:
    if i not in sole_list:
        sole_list.append(i)

# sole_list = list(set(my_list)) <- 한줄로도 가능

print(sole_list)

#150 내장 함수를 사용하지 않고 반복문을 사용해서 my_list에 저장된 모든 수의 합를 출력하라
print("150: ", end='')
my_list = [3, 4, 5]
sum = 0
for i in my_list:
    sum += i
print(sum)







