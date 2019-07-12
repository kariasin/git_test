import numpy as np
x = np.array([[0,2],
              [3,2]])
y = np.array([[2,2],
              [1,2]])

# print(np.add(x,y))      #동일자리 덧셈
# print(np.subtract(x,y)) #동일자리 뺄셈
# print(np.multiply(x,y)) #동일자리 곱셈
# print(np.dot(x,y))      #행렬 곱셈
# print(np.divide(x,y))   #동일자리 나눗셈

print(np.array(range(10,21)))
print(np.array(range(10,20)).reshape((2,5)))

A = np.array(range(1,13)).reshape(3,4)
B = np.array(range(1,13)).reshape(4,3)
print(A)
print(B)
print(np.dot(A,B))
