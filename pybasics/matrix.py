# Write a python program for demonstrating use of numPy
import numpy as n
a=n.array([[10,15]])
b=n.array([[15,20]])
print('\nA: ',a)
print('\nB:',b)
print('\nadd: ',a+b)
print('\ntranspose: ',a.T+b.T)
print('\nsub: ',a-b)
#scalar
s=5
c=n.array([[5,7]])
print('\nscalar mul: ',s*c)
#matrix mul
print('\nmatrix mul: ',a*b)
#dot mul
print('\ndot mul: ',n.dot(a,b.T))
#matrix sum
print('\nmatrix sum: ',a+b)
#identity
im=n.eye(4)
print('\nidentity matrix: ',im)
#inverse
d=([[1,2,0],[0,1,2],[2,0,1]])
print('\nD: ',d)
print('\ninverse: ',n.linalg.inv(d))