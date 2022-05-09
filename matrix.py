import numpy as n
a=n.array([[10,15]])
b=n.array([[15,20]])
print(a)
print(b)
print('add: ',a+b)
print('transpose: ',a.T+b.T)
print('sub: ',a-b)
#scalar
s=5
c=n.array([[5,7]])
print('scalar mul: ',s*c)
#matrix mul
print('matrix mul: ',a*b)
#dot mul
print('dot mul: ',n.dot(a,b.T))
#matrix sum
print('matrix sum: ',a+b)
#identity
im=n.eye(4)
print('identity matrix: ',im)
#inverse
d=([[1,2,0],[0,1,2],[2,0,1]])
print('D: ',d)
print('inverse: ',n.linalg.inv(d))