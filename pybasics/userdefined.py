# Write a python program for implementing user defined functions
name = input("Enter name: ")
sub = input("Enter subject: ")

def print_info(x,y):
    print("{0}, welcome to {1}".format(x,y))

print_info(name,sub)