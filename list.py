#list operations
l=[1,'a',3,'b','c','d']

#index
print('index: ',l[3])
#range
print('range: ',l[0:5])
#insert
l[2]=2
print('insert element: ',l)
#delete
del (l[3])
print('delete: ',l)
#length
print('length: ',len(l))
#replicate
print('replicate: ',l*3)
#reverse
print('reverse: ',l[::-1])