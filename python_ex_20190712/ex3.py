import numpy as np

# zeros(): 모든 값을 0으로 하는 배열 만들기
# ones():  모든 값을 1으로 하는 배열 만들기
# full():  모든 값을 특정 값으로 하는 배열 만들기
# eye():   대각선으로는 1, 나머지는 0으로 하는 2차원 배열 만들기 


np_array = np.zeros((2,2)) # 입력은 각차원의 크기, shape 메서드의 결과값과 동일, 입력 타입이 튜플()임을 확인
#print(np_array)

np_array = np.zeros((2,3))
#print(np_array)

np_array = np.zeros((3,2,1))
#print(np_array)


np_array = np.ones((2,2))
#print(np_array)


np_array = np.full((2,3), 4) # 입력은 각차원의 크기, shape 메서드의 결과값과 동일,입력 타입이 튜플()과 특정 값 두개임을 확인
#print(np_array)

np_array = np.eye(3)
#print(np_array)

# 1. 길이가 5이고, 값이 각각 0인 1차원 배열을 만드세요 

np_array = np.zeros(5)
#print(np_array)

# 2. 길이가 10이고, 값이 각각 1인 2x5 배열(행렬)을 만드세요 
np_array = np.ones((2,5))
#print(np_array)

