import numpy as np

#array create
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])

#print(arr1d)
#print(arr2d)


#math operators
math_arr1 = np.array([1,2,3])
math_arr2 = np.array([4,5,6])

#print(math_arr1 +math_arr2)
#print(math_arr1*math_arr2)

#Array reshape

arr_r = np.array([1,2,3,4,5,6])
print(arr_r.mean())
print(arr_r.max())
print(arr_r.min())
print(arr_r.reshape(2,3))
