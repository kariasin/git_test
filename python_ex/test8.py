#81 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print("81: " + str(inventory))

#82 081의 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print("82: " + str(inventory['메로나'][0]), "원")


#83 081의 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print("83: " + str(inventory['메로나'][1]), "개")

#84 081의 inventory 딕셔너리에 아래 데이터를 추가하라.
inventory['월드콘'] = [500,7]
print("84: " + str(inventory))


#85 다음의 딕셔너리에서 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print("85: " + str(list(icecream.keys())))

#86 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
print("86: " + str(list(icecream.values())))

#87 icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.

print("87: " + str(sum(icecream.values())))    

#88 new_product에는 두 개의 데이터가 있기 때문에, 하나씩 데이터를 추가할 수 있습니다. 하지만, 딕셔너리의 데이터가 수백, 수천개라면 하나씩 손으로 추가하기 어렵습니다.

icecream.update({'팥빙수':2700,'아맛나':1000})
print("88: " + str(icecream))

#89 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print("89: " + str(result))

#90 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))

print("90: " + str(close_table))