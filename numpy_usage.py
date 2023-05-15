import numpy as np

numbers = [[1, 2, 3],[ 4, 5, 6]]

np_array = np.array(numbers)

print(np_array)
print(type(np_array))
print(np_array.ndim)
print(np_array.shape)
print(np_array.dtype)


zero_array = np.zeros((4,4))
print(zero_array)

ones_array = np.ones((4, 3))
print(ones_array)

identity_array = np.eye(4,4)
print(identity_array)

arange_array = np.arange((2))
print(arange_array)


new_array = np.array([[1,2,3,4], [5, 6, 7, 8]])
print(new_array)

print(new_array.shape)

new_array.shape = (4,2)
print(new_array)