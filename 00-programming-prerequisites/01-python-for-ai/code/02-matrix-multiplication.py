import numpy as np

A=np.array([
  [1,2,3],
  [4,5,6]
])
B=np.array([
  [7,8],
  [9,10],
  [11,12]
])

C=A @ B
print(C)

X=np.array([
  [7,2],
  [9,5]
])
Y=np.array([
  [1,7],
  [4,9]
])

Z= X @ Y;
print(Z)
print("C's shape is: ", C.shape)
print("Z's shape is: ", Z.shape)