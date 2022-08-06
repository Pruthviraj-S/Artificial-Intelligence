# Write a python program for implementing conditions and loops
a = int(input("Enter a number: "))
b = 0

for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end="  ")
    while b != (2*i-1):
        print("* ", end="")
        b += 1

    b = 0
    print()

# number pyramid
rows = int(input("Enter number of rows: "))

k = 0
c1 = 0
c2 = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        c1 += 1

    while k != ((2*i)-1):
        if c1 <= rows-1:
            print(i+k, end=" ")
            c1 += 1
        else:
            c2 += 1
            print(i+k-(2*c2), end=" ")
        k += 1

    c2 = c1 = k = 0
    print()
