# creating dataset
set1 = {5,10}
print(set1)
print(type(set1))

# create list
my_list=[1,2,3,4,5,5]
my_set_from_list=set(my_list)
print(my_set_from_list)

# create set
my_set = set([2,4,6])
print("My set is:", my_set)
print("Is 3 in set:", 3 in my_set)
print("Is 6 in set:", 6 in my_set)
print("Is 4 NOT in set:", 4 not in my_set)

from itertools import product as prod
A= set([x for x in range(1,7)])
B= set([x for x in range(1,7)])
P=list(prod(A,B))

# outcomes
print("Outcome of dice A:", A)
print("Outcome of dice B:", B)
print("Possible outcome of A and B together:\n", P)

n_dice = 2
dice_faces={1,2,3,4,5,6}
#set of all possible events
event_space = set(prod (dice_faces, repeat = n_dice))

for outcome in event_space:
  print(outcome, end=', ')
print()
print(len(event_space))

# favorable outcomes
favorable_outcome = []
for outcome in event_space:
  x,y = outcome
  if (x+y)%3 ==0:
    favorable_outcome.append(outcome)
favorable_outcome = set(favorable_outcome)

for f_outcome in favorable_outcome:
  print(f_outcome,end =',')
print()
print(len(favorable_outcome))

prob = len(favorable_outcome)/len(event_space)
print("The probability of getting a sum which is divisible by 3 is:", prob) 