#71 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores
print("71: " + str(valid_score))

#72 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score = scores
print("72: " + str(valid_score))

#73 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b = scores
print("73: " + str(valid_score))


#74 temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}

#75 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
icecream = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print("75: " + str(icecream))

#76 073 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print("76: " + str(icecream))

#77 074에서 만든 딕셔너리를 사용하여 메로나 가격을 출력하라.
print("77: " + str(icecream["메로나"]))

#78 075에서 만든 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
icecream["메로나"] = 1300
print("78: " + str(icecream))


#79 076에서 만든 딕셔너리에 메로나를 삭제하라.
del icecream["메로나"]
print("79: " + str(icecream))

#80 다음 코드에서 에러가 발생한 원인을 설명하라.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바'] = 1000
print("80: " + str(icecream))