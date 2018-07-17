'''
Write a program which prints all the even, odd, and prime number from a list Separately
 Eg
 Input = Lis = [1,2,3,4,5]
 Output =
 even = 2,4
 Odd = 1,3,5
 Prime = 2,5
'''
import random
Input = Lis = [1,2,3,4,5]
factors = []

for i in range(20):
    Lis.append(random.randrange(0,9))
Input = Lis = [1,2,3,4,5,"hi","hello"]

def prime(i):
    j = 1
    for j in range(2,i):
        if i%j == 0:
            break
    if i-1 == j:
        return True
    else:
        return False

print(Lis)
Lis_string = []
Lis_num =[]
for i in Lis:
    if type(i) is str:
        Lis_string.append(i)
    else:
        Lis_num.append(i)

print(Lis_num)
print("Even numbers:",list(filter(lambda x: x%2==0, Lis_num)))
print("ODD numbers:",list(filter(lambda x: not x%2==0, Lis_num)))
print("Prime numbers:",list(filter(lambda x: prime(x), Lis_num)))
print("Even numbers:",Lis_string)
