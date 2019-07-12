import numpy as np

# 2 * 3 ( 2 rank(행), 3 shape(열)로 배열 생성하기)
np_array = np.array([[1,2,3],[4,5,6]]) # 리스트로 생성하기

#  배열 읽기
print(np_array[0])
print(np_array[0][1])
print(np_array[1][1])
print(np_array.shape)

np_array2 = np.array([[[ 0,  0,  0,  0],
                      [ 1,  2,  3,  4],
                      [ 2,  2,  2,  2]],

                     [[ 3,  3,  3,  3],
                      [ 4,  4,  4,  4],
                      [ 5,  5,  5,  5]]])

print(np_array2[0])
print(np_array2[0,1])
print(np_array2[0,1,1])
print(np_array2.shape)            

print(np_array2[1,1,1])
np_array2[1,1,1] = 2
print(np_array2[1,1,1])



# 1. 3차원 배열로, 1차원은 3개, 2차원은 2개, 3차원은 1개로 만들어보기, 모든 값은 0
np_array3 = np.array([
                        [[0],
                         [0]],
                        [[0],
                         [0]],
                        [[0],
                         [0]]
                    ])
print(np_array3.shape)