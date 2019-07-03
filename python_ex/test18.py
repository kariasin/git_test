#정규식 표현

import re

pattern = re.compile('[a-z]+')
pattern2 = re.compile('[a-zA-Z]+')
t1 = pattern.match("Dave") 
t2 = pattern.search("Dave")
t3 = pattern.findall('Game of Life in Python')
t4 = pattern2.findall('Game of Life in Python')
t5 = pattern2.finditer('Game of Life in Python')
# print(t1)
# print(t2)
# print(t3)
#print(t4)

# for i in t5:
#     print(i.group(), end="\n")
#     print(i.start(), end="\n")
#     print(i.end(), end="\n")
#     print(i.span(), end="\n")

pattern3 = re.compile(' [A-Z]{2} ')
t11 = pattern3.split("java VS test")
print(t11)

pattern4 = re.compile('-')
t12 = pattern4.sub('*','801210-1011323')
t13 = re.sub('-','*','801210-1011323')
print(t12)
print(t13)
#주민번호 뒷자리 * 표시로 변경
t14 = re.sub('[0-9]{7}','*******','801210-1011323')

print(t14)