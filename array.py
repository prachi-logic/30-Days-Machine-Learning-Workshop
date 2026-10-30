import numpy as np
arr=[2,6,7,0,8,9]
print(arr)
print(type(arr))

#2D array
arr1=[2,3,4,6.7,8]
arr2=[4,6,7,0,91]
arr= np.array([arr1,arr2])
print(arr)

#zero array
a1=np.zeros((2,3))
print(a1)

#  identity matrix
a1 = np.ones((3, 3))
print(a1)

#sam elemnet matrix
af = np.full((2, 2), 7)
print(af)

# index
ar = np.arange(0, 10, 2)  # start, stop, step
print(ar)

#
la = np.linspace(0, 1, 5)  # start, stop, num
print(la)

#shape --they give row and column number
a=np.array([[1,2,3],
            [4,5,6]])
print(a.shape)

# size

#a=np.array([[20,10,60]],[[20,30,70]])
#print(a.size)

#ndim --give dimensions
a=np.array([1,2,3])
print(a.ndim)

a2=np.array([[2,3,4],
            [4,6,7]])
print(a2.ndim)
    

a3=np.array([[2,3],
            [4,5],
            [6,7]])
print(a3.ndim)

#Data type

a=np.array([2,7,8,9,10])
print(a.dtype)

#float
a=np.array([0.5,7.9,8.9])
print(a.dtype)

#Indexingg


arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])

# slicing

arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[1:4])
print(arr[::1])
print(arr[2:4])


#fancy indeximg
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])

#Mathemtical operations
arr=np.array([10,20,30])
print(arr+5)
print(arr*6)
print(arr-5)
print(arr%2)
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.var(arr))
print(np.std(arr))