'''Most duplicate number = Take a list lis = [1,7,8,5,4,6,1,2,7,8,9,1,2,1]. and write a program which prints
   the number which repeats itself Maximum number of times in that list
 Bonus = Your program must create a random list which contains 15 integers Everytime you run the program
 What will you do if there are more than one number which repeats itself
'''
import random

lis = []
for i in range(15):
    lis.append(random.randrange(0,9))

print("List of Values \n",lis)

val=0
count =0

for i in lis:
    if lis.count(i) > count:
        val = i
        count = lis.count(i)

print("{0} is repeted maximum number of times {1} ".format(val,count))

'''
10). Ascending / Descending :- Write a program which prints the list lis = [1,7,8,5,4,6,1,2,7,8,9,1,2,1]. in Ascending and descending order.
'''
lis.sort()
print("Ascending Order", lis)
lis.reverse()
print("Descending Order", lis)
