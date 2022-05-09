#armstrong
num  = input('Enter a number: ')
power = len(num)
sum = 0
num = int(num)

a = num
while a > 0:
    b = a % 10
    #print(f'b: {b}')
    sum += b ** power
    #print(f'sum: {sum}')
    a //=10
    #print(f'a: {a}')

if num == sum:
    print(num,'is an armstrong number.')
else:
    print(num,'is not an armstrong number.')