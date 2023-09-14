import numpy as np 
list1, list2 = [1,2,3,4] , [1,2,3,4]
a = np.array(list1)
b = np.array(list2)

c = np.zeros((2,5), int)
d = np.ones((3,1))
e = np.empty((1,5), float)
f = np.full(5,15, float)

np.random.seed(10)

a = np.random.rand(2,3)
b = np.random.rand(3,2)
c = np.random.rand(6)
d = np.random.randint(1,100,6)

d = d.reshape(2,-1)
print(d)
# c = np.reshape(c,(2,3))
# print(c)