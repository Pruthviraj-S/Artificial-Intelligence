#string operations.
str='hello world!'
#index
print('index:',str.index('h'))
#strip
strs='     space       '
print('strip:',strs.strip())
#count
print('count:',str.count('l'))
#split
print('split:',str.split(' '))
#upper
print('upper:',str.upper())
#lower
print('lower:',str.lower())
#isupper
print('isupper:',str.isupper())
#islower
print('islower:',str.islower())
#translate
dict = {101: 69, 104: 72}
print('translate:',str.translate(dict))
#format
print('string is: {0}'.format(str))
#find
print('find:',str.find('wo'))
#center
print('center:',str.center(20,'*'))
#join
str2='*'
print('join:',str2.join(str))