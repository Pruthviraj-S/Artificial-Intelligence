a = int(input("Enter a number: "))
b = 0

for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end="  ")
    while b!=(2*i-1):
        print("* ", end="")
        b += 1
   
    b = 0
    print()